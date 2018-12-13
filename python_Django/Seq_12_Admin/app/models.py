from django.db import models


class Article(models.Model):
    title = models.CharField(u'标题', max_length=256)
    content = models.CharField(u'内容', max_length=200)
    pub_date = models.DateField(u'发表的时间', auto_created=True, editable=True)
    update_time = models.DateField(u'更新时间', auto_now=True, null=True)

    def __str__(self):
        return self.title
