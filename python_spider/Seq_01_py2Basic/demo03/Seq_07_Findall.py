# encoding=utf-8
import re

# 搜索string，以列表形式返回全部能匹配的子串
str = "I love love love python"
str2 = r"love"
pattern = re.compile(str2)
print(re.search(str2, str).group())
print(re.findall(pattern, str))
