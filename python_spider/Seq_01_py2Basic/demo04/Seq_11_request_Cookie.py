# coding=utf-8
# 向服务器发送cookie
import requests

url = 'http://httpbin.org/cookies'
cookies = dict(cookies_are='working')
r = requests.get(url, cookies=cookies)
print r.text
