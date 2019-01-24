# encoding=utf-8
import urllib2

try:
    # 访问一个不存在的网址
    request = urllib2.Request('http://www.ifengw2323.com')
    urllib2.urlopen(request)
except urllib2.URLError, e:
    print e.reason
