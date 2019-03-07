from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone


class Blog(models.Model):
    # 作者，标题，文章内容，创建时间，发布时间等
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    text = models.TextField()
    created_date = models.DateTimeField(default=timezone.now)
    published_date = models.DateTimeField(blank=True, null=True)

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = u'文章'
        verbose_name_plural = u'文章2'
