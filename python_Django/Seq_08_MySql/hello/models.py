from django.db import models


# Create your models here.
class Stu(models.Model):
    name = models.CharField(max_length=40)
    pwd = models.CharField(max_length=60)
