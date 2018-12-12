from django.shortcuts import render
import json
from django.http import HttpResponse, JsonResponse


def index(request):
    list1 = ["python", "h5", "Java", "AI", "Web"]
    dict1 = {"apple": "23.45", "pear": "45.67", "peach": "23.12", "banance": "23.67"}
    return render(request, 'index.html', {"list1": json.dumps(list1), "dict1": json.dumps(dict1)})


def goPage01(request):
    return render(request, "Seq_01_Ajax.html")


def ajaxDemo1(request):
    # 查询数据库后的数据
    list1 = ["王军", "刘华", "花花", "成局"]
    return HttpResponse(json.dumps(list1, ensure_ascii=False))


def goPage02(request):
    return render(request, "Seq_02_Ajax.html")


def ajaxDemo2(request):
    # 查询数据库后的数据
    dict1 = {"apple": "23.45", "pear": "45.67", "peach": "23.12", "banance": "23.67"}
    # return HttpResponse(json.dumps(dict1))
    return JsonResponse(dict1, content_type="application/json")


def goPage03(request):
    return render(request, "Seq_03_Ajax.html")


def goPage04(request):
    return render(request, "Seq_04_Ajax.html")


def add(request):
    a = int(request.GET['a'])
    b = int(request.GET['b'])
    return HttpResponse(str(a + b))


def goPage05(request):
    return render(request, "Seq_05_CheckSameName.html")


from app.models import User


def checkSameName(request):
    name = request.GET['name']
    print(name)
    lists = User.objects.filter(name=name)
    if len(lists) >= 1:
        return HttpResponse("1")
    else:
        return HttpResponse("0")
