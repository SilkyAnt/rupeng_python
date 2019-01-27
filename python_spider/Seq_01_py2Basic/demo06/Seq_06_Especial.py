# encoding=utf-8
from lxml import etree

'''
starts-with：顾名思义，匹配一个属性开始位置的关键字
contains：匹配一个属性值中包含的字符串
text（）：匹配的是显示文本信息，此处也可以用来做定位用
'''

html = etree.parse('Seq_05_LocalHtml.html')
result = html.xpath("//li[starts-with(@class,'item')]")
for l in result:
    print etree.tostring(l)
print("*#" * 20)
result = html.xpath("//li[contains(@class,'1')]")
for l in result:
    print etree.tostring(l)
print("*^" * 20)
result = html.xpath("//a[contains(text(),'first')]")
for l in result:
    print etree.tostring(l)
