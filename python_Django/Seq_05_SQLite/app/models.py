from django.db import models


class Stu(models.Model):
    id = models.IntegerField(primary_key=id)
    name = models.CharField(max_length=50)

    def __str__(self):
        return str(self.id) + " " + self.name
