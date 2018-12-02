from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, reverse
from hello.forms import addForms, RegisterForm


# Create your views here.
def index(request):
    return render(request, "Seq_05_Add.html")


def to_add(request):
    if request.method == "GET":
        form = addForms(initial={"a": 10, "b": 30})
        return render(request, "Seq_02_form.html", {"form": form})
    if request.method == "POST":
        form = addForms(request.POST)
        if form.is_valid():
            a = form.cleaned_data["a"]
            b = form.cleaned_data["b"]
            return HttpResponse(str(int(a) + int(b)))
        else:
            return render(request, "Seq_02_form.html", {"form": form})


def regsiter(request):
    if request.method == "GET":
        form = RegisterForm()
        return render(request, "Seq_03_reg.html", {"form": form})
    if request.method == "POST":
        form = RegisterForm(request.POST)
        if form.is_valid():
            print(form.cleaned_data["name"])
            return HttpResponse("OK")
        else:
            return render(request, "Seq_03_reg.html", {"form": form})


def regsiter2(request):
    if request.method == "GET":
        form = RegisterForm()
        return render(request, "Seq_04_REG.html", {"form": form})
    if request.method == "POST":
        form = RegisterForm(request.POST)
        if form.is_valid():
            print(form.cleaned_data["name"])
            return HttpResponse("OK")
        else:
            return render(request, "Seq_04_REG.html", {"form": form})


# 地址映射,name 参数的用法
def add(request, a, b):
    a = int(a)
    b = int(b)
    return HttpResponse(str(a + b))


# 地址映射，反转的方法
def addNew(request, a, b):
    return HttpResponseRedirect(
        reverse("add1", args=(a, b))
    )


# 上下文渲染器
def content(request):
    request.GET = request.GET.copy()
    request.GET['jianglp'] = '蒋林平'
    return render(request, "Seq_06_Content.html")
