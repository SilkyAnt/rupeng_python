# coding=utf-8
# 如果想获取来自服务器的原始套接字响应
# 可以取得 r.raw ,不过需要在初始请求中设置 stream=True
import requests

r = requests.get('https://developer.github.com/v3/activity/events/#list-public-events', stream=True)
print r.raw
print r.raw.read(20)
