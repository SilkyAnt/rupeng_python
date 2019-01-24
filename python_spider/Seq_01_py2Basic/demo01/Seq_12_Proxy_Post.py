# encoding=utf-8
import urllib, urllib2


def use_proxy_to_post(proxy_ip, proxy_port):
    proxy_support = urllib2.ProxyHandler({'http': r'http://' + proxy_ip + ':' + proxy_port})
    opener = urllib2.build_opener(proxy_support, urllib2.HTTPHandler)
    try:
        url = "http://httpbin.org/post"
        # url="http://www.rupeng.com"
        opener.addheaders = [
            # ('Cookie', 'this is cookie'),
            # ('Referer','this is refere'),
            ('User-Agent',
             'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36'),
        ]
        values = {'a': '1', 'b': '2'}
        data = urllib.urlencode(values)
        response = opener.open(url, timeout=50, data=data)
        html = response.read()
        print html
    except urllib2.HTTPError, e:
        print('UseProxyToPost:', proxy_ip, ' HTTPError:', e)
    except urllib2.URLError as e:
        print('UseProxyToPost:', proxy_ip, ' URLError:', e)
    except Exception as e:
        print('UseProxyToPost:', proxy_ip, ' Exception:', e)


use_proxy_to_post("58.55.139.19", "9999")
