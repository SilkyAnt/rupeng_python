import os, django

os.environ['DJANGO_SETTINGS_MODULE'] = 'Seq_10_SiteMap.settings'
django.setup()

from app.models import Login

'''
u1 = Login(id=1, name="afeng1", password="1")
u2 = Login(id=2, name="afeng2", password="1")
u3 = Login(id=3, name="afeng3", password="1")
u4 = Login(id=4, name="afeng4", password="1")

u1.save()
u2.save()
u3.save()
u4.save()
'''