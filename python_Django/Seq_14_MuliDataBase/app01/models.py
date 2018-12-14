from django.db import models


class Users(models.Model):
    name = models.CharField(max_length=50)
    passwd = models.CharField(max_length=100)

    def __str__(self):
        return "app01 %s " % self.name

    class Meta:
        app_label = "app01"
