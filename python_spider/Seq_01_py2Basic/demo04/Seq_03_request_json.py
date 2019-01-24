# coding=utf-8
# get方法请求json文件
import requests
import json

r = requests.get("http://f.apiplus.net/cqssc.json")
print r.text
print json.dumps(r.json(), ensure_ascii=False)
