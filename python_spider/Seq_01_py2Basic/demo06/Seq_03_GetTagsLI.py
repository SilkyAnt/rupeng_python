# coding=utf-8
from lxml import etree

html = etree.parse('Seq_02_LocalHtml.html')
print type(html)
result = html.xpath("//li")
print result
print len(result)
for l in result:
    # 通过get方法获取属性名对应的属性值
    print l.get("class")
    # 获取所有的属性
    attributes = l.attrib
    # 获取属性名对应的属性值
    print(attributes["class"])
    # 把节点转化为字符串
    print etree.tostring(l)
