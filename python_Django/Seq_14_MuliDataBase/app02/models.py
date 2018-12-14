from django.db import models


class Users(models.Model):
    username = models.CharField(max_length=100)
    password = models.CharField(max_length=50)
    age = models.IntegerField()

    def __str__(self):
        return "app02 %s" % self.username

    class Meta:
        app_label = "app02"


class Book(models.Model):
    user = models.ForeignKey("Users", on_delete=models.CASCADE)
    bookname = models.CharField(max_length=100)

    def __str__(self):
        return "%s: %s" % (self.user.username, self.bookname)

    class Meta:
        app_label = "app02"
