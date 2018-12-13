import os, django

os.environ['DJANGO_SETTINGS_MODULE'] = 'Seq_11_Cache.settings'
django.setup()

from app.models import Stu

Stu.objects.get_or_create(id="1", name="czf", age="38")
Stu.objects.get_or_create(id="2", name="afeng", age="34")
