# encoding=utf-8
# 使用代理IP抓取百度的网页内容
import urllib2

headers = {
    'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36'
}
proxy_support = urllib2.ProxyHandler({'http': r'http://119.101.112.213:9999'})
opener = urllib2.build_opener(proxy_support, urllib2.HTTPHandler)
urllib2.install_opener(opener)

req = urllib2.Request("http://www.baidu.com", headers=headers)
response = urllib2.urlopen(req)
print(response.read())