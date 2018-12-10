# 如果要执行main方法，一定要设置上下文环境
import os
import django

os.environ['DJANGO_SETTINGS_MODULE'] = 'Seq_06_Blog.settings'
django.setup()
# 设置上下文环境结束

from blog.models import Article, Author, Tag


def querydata1():
    # 查询所有的文章
    print(Article.objects.all())
    # 查看SQL语句
    print(str(Article.objects.all().query))
    # values_list获取元组形式结果
    print(Author.objects.values_list("addr", "email"))
    print(Author.objects.values_list("addr"))
    print(Author.objects.values_list("addr", flat=True))
    # 查询 Hanhu这个人的文章标题
    print(Article.objects.filter(author__name='Hanhu').values_list("title", flat=True))
    # values 获取字典形式的结果
    print(Author.objects.values("addr", "qq"))
    print(Article.objects.filter(author__name='Hanhu').values("title"))
    # 排序
    print(Tag.objects.all().order_by("id"))
    # 条件查询
    print(Tag.objects.all().extra(where=['name=%s'], params=['AI']))
    # 聚合查询
    from django.db.models import Count
    print(Article.objects.all().values('author_id')
          .annotate(count=Count('author_id')).values("author_id", "count"))
    print(Article.objects.all().values('author__name').
          annotate(count=Count('author')).values('author__name', 'count'))
    # 求和
    from django.db.models import Sum
    print(Article.objects.values('author__name').
          annotate(sum_score=Sum('score')).values('author__name', 'sum_score'))

if __name__ == "__main__":
    querydata1()
