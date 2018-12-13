from django.utils.deprecation import MiddlewareMixin
from django.conf import settings
from django import http


# 实现通过辨别IP地址来禁止访问
# 中间件一定要继承类MiddlewareMixin
class BlockedIPMiddleWare(MiddlewareMixin):
    def process_request(self, request):
        print(request.META['REMOTE_ADDR'])
        if request.META['REMOTE_ADDR'] in getattr(settings, "BLOCKED_IPS", []):
            return http.HttpResponseForbidden('<h1>Forbidden</h1>')
        return None

    def process_response(self, request, response):
        return response

# getattr()三个参数，第一个是对象，第二个是方法，
# 第三个是可选的一个缺省的返回值。
# 如果第二个参数指定的属性或方法没找到则返回这个缺省值。
