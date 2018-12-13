from django.shortcuts import render


def login(request):
    return render(request, "Seq_01_login.html")


def deallogin(request):
    print("deallogin")
    name = request.GET['username']
    pwd = request.GET['userpwd']
    if name == 'admin' and pwd == '1':
        request.session["loginkey"] = "OK"
        print(request.session['loginkey'])
        return render(request, "Seq_02_Admin.html")
    else:
        return render(request, "Seq_01_login.html")


def main(request):
    return render(request, "Seq_02_Admin.html")
