import xml.dom.minidom
xmldoc = xml.dom.minidom.parse("student.xml")
root = xmldoc.documentElement

'''
#第一种方法
for c in root.childNodes:
    if c.nodeType == 1:
        if c.getAttribute("sid") == "6":
            root.removeChild(c)
            break

fxml = open("student.xml",mode="r+",encoding="utf-8")
fxml.write(xmldoc.toprettyxml())
fxml.close()
'''
#第二种方法
stunodes = root.getElementsByTagName("student")
for s in stunodes:
    if s.getAttribute("sid") == "6":
        root.removeChild(s)
        break

fxml = open("student.xml",mode="r+",encoding="utf-8")
fxml.write(xmldoc.toprettyxml())
fxml.close()


