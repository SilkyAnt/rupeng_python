# 如果要执行main方法，一定要设置上下文环境
import os
import django

os.environ['DJANGO_SETTINGS_MODULE'] = 'Seq_05_SQLite.settings'
django.setup()
# 设置上下文环境结束

from app.models import Stu


# 初始化数据的例子
def initData():
    # 第一种方法
    p1 = Stu(id=1, name="czf")
    p1.save()
    # 第二种方法
    p2 = Stu()
    p2.id = 2
    p2.name = "afeng"
    p2.save()
    # 第三种方法 可以检测数据是否重复 效率低
    Stu.objects.get_or_create(id="3", name="张三")
    # 第四种方法
    Stu.objects.create(id="4", name="花花")


if __name__ == "__main__":
    initData()
