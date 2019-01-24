# coding=utf-8
'''
国外免费代理：
www.gatherproxy.com/zh
国内免费代理:
http://www.xicidaili.com/
'''
import requests

proxies = {
    "http": "http://101.236.18.101:8866",
}
r = requests.post("http://httpbin.org/post", proxies=proxies)
r.encoding = 'gbk'
print(r.text)
