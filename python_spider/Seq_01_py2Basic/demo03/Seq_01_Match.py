# -*- coding: UTF-8 -*-

import re

'''
re.match(pattern, string, flags)
第一个参数是正则表达式,如果匹配成功，则返回一个Match，否则返回一个None；
第二个参数表示要匹配的字符串；
第三个参数是标致位，用于控制正则表达式的匹配方式，如：是否区分大小写，多行匹配等等。
'''
print(re.match('www', 'www.runoob.com').span())  # 在起始位置匹配
print(re.match('com', 'www.runoob.com'))  # 不在起始位置匹配
print(re.match('com', 'comwww.runcomoob').group())
print(re.match('com', 'Comwww.runcomoob', re.I).group())


'''
group() 返回被 RE 匹配的字符串
start() 返回匹配开始的位置
end() 返回匹配结束的位置
span() 返回一个元组包含匹配 (开始,结束) 的位置
group() 返回re整体匹配的字符串，可以一次输入多个组号，对应组号匹配的字符串。
'''

# 将正则表达式编译成Pattern对象，注意hello前面的r的意思是“原生字符串”
pattern = re.compile(r'hello')

# 使用re.match匹配文本，获得匹配结果，无法匹配时将返回None
result1 = re.match(pattern, 'hello')
result2 = re.match(pattern, 'helloo CQC!')
result3 = re.match(pattern, 'helo CQC!')
result4 = re.match(pattern, 'hello CQC!')

# 如果1匹配成功
if result1:
    # 使用Match获得分组信息
    print result1.group()
else:
    print '1匹配失败！'

# 如果2匹配成功
if result2:
    # 使用Match获得分组信息
    print result2.group()
else:
    print '2匹配失败！'

# 如果3匹配成功
if result3:
    # 使用Match获得分组信息
    print result3.group()
else:
    print '3匹配失败！'

# 如果4匹配成功
if result4:
    # 使用Match获得分组信息
    print result4.group()
else:
    print '4匹配失败！'