# 如果要执行main方法，一定要设置上下文环境
import os
import django

os.environ['DJANGO_SETTINGS_MODULE'] = 'Seq_06_Blog.settings'
django.setup()
# 设置上下文环境结束

from blog.models import Article, Author, Tag

tags = Tag.objects.all()
for t in tags:
    print(t.name)

# 一对一
'''
# 会输出10条sql
articles = Article.objects.all()[:10]
for a in articles:
    print(a.author.name)
'''

'''
# 只输出一条sql
articles = Article.objects.all().select_related("author")[:10]
for a in articles:
    print(a.author.name)
'''

# 多对多
# 输出11条sql
articles = Article.objects.all()[:10]
for a in articles:
    print(a.tags.all())

# 只输出两条sql
articles = Article.objects.all().prefetch_related("tags")[:10]
for a in articles:
    print(a)

# 排除不需要的字段
articles = Article.objects.all().defer("content")[:5]
articles = Article.objects.all().only("name")[:5]

# 必须要包含主键
articles = Article.objects.raw("select id,title from blog_article limit 5")