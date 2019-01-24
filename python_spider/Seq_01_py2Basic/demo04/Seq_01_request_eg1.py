# encoding=utf8
# request的简单使用
import requests

r = requests.get('https://www.baidu.com')
print type(r)
print r.status_code
print r.encoding
print r.text
print r.cookies
print r.url

r.encoding = 'utf-8'
print r.text
