# encoding=utf-8
from lxml import etree

# 6、获取 <li> 标签下的所有 <span> 标签
html = etree.parse('Seq_05_LocalHtml.html')
# 错误的写法：//li/span
result = html.xpath("//li//span")
for l in result:
    print(etree.tostring(l))
# 7、获取 <li> 标签下的所有a标签下的class属性值
print("7 " * 10)
result = html.xpath('//li/a//@class')
for l in result:
    print(l)
# 8、获取倒数第二个 <li> 的 <a> 的 href
print("8 " * 10)
result = html.xpath('//li[last()-1]/a/@href')
for l in result:
    print(l)
# 9、获取倒数第三个元素的内容
print("9 " * 10)
result = html.xpath('//li[last()-2]/a')
for l in result:
    print etree.tostring(l)
# 10、获取 class 为 bold 的标签名
print("10 " * 10)
result = html.xpath("//*[@class='bold']")
for l in result:
    print etree.tostring(l)
