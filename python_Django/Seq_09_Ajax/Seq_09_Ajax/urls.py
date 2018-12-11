"""Seq_09_Ajax URL Configuration

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
from app import views as hv

urlpatterns = [
    url('^$', hv.index),
    url('^01$', hv.goPage01),
    url('^ajax1$', hv.ajaxDemo1),
    url('^02$', hv.goPage02),
    url('^ajax2$', hv.ajaxDemo2),
    url('^03$', hv.goPage03),
    path('admin/', admin.site.urls),
]
