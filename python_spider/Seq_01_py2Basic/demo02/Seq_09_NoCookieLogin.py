# encoding=utf-8
# 模拟登录
import cookielib
import urllib2
import urllib

# 声明一个MozillaCookieJar对象实例来保存cookie
cookie = cookielib.MozillaCookieJar()
# 利用urllib2库的HTTPCookieProcessor对象来创建cookie处理器
handler = urllib2.HTTPCookieProcessor(cookie)
# 通过handler来构建opener
opener = urllib2.build_opener(handler)
data = {"username": "admin", "userpwd": "123456"}
data2 = urllib.urlencode(data)
# 创建一个请求，原理同urllib2的urlopen
response = opener.open("http://127.0.0.1:8000/admin?" + data2)
url = "http://127.0.0.1:8000/toAdmin"
result = opener.open(url)
print(result.read())
