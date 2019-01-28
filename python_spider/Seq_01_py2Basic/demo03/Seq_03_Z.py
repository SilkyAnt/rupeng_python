# coding=utf-8
import re

# 1、\Z表示匹配字符串的尾部
str = "abc1 abc2 abc3 ew23abc4 dd abc5"
str2 = r"abc5\Z"
pattern = re.compile(str2)
print(re.search(pattern, str).group())
print(re.findall(pattern, str))
