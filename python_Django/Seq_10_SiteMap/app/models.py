from django.db import models


class Login(models.Model):
    id = models.IntegerField(primary_key="id")
    name = models.CharField(max_length=30)
    password = models.CharField(max_length=40)

    # get_absolute_url 这个方法一定要有
    def get_absolute_url(self):
        return "/login/" + self.name

    def __str__(self):
        return self.name + "," + str(self.id)
