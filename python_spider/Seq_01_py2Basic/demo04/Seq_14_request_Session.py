# coding=utf-8
# 使用Session的时候
import requests

s = requests.Session()
# 设置 cookies
s.get('http://httpbin.org/cookies/set/sessioncookie/123456789')
# 获得 cookies
r = s.get("http://httpbin.org/cookies")
print(r.text)
