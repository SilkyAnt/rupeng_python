from django.db import models


# Create your models here.
class Author(models.Model):
    name = models.CharField(max_length=90)
    qq = models.CharField(max_length=30)
    addr = models.TextField()
    email = models.EmailField()

    def __str__(self):
        return self.name


class Article(models.Model):
    title = models.CharField(max_length=60)
    content = models.TextField()
    score = models.IntegerField()
    # 一片文章对应一个作者 one to one
    author = models.ForeignKey(Author, on_delete=models.CASCADE)
    # 一片文章可以有多个标签，一个标签可以用在多个文章中 many-to-many
    tags = models.ManyToManyField("Tag")

    def __str__(self):
        return self.title


class Tag(models.Model):
    name = models.CharField(max_length=10)

    def __str__(self):
        return self.name