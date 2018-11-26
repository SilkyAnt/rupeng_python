from django.shortcuts import render
from django.http import HttpResponse


# Create your views here.
def index(request):
    return render(request, "index.html")


def main(request):
    return render(request, "main.html")


def person(request):
    # 传递字典
    return render(request, 'person.html', {"name": "czf", "age": "18", "address": "北京昌平"})


def person2(request):
    # 传递所有的参数
    name = "youname"
    age = "18"
    address = "北京昌平"
    return render(request, 'person.html', locals())


def person3(request):
    # 传递一个键值对(字典)的对象
    p1 = {"name": "czf", "age": "28", "address": "北京昌平"}
    hobby = "reading"
    print(type(p1))
    # 错误的传递方式 p1=p1
    return render(request, 'person3.html', {"p": p1, "hobby": hobby})


def subject(request):
    subjectLists = ["Python", "Redis", "MongoDB", "AI", "Big_Data", "H5"]
    a = []
    scores = [12, 100, 99, 22, 78, 88, 60, 48]
    ss = {"Python": 100, "Redis": 80, "MongoDB": 88, "AI": 99, "Big_Data": 70, "H5": 60}
    return render(request, "subject.html", {"subjectLists": subjectLists,
                                            "a": a, "scores": scores, "ss": ss})


def requestDemo(request):
    '''
    # request 常见属性
    print(request.scheme)
    print(request.method)
    print(request.encoding)
    print(request.path)
    print(request.path_info)
    print(request.body)
    print(request.user)
    print(request.COOKIES)
    print(request.session)
    print("###############")
    for t in request.META:
        print(t, ":", request.META[t])
    '''
    # request 常见方法
    print(request.get_host())
    print(request.is_ajax())
    print(request.is_secure())
    print(request.get_full_path())
    print(request.get_port())

    return render(request, "request.html")


def goDataPage(request):
    return render(request, "data.html")


def getAData(request):
    a = (int)(request.GET['a'])
    b = (int)(request.GET['b'])
    print(a, b)
    return HttpResponse(str(a + b))


def goFormPage(request):
    return render(request, "form.html")


def login(request):
    # 用 POST 方法 来接收数据和用 GET 方法来接收数据差不多
    # 将下面的GET改为POST来接收数据，并且在HTML页面中添加一行代码
    # {% csrf_token %}
    print(request.GET)
    name = request.GET['username']
    pwd = request.GET['userpwd']
    print(name, pwd)
    return render(request, "main.html")
