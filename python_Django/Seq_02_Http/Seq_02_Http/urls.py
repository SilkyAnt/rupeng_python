"""Seq_02_Http URL Configuration

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
from Hello import views as hv

urlpatterns = [
    url("^index$", hv.index),
    url("^hello$", hv.hello),
    url("^gotoLoginPage$", hv.gotoLoginPage),
    url("^dealLogin$", hv.dealLogin),
    url("^main$", hv.gotoMainPage),
    url("^session01$", hv.session01),
    url("^login2$", hv.login2),
    url("^dealLogin2$", hv.dealLogin2),
    url("^gotoMainPage2$", hv.gotoMainPage2),
    url("^gotoCountPage$", hv.gotoCountPage),
    path('admin/', admin.site.urls),
]
