# 如果要执行main方法，一定要设置上下文环境
import os
import django

os.environ['DJANGO_SETTINGS_MODULE'] = 'Seq_07_MyView.settings'
django.setup()
# 设置上下文环境结束


from hello.models import Login

Login.objects.get_or_create(id=1, name="fdas", password="1")
Login.objects.get_or_create(id=2, name="aaa", password="1")
Login.objects.get_or_create(id=3, name="bbbb", password="1")
