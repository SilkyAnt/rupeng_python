# coding=utf-8
from lxml import etree

# 利用 parse 方法来读取文件，文件中标签需要闭合
html = etree.parse('Seq_02_LocalHtml.html')
result = etree.tostring(html, pretty_print=True)
print(result)
