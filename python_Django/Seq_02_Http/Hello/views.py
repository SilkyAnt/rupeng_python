from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader


# Create your views here.
def index(request):
    # response = HttpResponse("Hello,Django")
    # return response

    # 两种访问方式，第一种
    # return render(request, "index.html", {"username": "afeng"})

    # 第二种
    t1 = loader.get_template("index.html")
    context = {"username": "afeng"}
    response = HttpResponse(t1.render(context))

    '''
    # response的常见属性
    print(response.content)
    print(response.charset)
    print(response.status_code)
    print(response.cookies)
    print(response.reason_phrase)
    print(response.streaming)
    print(response.closed)
    '''
    return response


def hello(request):
    response = HttpResponse()
    # response 常见方法
    response.write("Welcome to Django1！")
    response.write("Welcome to Django2！")
    response.writelines(["Welcome to Django3！", "Welcome to Django4！", "Welcome to Django5！"])
    print(response.getvalue())
    print(response.writable())
    response.__setitem__("age", "30")
    print(response.has_header("age"))
    print(response.__getitem__("age"))
    print(response.get("age"))
    response.__delitem__("age")
    response['address'] = "北京"
    print(response.get("address"))
    return response


def gotoLoginPage(request):
    return render(request, "login.html")


def dealLogin(request):
    name = request.GET['username']
    pwd = request.GET['userpwd']
    print(name, pwd)
    if name == 'admin' and pwd == '1':
        # 创建一个 Cookie
        response = render(request, "main.html")
        response.set_signed_cookie("user", name, salt="123", max_age=120)
        # 为了速度更安全，加盐加密
        response.set_cookie("user", name, max_age=120)
        # 删除 Cookie
        # response.delete_cookie("user")
        return response
    else:
        return render(request, "login.html")


def gotoMainPage(request):
    # 读取 Cookie 的值
    admin = request.COOKIES.get("user")
    request.get_signed_cookie("user", salt="123")
    # 遍历所有的 cookie
    # for key in request.COOKIES:
    #     print(key, request.COOKIES.get(key))
    if admin == 'admin':
        return render(request, "main.html")
    else:
        return render(request, "login.html")


def session01(request):
    request.session['user'] = "admin"
    print(request.session.get("user"))
    del request.session['user']
    return render(request, "session_01_index.html")


def login2(request):
    return render(request, "session_02_login.html")


def dealLogin2(request):
    name = request.GET['username']
    pwd = request.GET['userpwd']
    print(name, pwd)
    if name == "admin" and pwd == "1":
        request.session['loginUser'] = "admin"
        request.session.set_expiry(60)
        return render(request, 'session_03_main.html')
    else:
        return render(request, 'session_02_login.html')


def gotoMainPage2(request):
    name = request.session.get('loginUser')
    if name == "admin":
        return render(request, "session_03_main.html")
    else:
        return render(request, "session_02_login.html")


def gotoCountPage(request):
    count = request.session.get("count")
    if count == None:
        request.session['count'] = 1
        return render(request, "session_04_count.html", {"count": 1})
    else:
        count = int(count)
        count += 1
        request.session['count'] = count
        return render(request, "session_04_count.html", {"count": count})
