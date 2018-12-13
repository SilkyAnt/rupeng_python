from django.utils.deprecation import MiddlewareMixin


# 中间件一定要继承类MiddlewareMixin
class HelloMiddleWare(MiddlewareMixin):
    def process_request(self, request):
        print("Hello，MiddleWare！")
        return None

    def process_response(self, request, response):
        return response
