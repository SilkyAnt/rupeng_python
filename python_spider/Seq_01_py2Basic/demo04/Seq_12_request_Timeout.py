# coding=utf-8
# 可以利用 timeout 变量来配置最大请求时间
# timeout 仅对连接过程有效，与响应体的下载无关
import requests

r = requests.get('http://github.com', timeout=0.001)
print r.text

