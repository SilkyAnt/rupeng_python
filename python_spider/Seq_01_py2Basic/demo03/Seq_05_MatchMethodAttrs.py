# encoding=utf-8
# 导入re模块
import re

# 将正则表达式编译成Pattern对象，注意rupengwang前面的r的意思是“原生字符串”
pattern = re.compile(r'(?P<name>rupengwang)')
# 使用re.match匹配文本，获得匹配结果，无法匹配时将返回None
result2 = re.match(pattern, 'rupengwango CQC!')
print("string", result2.string)
print("pattern", result2.re.pattern)
print("pos", result2.pos)
print("endpos", result2.endpos)
print("lastindex", result2.lastindex)
print("lastgroup", result2.lastgroup)
print("group", result2.group())
print("groups", result2.groups())
print("groupdict", result2.groupdict())
print("start", result2.start())
print("end", result2.end())
print("span", result2.span())
print("template", result2.expand(r'\1'))
