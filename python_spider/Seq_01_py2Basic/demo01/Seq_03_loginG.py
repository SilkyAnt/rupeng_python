# encoding=utf-8
# get 方法爬虫登录
# 1.导入模块
import urllib, urllib2

# 2.构建发送给服务器端（爬取网站）的数据
data = {"username": "admin", "userpwd": "123467"}
# 3.格式化数据,便于网络传输：dict对象 -> a=1&b=2
data = urllib.urlencode(data)
geturl = "http://localhost:8080/login?" + data
# 构建请求对象
request = urllib2.Request(geturl)
# 爬取页面
text = urllib2.urlopen(request).read()
print(text)
