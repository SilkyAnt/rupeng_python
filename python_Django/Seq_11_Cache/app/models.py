from django.db import models


class Stu(models.Model):
    id = models.IntegerField(primary_key="id")
    name = models.CharField(max_length=40)
    age = models.IntegerField()

    def __str__(self):
        return self.name
