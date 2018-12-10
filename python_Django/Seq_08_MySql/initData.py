import os
import django

os.environ['DJANGO_SETTINGS_MODULE'] = 'Seq_08_MySql.settings'
django.setup()

from hello.models import Stu

s1 = Stu(name="czf", pwd="1")
s1.save()
s2 = Stu(name="jianglp", pwd="1")
s2.save()
