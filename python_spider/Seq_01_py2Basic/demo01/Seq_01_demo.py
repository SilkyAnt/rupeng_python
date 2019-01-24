# encoding=utf-8
# python2.7
import urllib2

response = urllib2.urlopen("http://www.rupeng.com").read()
print(response)
