# coding=utf-8
# 获取服务器中的cookie
import requests

url = 'https://www.baidu.com'
r = requests.get(url)
print r.cookies
print r.cookies['BDORZ']
