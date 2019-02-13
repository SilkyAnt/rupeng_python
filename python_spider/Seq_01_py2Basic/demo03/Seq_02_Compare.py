# coding=utf-8
import re

'''
I	IGNORECASE	忽略大小写
M	MULTILINE	多行模式
S	DOTALL	单选模式——点任意匹配模式
L	LOCALE	使预定字符类 \w \W \b \B \s \S 取决于当前区域设定
U	UNICODE	使预定字符类 \w \W \b \B \s \S \d \D 取决于unicode定义的字符属性
X	VERBOSE	详细模式。该模式下正则表达式可以是多行，忽略空白字符
'''

str = "I love love love python"
str2 = r".*(love)+?"
pattern = re.compile(str2)
print(pattern)
print(re.match(str2, str).group())
print(re.search(str2, str).group())
print(re.findall(pattern, str))
