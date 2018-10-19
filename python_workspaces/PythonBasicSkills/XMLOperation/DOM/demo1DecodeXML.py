#第一步：导入模块
from xml.dom.minidom import *
#第二步：载入要解析的文档
xmldoc = parse("student.xml")
#第三步：获取根节点
root = xmldoc.documentElement
print(root)
print(root.nodeName)
print(root.nodeValue)
print(root.nodeType)
print(len(root.childNodes))
#方法一：根据节点类型，取出所有跟节点下的student节点
stuLists=[]
for node in root.childNodes:
    if node.nodeType==1:
        stuLists.append(node)
print(stuLists)

#方法二：
stunodes = root.getElementsByTagName("student")
print(stunodes)
'''
nodeType是结点的类型，nodeType的12种类型：
const unsigned short ELEMENT_NODE = 1; 元素节点 
const unsigned short ATTRIBUTE_NODE = 2; 属性节点 
const unsigned short TEXT_NODE = 3; 文本节点 
const unsigned short CDATA_SECTION_NODE = 4; CDATA 区段 
const unsigned short ENTITY_REFERENCE_NODE = 5; 实体引用元素 
const unsigned short ENTITY_NODE = 6; 实体 
const unsigned short PROCESSING_INSTRUCTION_NODE = 7; 表示处理指令 
const unsigned short COMMENT_NODE = 8; 注释节点 
const unsigned short DOCUMENT_NODE = 9; 最外层的Root element,包括所有其它节点 
const unsigned short DOCUMENT_TYPE_NODE = 10; <!DOCTYPE………..> 
const unsigned short DOCUMENT_FRAGMENT_NODE = 11; 文档碎片节点 
const unsigned short NOTATION_NODE = 12; DTD 中声明的符号节点
'''