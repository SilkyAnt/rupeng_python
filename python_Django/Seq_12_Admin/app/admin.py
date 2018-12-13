from django.contrib import admin
from app.models import Article


class ArticleAdmin(admin.ModelAdmin):
    # 配置要显示的字段
    list_display = ('title', 'pub_date', 'update_time',)


admin.site.register(Article)
