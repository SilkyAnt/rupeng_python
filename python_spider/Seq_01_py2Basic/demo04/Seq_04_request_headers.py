# coding=utf-8
# 如果想添加 headers，可以传 headers 参数
import requests

payload = {'key1': 'value1', 'key2': 'value2'}
headers = {'content-type': 'application/json'}
r = requests.get("http://httpbin.org/get", params=payload, headers=headers)
print r.url
print r.headers
