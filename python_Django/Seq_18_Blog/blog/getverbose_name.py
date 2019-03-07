import os, django

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "Seq_18_Blog.settings")
django.setup()
from django.apps import apps

modelobj = apps.get_model("blog", "Blog")
print(modelobj)
# 获取元信息的versbose_name
print(modelobj._meta.verbose_name)
# 获取字段的versbose_name
fields = modelobj._meta.fields
for i in range(len(fields)):
    print(fields[i].verbose_name)
