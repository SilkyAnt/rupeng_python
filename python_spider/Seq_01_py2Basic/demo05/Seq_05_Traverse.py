# coding=utf-8
from bs4 import BeautifulSoup

# 遍历
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
# 遍历直接子节点，把结果放入列表中
print soup.head.contents
print soup.body.contents
print type(soup.body.contents)
print "# " * 10
# 遍历直接子节点，把结果放入迭代器中
print soup.head.children
print soup.body.children
print type(soup.body.children)
for c in soup.head.children:
    print c
for c in soup.body.children:
    print c
print "# " * 10
# 遍历所有子孙节点
print soup.body.descendants
for c in soup.body.descendants:
    print c
print "# " * 10
# 节点内容
print soup.html.string
print soup.head.string
# 标签下的多个子标签以及子孙标签里的内容用 strings
for c in soup.html.strings:
    print c
print "# " * 10
# 去掉结果里面的空值与空行
for s in soup.html.stripped_strings:
    print s

# 父节点
print "# " * 10
p = soup.p
print p.parent.name
content = soup.title.string
print content.parent.name
# 全部父节点
print "# " * 10
content = soup.head.title.string
for parent in content.parents:
    print parent.name
# 兄弟节点 分层次
print "# " * 10
p1 = soup.p
print p1.next_sibling  # 下一个兄弟节点
print p1.next_sibling.next_sibling  # 下下个兄弟节点
print p1.previous_sibling  # 上一个兄弟节点
print "# " * 10
# 全部兄弟节点
for t in p1.next_siblings:
    print t
for t in p1.previous_siblings:
    print t
print "# " * 10
# 全部兄弟节点
for t in p1.next_siblings:
    print t
for t in p1.previous_siblings:
    print t
print "# " * 10
# 上一节点、下一个节点    不分层次
print soup.head.next_element
print soup.b.previous_element
print "# " * 10
# 所有前后节点.next_elements 和 .previous_elements
h = soup.head
for t in h.next_elements:
    print t