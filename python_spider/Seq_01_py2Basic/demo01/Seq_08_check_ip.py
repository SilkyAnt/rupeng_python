# encoding=utf-8
# 检测爬取到的代理IP是否可用
# 方法二
import urllib2


def CheckProxyIsCorrect(proxy_ip, proxy_port):
    proxy_support = urllib2.ProxyHandler({'http': r'http://' + proxy_ip + ':' + proxy_port})
    opener = urllib2.build_opener(proxy_support, urllib2.HTTPHandler)
    url = 'http://httpbin.org/ip'
    try:
        response = opener.open(url, timeout=5)
        html = response.read()
        if proxy_ip in html:
            return 1
        else:
            return 0
    except urllib2.HTTPError, e:
        print('CheckProxyIsCorrect:', proxy_ip, ' HTTPError:', e)
        return 0
    except urllib2.URLError, e:
        print('CheckProxyIsCorrect:', proxy_ip, ' URLError:', e)
        return 0
    except Exception as e:
        print('CheckProxyIsCorrect:', proxy_ip, ' Exception:', e)
        return 0
    print("该代理IP地址可以使用！")
    # 'http://101.236.60.52:8866'}


CheckProxyIsCorrect("101.236.60.52", "8866")



