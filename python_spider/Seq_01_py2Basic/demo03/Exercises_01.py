# coding=utf-8

import re

line = '''Cats are smarter than dogs
          Cats2 are smarter2 than dogs2'''
matchObj = re.match(r'(.*) are (.*?) .*', line, re.M | re.I)
if matchObj:
    print "matchObj.group() : ", matchObj.group()
    print "matchObj.group(0) : ", matchObj.group(0)
    print "matchObj.group(1) : ", matchObj.group(1)
    print "matchObj.group(2) : ", matchObj.group(2)
else:
    print "No match!!"

# 1、匹配一行文字中的所有开头的字母内容
s = "i love you not because of who you are, but because of who i am when i am with you"

content = re.findall(r"\b\w", s)
print(content)
print("$ " * 10 + "   1   " + "# " * 10)
# 2、匹配一行文字中的所有开头的数字内容
s = "i love you not because 12sd 34er 56df e4 54434"
content = re.findall(r"\b\d", s)
print(content)
print("$ " * 10 + "   2   " + "# " * 10)
# 3、写一个正则表达式，使其能同时识别下面所有的字符串：
# 'bat', 'bit', 'but', 'hat', 'hit', 'hut‘
s = "'bat', 'bit', 'but', 'hat', 'hit', 'hut"
content = re.findall(r"..t", s)
print(content)
print("$ " * 10 + "   3   " + "# " * 10)
# 4、提取每行中完整的年月日和时间字段
s = """se234 1987-02-09 07:30:00
    1987-02-10 07:25:00"""
content = re.findall(r"\d{4}-\d{2}-\d{2} \d{2}:\d{2}:\d{2}", s, re.M)
print(content)
print("$ " * 10 + "   4   " + "# " * 10)
# 5、将每行中的电子邮件地址替换为你自己的电子邮件地址
s = """693152032@qq.com, werksdf@163.com, sdf@sina.com

    sfjsdf@139.com, soifsdfj@134.com
    pwoeir423@123.com"""
content = re.sub(r"\w+@\w+.com", "my163mail@163.com", s)
print(content)
print("$ " * 10 + "   5   " + "# " * 10)
# 6、使用正则提取出字符串中的单词
s = """i love you not because of who 234 you are, 234 but 3234ser because of who i am when i am with you"""
content = re.findall(r"\b[a-zA-Z]+\b", s)
print(content)
print("$ " * 10 + "   6   " + "# " * 10)
# 7、使用正则表达式匹配合法的邮件地址
s = """xiasd@163.com, sdlfkj@.com sdflkj@180.com solodfdsf@123.com 
 sdlfjxiaori@139.com saldkfj.com oisdfo@.sodf.com.com"""
content = re.findall(r"\w+@\w+.com", s)
print(content)
print(re.__all__)
print(re.__version__)
