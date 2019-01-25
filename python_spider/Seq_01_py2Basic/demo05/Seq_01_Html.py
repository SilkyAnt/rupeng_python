# coding=utf-8
from bs4 import BeautifulSoup

# 我们创建一个字符串，后面的例子我们便会用它来演示
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
# 通过访问字符串的形式解析页面内容
# 四大解释器参考链接：https://cuiqingcai.com/1319.html
# soup=BeautifulSoup(html,"html5lib")
soup = BeautifulSoup(html, "lxml")
# soup=BeautifulSoup(html,"html.parser")
# soup = BeautifulSoup(html, ["lxml", "xml"])
# 格式化输出
print soup.prettify()
