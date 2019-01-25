# coding=utf-8
from bs4 import BeautifulSoup

soup = BeautifulSoup(open('Seq_02_LocalHtml.html'))
print soup.prettify()
print soup.title
print soup.h1           # 查找符合内容的第一个标签
