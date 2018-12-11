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
