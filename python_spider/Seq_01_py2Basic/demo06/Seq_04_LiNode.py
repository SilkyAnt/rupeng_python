# encoding=utf-8
from lxml import etree

# 2、查找li节点下的节点
html = etree.parse('Seq_02_LocalHtml.html')
result = html.xpath("//li/node()")
for l in result:
    print etree.tostring(l)
print("2 " * 10)

# 3、查找li节点下a节点的文本
result = html.xpath("//li/a/node()")
for l in result:
    print l
print("3 " * 10)

# 4、获取 <li> 标签的所有 class
result = html.xpath("//li/@class")
for l in result:
    print l
print("4 " * 10)

# 5、获取 <li> 标签下 href 为 link1.html 的 <a> 标签
result = html.xpath("//li/a[@href='link1.html']")
for l in result:
    print etree.tostring(l)
print("5 " * 10)
