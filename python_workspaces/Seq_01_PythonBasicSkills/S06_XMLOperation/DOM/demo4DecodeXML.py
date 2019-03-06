# 第一步：导入模块
from xml.dom.minidom import *

# 第二步：载入要解析的文档
xmldoc = parse("student.xml")
# 第三步：获取根节点
root = xmldoc.documentElement
# 第四步：根节点下的student子节点
stunodes = root.getElementsByTagName("student")
for s in stunodes:
    # 前提：知道所有子节点的name才能解析
    # 所以不建议使用，更多是使用demo2中的方法
    print(s.hasAttribute("sid"), s.getAttribute("sid"))
    # 第五步：解析student子节点下所有的子节点
    idTag = s.getElementsByTagName("id")
    print("id={}".format(idTag[0].firstChild.data))
    nameTag = s.getElementsByTagName("name")
    print("name={}".format(nameTag[0].firstChild.data))
    sexTag = s.getElementsByTagName("sex")
    print("sex={}".format(sexTag[0].firstChild.data))
    addressTag = s.getElementsByTagName("address")
    print("address={}".format(addressTag[0].firstChild.data))
    ageTag = s.getElementsByTagName("age")
    print("age={}".format(ageTag[0].firstChild.data))
    print()
