# coding=utf-8
# 会话是一个全局的变量
import requests

s = requests.Session()
s.headers.update({'x-test': 'true', 'x-test3': 'true'})
r = s.get('http://httpbin.org/headers', headers={'x-test2': 'true'})
print(r.text)
print('######################################')
# 因为 x-test 在会话中已存在，再设值，会覆盖前面的 x-test
r = s.get('http://httpbin.org/headers', headers={'x-test': 'false'})
print(r.text)
print('######################################')
# 如果不想要全局配置中的一个变量，设置为 None 即可
r = s.get('http://httpbin.org/headers', headers={'x-test': None})
print(r.text)
