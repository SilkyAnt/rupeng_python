# coding=utf-8
from bs4 import BeautifulSoup

# bs4 的对象可以归纳为4种：1.Tag  2.NavigableString   3.BeautifulSoup 4.Comment
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
# Tag
print soup.p
print soup.p.name
print soup.p.attrs
print "# " * 10
# 获取单个属性的名字
print soup.p['class']
print soup.p.get('name')
# 修改属性值
soup.p['class'] = 'newClass'
print soup.p.get('class')
print "# " * 10
# NavigableString
# 获取标签的内容
print soup.p.string
print type(soup.p.string)
print "# " * 10
# BeautifulSoup
print soup.name
print soup.attrs
print "# " * 10

print soup.a
print soup.a.string
print type(soup.a.string)
if type(soup.a.string) == 'bs4.element.Comment':
    print soup.a.string
