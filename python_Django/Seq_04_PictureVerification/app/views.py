from django.shortcuts import render
from django.views.generic.base import View
from django.http import HttpResponse, StreamingHttpResponse
from app.forms import RegisterForm


# 注册表单，带有验证码
class RegisterView(View):
    def get(self, request):
        registerForm = RegisterForm()
        return render(request, "Seq_01_Reg.html", {"registerForm": registerForm})

    def post(self, request):
        registerForm = RegisterForm(request.POST)
        if (registerForm.is_valid()):
            name = registerForm.cleaned_data['name']
            pwd = registerForm.cleaned_data['pwd']
            email = registerForm.cleaned_data['email']
            captache = registerForm.cleaned_data['captcha']
            print(name, pwd, email)
            print(captache)
            return HttpResponse("OK")
        else:
            return render(request, "Seq_01_Reg.html", {"registerForm": registerForm})


def index(request):
    return render(request, "Seq_02_upload.html")


from django.conf import settings


# 文件的上传一
def getUpload(request):
    if request.method == "POST":
        file = request.FILES['filename']
        print(file.name)
        # f = "static/upload/" + file.name
        f = "%s%s" % (settings.MEDIA_ROOT, file.name)
        with open(f, mode="wb+") as pic:
            for c in file:
                pic.write(c)
        return HttpResponse("上传成功！")
    else:
        return HttpResponse("上传失败！")


from app.forms import UploadForms


# 文件的上传二
def uploadForm(request):
    if request.method == "GET":
        uploadForm = UploadForms()
        return render(request, "Seq_03_upload.html", {"uploadForm": uploadForm})
    else:
        uploadForm = UploadForms(request.POST, request.FILES)
        if uploadForm.is_valid():
            file = uploadForm.cleaned_data['file']
            f = "%s%s" % (settings.MEDIA_ROOT, file.name)
            with open(f, mode="wb+") as pic:
                for c in file.chunks():
                    pic.write(c)
            return HttpResponse("上传成功！")
        else:
            return HttpResponse("上传失败！")


from django.utils.http import urlquote
import time


# 文件下载
def downloadfile(request):
    print("开始下载文件")
    file = "app/static/img/favicon.ico"
    filename = u"蒋林平jianglp"
    # 解决中文乱码问题
    filename = urlquote(filename)
    with open(file, "rb") as f:
        c = f.read()
        resp = HttpResponse(c)
        resp['Content-Type'] = "application/octet-stream"
        resp['Content-Disposition'] = 'attachment; filename=%s' % (filename) \
                                      + time.strftime('%Y%m%d', time.localtime(time.time())) + '.ico'
    return resp


# 文件下载优化 迭代器
def file_read_iterator(filepath, bluk_size=512):
    with open(filepath, "rb") as f:
        while True:
            c = f.read(bluk_size)
            if c:
                yield c
            else:
                break


def downloadfile2(request):
    print("开始下载文件2")
    file = "app/static/img/favicon.ico"
    filename = u"蒋林平jianglp"
    # 解决中文乱码问题
    filename = urlquote(filename)
    # 每次读取 512 字节
    resp = StreamingHttpResponse(file_read_iterator(file))
    resp['Content-Type'] = "application/octet-stream"
    resp['Content-Disposition'] = 'attachment; filename=%s' % (filename) \
                                  + time.strftime('%Y%m%d', time.localtime(time.time())) + '.ico'
    return resp
