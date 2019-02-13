# coding=utf-8
import re

# 2、\A表示匹配字符串的开始
str = "abc1 abc2 abc3 ew23 abc4dd abc5"
str2 = r"\Aabc\d"
pattern = re.compile(str2)
print(re.search(pattern, str).group())
print(re.findall(pattern, str))
