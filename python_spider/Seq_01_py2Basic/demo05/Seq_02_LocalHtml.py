# coding=utf-8
from bs4 import BeautifulSoup

# 通过打开文件的形式读取内容
soup = BeautifulSoup(open('Seq_02_LocalHtml.html'))
# 格式化输出
print soup.prettify()
