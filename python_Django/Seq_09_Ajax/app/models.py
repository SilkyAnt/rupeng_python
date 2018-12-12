from django.db import models


class User(models.Model):
    id = models.IntegerField(primary_key="id")
    name = models.CharField(max_length=20)
    password = models.CharField(max_length=30)

    def __str__(self):
        return self.name + "," + self.password
