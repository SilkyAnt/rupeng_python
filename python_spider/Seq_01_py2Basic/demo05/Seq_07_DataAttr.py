# coding=utf-8
from bs4 import BeautifulSoup

data_soup = BeautifulSoup('<div data-foo="value">foo!</div>', "lxml")
# 错误的写法
# data_soup.find_all(data-foo = "value")
# 正确的写法
alls = data_soup.find_all(attrs={"data-foo": "value"})
for t in alls:
    print(t)
