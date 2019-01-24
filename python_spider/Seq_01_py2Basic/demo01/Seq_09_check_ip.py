# coding=utf-8
# 1、不是一次性的读取整个txt文件，使用迭代器一行一行的读取，防止文件过大，占用太多内存
# 2、封装了检测代理IP的方法
# 3、把有效的地址存入文件，减少运行次数。

import urllib2

# 把ip成功的文件存放到这个文件里
f = open("Seq_09_canUseIp.txt", mode="a")

# 使用迭代器读取文件
class LoadFilesWithIteration(object):
    def __init__(self, path):
        self.path = path

    def __iter__(self):
        for line in open(self.path):
            yield line.split()



# 定义一个方法，检测代理IP是否可用
def check_proxy_is_correct(proxy_ip, proxy_port, url):
    proxy_support = urllib2.ProxyHandler({'http': r'http://' + proxy_ip + ':' + proxy_port})
    opener = urllib2.build_opener(proxy_support, urllib2.HTTPHandler)
    try:
        response = opener.open(url, timeout=3)
        html = response.read()
        f.write(proxy_ip + ":" + proxy_port + "\n")
        print 'ok'
    except urllib2.HTTPError, e:
        print('CheckProxyIsCorrect:', proxy_ip, ' HTTPError:', e)
        return 0
    except urllib2.URLError, e:
        print('CheckProxyIsCorrect:', proxy_ip, ' URLError:', e)
        return 0
    except Exception as e:
        print('CheckProxyIsCorrect:', proxy_ip, ' Exception:', e)
        return 0


n = 0
# 载入ip地址存放的文件
corpus = LoadFilesWithIteration('Seq_05_xici_ip.txt')

for item in corpus:
    n = n + 1
    print("第" + str(n) + "条记录：")
    proxy_host = "http://" + item[0] + ":" + item[1]
    print(proxy_host)
    # 这个url是你想通过代理IP和端口访问的最终目标网址
    url = 'http://httpbin.org/get?a=1&b=2'
    check_proxy_is_correct(item[0], item[1], url)
    # 因为耐心有限，所有我就只检测了20天记录，从中获取可用的记录
    if n==20:
        break
