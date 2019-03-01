# 第一步：导入模块
from xml.dom.minidom import *

# 第二步：载入要解析的文档
xmldoc = parse("student.xml")
# 第三步：获取根节点
root = xmldoc.documentElement
# 第四步：根节点下的student子节点
stunodes = root.getElementsByTagName("student")
for s in stunodes:
    print(s.hasAttribute("sid"), s.getAttribute("sid"))
