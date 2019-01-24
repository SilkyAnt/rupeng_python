# encoding = utf-8
import urllib2

req = urllib2.Request('http://my.csdn.net/my/score')
try:
    urllib2.urlopen(req)
except urllib2.URLError, e:
    if hasattr(e, "reason"):
        print e.reason
else:
    print "OK"
