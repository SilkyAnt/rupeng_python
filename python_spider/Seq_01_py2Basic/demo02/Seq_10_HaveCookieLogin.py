# 模拟登录，并保存cookie信息存入cookie.txt
# encoding=utf-8
import cookielib
import urllib2
import urllib

# 设置保存cookie的文件，同级目录下的cookie.txt
filename = 'cookie.txt'
# 声明一个MozillaCookieJar对象实例来保存cookie，之后写入文件
cookie = cookielib.MozillaCookieJar(filename)
# 利用urllib2库的HTTPCookieProcessor对象来创建cookie处理器
handler = urllib2.HTTPCookieProcessor(cookie)
# 通过handler来构建opener
opener = urllib2.build_opener(handler)
data = {"username": "admin", "userpwd": "123456"}
data2 = urllib.urlencode(data)
# 创建一个请求，原理同urllib2的urlopen
response = opener.open("http://127.0.0.1:8000/admin?" + data2)
print opener
# 保存cookie到文件
cookie.save(ignore_discard=True, ignore_expires=True)
print response.read()

# 创建MozillaCookieJar实例对象
cookie2 = cookielib.MozillaCookieJar()
# 从文件中读取cookie内容到变量
cookie2.load('cookie.txt', ignore_discard=True, ignore_expires=True)
# 第二步：读取cookie.txt, 然后访问http: // localhost:8000 / toAdmin
# encoding=utf-8
import cookielib
import urllib2
import urllib

# 创建MozillaCookieJar实例对象
cookie2 = cookielib.MozillaCookieJar()
# 从文件中读取cookie内容到变量
cookie2.load('cookie.txt', ignore_discard=True, ignore_expires=True)
print cookie2
# 创建请求的request
req = urllib2.Request("http://127.0.0.1:8000/toAdmin")
opener2 = urllib2.build_opener(urllib2.HTTPCookieProcessor(cookie2))
# 请求访问
response2 = opener2.open(req)
print response2.read()
