# coding=utf-8
# 不使用Session的时候
import requests

requests.get('http://httpbin.org/cookies/set/sessioncookie/123456789')
r = requests.get("http://httpbin.org/cookies")
print(r.text)
