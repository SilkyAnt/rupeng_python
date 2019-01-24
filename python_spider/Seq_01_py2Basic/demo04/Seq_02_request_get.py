# coding=utf-8
# get方法带参数的基本使用
import requests

payload = {'key1': 'value1', 'key2': 'value2'}
r = requests.get("http://httpbin.org/get", params=payload)
print r.url
print r.text
