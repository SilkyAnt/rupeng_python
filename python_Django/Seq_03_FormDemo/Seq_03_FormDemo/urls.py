"""Seq_03_FormDemo URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from django.conf.urls import url
from hello import views as hv
from hello import views2 as hv2

urlpatterns = [
    url("^$", hv.index),
    url("^toadd$", hv.to_add),
    url("^reg$", hv.regsiter),
    url("^reg2$", hv.regsiter2),
    url(r"^add2/(\d+)\+(\d+)$", hv.add, name="add1"),
    url(r"^add3/(\d+)/(\d+)$", hv.addNew),
    url("^content$", hv.content),
    url("^hello$", hv2.HelloView.as_view()),
    path('admin/', admin.site.urls),
]
