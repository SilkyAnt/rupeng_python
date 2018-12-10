from django.shortcuts import render
from django.views.generic.base import View
from django.http import HttpResponse
from hello.models import Login


# Create your views here.
def hello(request):
    return render(request, "index.html")


# 方法一：类视图
class MyViews(View):
    def get(self, request):
        print("get")
        return HttpResponse("get")

    def post(self, request):
        print("post")
        return HttpResponse("post")


def getAllLogin(request):
    lists = Login.objects.all()
    return render(request, "login.html", {"lists": lists})


from django.views.generic.base import TemplateView


# 方法二：基于模板视图
class GetAllLogin(TemplateView):
    template_name = "login.html"

    def get_context_data(self, **kwargs):
        context = super(GetAllLogin, self).get_context_data(**kwargs)
        print(context)
        context['lists'] = Login.objects.all()
        print(context)
        return context
