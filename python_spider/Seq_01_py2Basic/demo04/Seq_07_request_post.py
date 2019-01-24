# coding=utf-8
# 传json数据给服务器
import json
import requests

url = 'http://httpbin.org/post'
payload = {'some': 'data'}
r = requests.post(url, data=json.dumps(payload))
print r.text
