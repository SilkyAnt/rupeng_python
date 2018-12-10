from django.db import models


# Create your models here.
class Login(models.Model):
    id = models.IntegerField(primary_key="id")
    name = models.CharField(max_length=30)
    password = models.CharField(max_length=50)

    def __str__(self):
        return str(self.id)


class Animal(models.Model):
    name = models.CharField(max_length=40)
    sounds = models.CharField(max_length=80)

    def speak(self):
        return "the %s says %s " % (self.name, self.sounds)
