# coding=utf-8
from bs4 import BeautifulSoup

# 说白了就是select方法的用法
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

# 标签选择器
t = soup.select("title")
a = soup.select("a")

# 通过类名查找
a = soup.select(".sister")
# 通过ID查找
link2 = soup.select("#link2")

# 组合查找
link2 = soup.select("p #link2")
# 直接子标签查找
title = soup.select("head > title")
print(title)
# 属性查找
links = soup.select('a[class="sister"]')

# 以上通过select方法返回的结果都是列表形式，可以遍历形式输出
# 然后通过get_text()方法来获取它的内容
for title in soup.select('title'):
    print title.get_text()
