import xml.dom.minidom

xmldoc = xml.dom.minidom.parse("student.xml")

root = xmldoc.documentElement

StudNodes = root.getElementsByTagName("student")
for s in StudNodes:
    if s.getAttribute("sid") =="4":
        print(s.getElementsByTagName("name")[0].firstChild.data)
        s.getElementsByTagName("name")[0].firstChild.data="hashaki"
        break

fxml = open("student3.xml",mode="w+",encoding="utf-8")
fxml.write(xmldoc.toprettyxml())
fxml.close()