"""Seq_18_Blog URL Configuration

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
from blog import views as bv
from django.contrib.auth import views as auth_view

urlpatterns = [
    url('^$', bv.getAllBlog),

    url('^blogs/(?P<pk>[0-9]+)$', bv.blog_detail, name="blog_detail"),
    # url('^first$',bv.first),
    # url('^last$',bv.last),
    url('^page$', bv.page),
    path('admin/', admin.site.urls),
    url('add_blog', bv.add_blog, name="addblog"),
    url('^blog/(?P<pk>[0-9]+)/edit$', bv.blog_edit, name="blog_edit"),
    url('^drafts$', bv.draft_list, name="drafts"),
    url('^blog/(?P<pk>[0-9]+)/publish/$', bv.publish, name="publish"),
    url('^blog/(?P<pk>[0-9]+)/delete/$', bv.remove, name="deleteBlog"),
    url('^blog/(?P<pk>[0-9]+)/setNone/$', bv.setpublishDateNone, name="setNone"),
    url('^accounts/login/$', auth_view.auth_login, name="auth_login"),
    url('^accounts/logout/$', auth_view.auth_logout, {'next_page': '/'}, name="auth_logout"),
    url('startSearch', bv.start_search, name="startSearch"),
    url(r'search/', bv.full_text_search),

]
