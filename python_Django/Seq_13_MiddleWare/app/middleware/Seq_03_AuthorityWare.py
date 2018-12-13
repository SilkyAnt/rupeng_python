from django.http import HttpResponseRedirect
from django.utils.deprecation import MiddlewareMixin


# 中间件一定要继承类MiddlewareMixin
class Seq_03_AuthorityWare(MiddlewareMixin):
    def process_request(self, request):
        print("使用中间件实现权限管理")
        address = ['/favicon.ico', '/login', '/deallogin']
        if request.path in address:
            return None
        else:
            try:
                if request.session['loginkey'] == "OK":
                    return None
                else:
                    return HttpResponseRedirect("/login")
            except Exception as e:
                print(e.message)
                return HttpResponseRedirect("/login")

    def process_response(self, request, response):
        return response
