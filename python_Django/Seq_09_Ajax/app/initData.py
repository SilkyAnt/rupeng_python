import os, django

os.environ['DJANGO_SETTINGS_MODULE'] = 'Seq_09_Ajax.settings'
django.setup()

from app.models import User

'''
u1 = User(id=1, name="afeng1", password="1")
u2 = User(id=2, name="afeng2", password="1")
u3 = User(id=3, name="afeng3", password="1")
u4 = User(id=4, name="afeng4", password="1")

u1.save()
u2.save()
u3.save()
u4.save()
'''

print(User.objects.all())
