# 第一步：导入模块
from xml.dom.minidom import *

# 第二步：载入要解析的文档
xmldoc = parse("student.xml")
# 第三步：获取根节点
root = xmldoc.documentElement
# 第四步：根节点下的student子节点
stunodes = root.getElementsByTagName("student")
for s in stunodes:
    # 第五步：student子节点下所有的子节点
    for c in s.childNodes:
        # 如果是元素节点（去掉换行节点）
        if c.nodeType == 1:
            # print(c.firstChild.data)
            print("{}={:6}".format(c.nodeName, c.firstChild.data), end="")
    print()
