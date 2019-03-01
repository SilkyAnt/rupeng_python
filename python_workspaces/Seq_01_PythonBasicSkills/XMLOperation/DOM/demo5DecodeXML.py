# 第一步：导入模块
from xml.dom.minidom import *

# 第二步：载入要解析的文档
xmldoc = parse("student.xml")
# 第三步：获取根节点
root = xmldoc.documentElement
# 第四步：根节点下的student子节点
stunodes = root.getElementsByTagName("student")
for s in stunodes:
    print("<student sid={}>".format(s.getAttribute("sid")))
    for c in s.childNodes:
        if c.nodeType == 1:
            print("<{0}>{1}</{0}>".format(c.nodeName, c.firstChild.data, c.nodeName))
    print("</student>")
    print()
