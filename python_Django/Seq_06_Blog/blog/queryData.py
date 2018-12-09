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


if __name__ == "__main__":
    querydata1()
