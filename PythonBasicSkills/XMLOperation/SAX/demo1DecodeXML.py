#第一步：导入相关的模块
import xml.sax
#第二步：自定义一个studentHandler，使其继承xml.sax.ContentHandler
class studentHandler(xml.sax.ContentHandler):
    def startDocument(self):
        print("开始解析文档")

    def endDocument(self):
        print("结束文档解析")

    def __init__(self):
        print("开始解析：")

    def startElement(self,name,attrs):
        if name == "student":
            print("<{} sid=\"{}\">".format(name,attrs['sid']))
        else:
            print("<{}>" .format(name))

    def endElement(self,name):
        print("</{}>" .format(name))

    def characters(self,content):
        print(content)

#第三步：创建一个新的解析器对象并返回
parser = xml.sax.make_parser()

#第四步：指定解析器的ContentHandler对象
parser.setContentHandler(studentHandler())

#第五步：解析xml文件
parser.parse("student.xml")