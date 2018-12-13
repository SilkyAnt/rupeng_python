from django.shortcuts import render
from app.models import Stu
from django.views.decorators.cache import cache_page


# 设置缓存为一分钟
@cache_page(60 * 1)
def getStu(request):
    stu = Stu.objects.get(id=2)
    print(stu)
    return render(request, "Seq_01_Stu.html", {"stu": stu})
