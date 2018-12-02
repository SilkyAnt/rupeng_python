from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic.base import View


class HelloView(View):
    def get(self, request):
        print("get")
        return render(request, "Seq_07_View2.html")

    def post(self, request):
        print("post")
        name = request.POST['username']
        return HttpResponse(name)
