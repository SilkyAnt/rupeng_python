# 如果要执行main方法，一定要设置上下文环境
import os
import django

os.environ['DJANGO_SETTINGS_MODULE'] = 'Seq_06_Blog.settings'
django.setup()
# 设置上下文环境结束

# 初始化数据
from blog.models import Author, Article, Tag
import random

author_name_list = ['WeiHui', 'Hanhu', 'LiJun', 'LuYao', 'Kehu']
author_address_list = ['北京昌平', '广东珠海', '上海开发区', '浙江杭州', '湖南长沙']
article_title_list = ['Django courses', 'Python courses', 'HTML courses',
                      'AI courses', "big_data courses"]


def init_author():
    """
    name = models.CharField(max_length=90)
    qq = models.CharField(max_length=30)
    addr = models.TextField()
    email = models.EmailField()
    """

    for author_name in author_name_list:
        qq = ""
        for i in range(10):
            # print(random.randrange(9))
            # 随机生成9位数的QQ
            qq = qq + str(random.randrange(9))
        i = random.randrange(4)
        author = Author(name=author_name, addr=author_address_list[i], email=qq + "@qq.com", qq=qq)
        author.save()


def init_article_tag():
    # 随机生成文章
    for article_title in article_title_list:
        # 从文章标题中得到 tag
        tag_name = article_title.split(' ', 1)[0]
        tag, created = Tag.objects.get_or_create(name=tag_name)
        random_author = random.choice(Author.objects.all())
        for i in range(30):
            score = random.randrange(61, 101)
            content = "%s __content" % (article_title)
            title = "%s_%s" % (article_title, str(i))
            author = random_author
            article, created = Article.objects.get_or_create(title=title,
                                                             author=author,
                                                             content=content,
                                                             score=score)
            article.tags.add(tag)


if __name__ == "__main__":
    init_author()
    init_article_tag()
