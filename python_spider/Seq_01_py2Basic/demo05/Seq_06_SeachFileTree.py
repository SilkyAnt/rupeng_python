# coding=utf-8
import re

from bs4 import BeautifulSoup

# 搜索文档树 find_all( name , attrs , recursive , text , **kwargs )
html = """
<html><head><title>The Dormouse's story</title></head>
<body>
<p class="title" name="dromouse"><b>The Dormouse's story</b></p>
<p class="story">Once upon a time there were three little sisters; and their names were
<a href="http://example.com/elsie" class="sister" id="link1"><!-- Elsie --></a>,
<a href="http://example.com/lacie" class="sister" id="link2">Lacie</a> and
<a href="http://example.com/tillie" class="sister" id="link3">Tillie</a>;
and they lived at the bottom of a well.</p>
<p class="story">...</p>
"""

soup = BeautifulSoup(html, "lxml")

# print soup.find_all("a")
# 找到所有的A标签
for a in soup.find_all("a"):
    print(a)
print "# " * 10
# 找到所有包含b字母的标签
for a in soup.find_all(re.compile("^b")):
    print a.name
print "# " * 10
# 找到所有的a和b标签
all = soup.find_all(['a', 'b'])
for t in all:
    print(t)
print "# " * 10
# 找到所有的标签
all = soup.find_all(True)
for t in all:
    print(t.name)
print "# " * 10


# 校验一个标签包含class属性却不包含id属性
def has_class_but_no_id(tag):
    t = tag.has_attr('class') and not tag.has_attr("id")
    print(t)
    return t


print "B " * 10

tags2 = soup.find_all(has_class_but_no_id)
for tag in tags2:
    print(tag)
    print "K " * 10
alls = soup.find_all(id="link1")
for t in alls:
    print(t)
print "# " * 10
alls = soup.find_all(href=re.compile(".com"))
for t in alls:
    print(t)
print "# " * 10
alls = soup.find_all(href=re.compile(".com"), id="link2")
for t in alls:
    print(t)
print "# " * 10
alls = soup.find_all(class_="title")

print "# " * 10
alls = soup.find_all(text="Tillie")
alls = soup.find_all(text=["Tillie", "Lacie"])
alls = soup.find_all(text=re.compile("Dormouse"))

alls = soup.find_all("a", limit=2)
for t in alls:
    print t
