from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect

from blog.models import Blog


# 文章都检索出来并且按照发布日期逆序排序
def getAllBlog(request):
    lists = Blog.objects.all().order_by("-published_date")
    # lists=enumerate(lists)
    print(lists)
    p = Paginator(lists, 2)
    return render(request, "page.html", {"lists": lists, 'lastPage': p.num_pages})


# 文章详情
from django.shortcuts import get_object_or_404


def blog_detail(request, pk):
    blog = get_object_or_404(Blog, pk=pk)

    return render(request, 'detail.html', {"blog": blog})


# 分页的视图函数

'''
def first(request):
   blogs= Blog.objects.all()
   p=Paginator(blogs,2)
   p1=p.page(1)
   print(p1.object_list)
   return render(request,"page.html",{"lists":p1.object_list,'currentPage':1})
def last(request):
    blogs = Blog.objects.all()
    p = Paginator(blogs, 2)
    print(p.num_pages)
    p1 = p.page(p.num_pages)
    return render(request,"page.html",{"lists":p1.object_list,'currentPage':p.num_pages})

from django.utils.datastructures import  MultiValueDictKeyError
def page(request):
    blogs = Blog.objects.all()
    p = Paginator(blogs, 2)
    try:
       currentPage=int(request.GET['currentPage'])
    except MultiValueDictKeyError:
        currentPage=1
    if currentPage<=0:
        currentPage=1
    if currentPage>=p.num_pages:
        currentPage=p.num_pages
    p1=p.page(currentPage)
    return render(request, "page.html", {"lists": p1.object_list, 'currentPage':currentPage,'lastPage':p.num_pages})
'''
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger


def page(request):
    blogs = Blog.objects.all()
    p = Paginator(blogs, 2)
    currentPage = request.GET['currentPage']
    # lists=None;
    p1 = None
    try:
        # lists=p.page(currentPage)
        p1 = p.page(currentPage)
    except PageNotAnInteger:
        # lists=p.page(1).object_list
        p1 = p.page(1)
    except EmptyPage:
        # lists=p.page(p.num_pages).object_list
        p1 = p.page(p.num_pages)
        print(p1.paginator.num_pages)

    return render(request, "page3.html", {"p": p1})


# 添加一篇文章
from .forms import BlogForm
from django.contrib.auth.models import User
import random


@login_required
def add_blog(request):
    if request.method == 'POST':
        form = BlogForm(request.POST)
        if form.is_valid():
            users = User.objects.all()
            blog = form.save(commit=False)
            blog.author = users[random.randrange(0, len(users))]
            blog.save()
            return redirect("blog_detail", pk=blog.pk)
    form = BlogForm()
    return render(request, 'edit.html', {"form": form})


@login_required
def blog_edit(request, pk):
    blog = get_object_or_404(Blog, pk=pk)
    if request.method == 'POST':
        form = BlogForm(request.POST, instance=blog)
        if form.is_valid():
            blog = form.save(commit=False)
            blog.save()
            return redirect('blog_detail', pk=blog.pk)
    else:
        form = BlogForm(instance=blog)
        return render(request, 'edit.html', {'form': form})


# 草稿箱
def draft_list(request):
    lists = Blog.objects.all().filter(published_date__isnull=True).order_by('-created_date')
    return render(request, 'draft.html', {"drafts": lists})


# 发布
@login_required
def publish(request, pk):
    blog = get_object_or_404(Blog, pk=pk)
    blog.publish()
    return redirect('blog_detail', pk=pk)


# 删除
@login_required
def remove(request, pk):
    blog = get_object_or_404(Blog, pk=pk)
    blog.delete()
    return redirect("/")


@login_required
def setpublishDateNone(request, pk):
    blog = get_object_or_404(Blog, pk=pk)
    blog.published_date = None
    blog.save()
    return redirect('blog_detail', pk=pk)


# 导向搜索页面
def start_search(request):
    return render(request, "startSearch.html")


# 全文检索的视图函数
from haystack.forms import SearchForm


def full_text_search(request):
    keyword = request.GET['q']
    sform = SearchForm(request.GET)
    blogs = sform.search()
    print(blogs.all())
    for t in blogs.all():
        print(t)
    return render(request, 'searchResult.html', {"blogs": blogs.all(), 'list_header': '关键字 \'{}\' '.format(keyword)})
