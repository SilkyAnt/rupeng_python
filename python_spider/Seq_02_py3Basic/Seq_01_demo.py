# encoding=utf-8
# python 3.x 用urllib.request代替urllib2
import urllib.request

response = urllib.request.urlopen("http://www.rupeng.com").read()
print(response.decode('utf-8'))
