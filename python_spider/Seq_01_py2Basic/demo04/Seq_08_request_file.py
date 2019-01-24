# coding=utf-8
# 上传文件
import requests

url = 'http://httpbin.org/post'
files = {'file': open('Seq_08_file.txt', 'rb')}
r = requests.post(url, files=files)
print r.text
