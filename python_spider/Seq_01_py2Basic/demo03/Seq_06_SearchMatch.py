# coding=utf-8
import re

# search()会扫描整个string查找匹配，match（）只有在0位置匹配成功的话才有返回
# match 与 search 这两种方式当找到一个匹配的,就会停止查找
print(re.match('python', 'pythonaaaaaaaa').group())
print(re.match('python', 'aaaaaapython'))
print(re.search('python', 'aaaaaapython').group())
