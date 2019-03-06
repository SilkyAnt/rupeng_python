import xml.dom.minidom

DomParser = xml.dom.minidom
# 获取要解析的文档
xmldom = DomParser.parse("student.xml")
# 获取要解析的文档的根节点
root = xmldom.documentElement
# 添加一个子节点
childXML = xmldom.createElement("student")
# 把这个节点追加到根节点下
root.appendChild(childXML)
# 把id节点追加到student节点下
childXML.setAttribute("sid", "6")
idNode = xmldom.createElement("id")
idNode.appendChild(xmldom.createTextNode("6"))
childXML.appendChild(idNode)
# 把age节点追加到student节点下
ageNode = xmldom.createElement("age")
ageNode.appendChild(xmldom.createTextNode("16"))
childXML.appendChild(ageNode)
# 把name节点追加到student节点下
nameNode = xmldom.createElement("name")
nameNode.appendChild(xmldom.createTextNode("花海"))
childXML.appendChild(nameNode)
# 把sex节点追加到student节点下
sexNode = xmldom.createElement("sex")
sexNode.appendChild(xmldom.createTextNode("女"))
childXML.appendChild(sexNode)
# 把address节点追加到student节点下
addressNode = xmldom.createElement("address")
addressNode.appendChild(xmldom.createTextNode("北京房山"))
childXML.appendChild(addressNode)
# 把新内容写入文件
fileXML = open("student.xml", "w", encoding="utf-8")
# toprettyxml:toprettyxml()输出美化后的XML文本
fileXML.write(xmldom.toprettyxml())
studentsTags = root.getElementsByTagName("student")
for s in studentsTags:
    # 解析未知子节点
    for nodechild in s.childNodes:
        # 节点类型是元素节点
        if nodechild.nodeType == 1:
            print("<%s>%s</%s>  " % (nodechild.nodeName, nodechild.firstChild.data, nodechild.nodeName))
    print()
