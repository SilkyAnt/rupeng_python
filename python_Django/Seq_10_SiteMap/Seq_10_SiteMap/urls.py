"""Seq_10_SiteMap URL Configuration

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
from app.models import Login
from django.contrib.sitemaps import GenericSitemap
from django.contrib.sitemaps.views import sitemap
from django.conf.urls import url

sitemaps = {
    'login': GenericSitemap({"queryset": Login.objects.all(),
                             "datetime.date": "name"}, priority=0.6),
}

urlpatterns = [
    url(r'^sitemap\.xml$', sitemap, {"sitemaps": sitemaps},
        name="django.contrib.sitemaps.views.sitemap"),
    path('admin/', admin.site.urls),
]
