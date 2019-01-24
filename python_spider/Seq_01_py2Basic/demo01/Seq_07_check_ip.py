# encoding=utf-8
# 检测爬取到的代理IP是否可用
# 方法一
import urllib

f = open("Seq_06_xici_ip.txt", mode="r")
f2 = open("Seq_07_canUseIp.txt", mode="a")
lines = f.readlines()
print(len(lines))
proxys = []
# 第一步： 读取Seq_06_xici_ip.txt文件，获取所有的ip+port
for i in range(0, 7):
    # strip() 方法用于移除字符串头尾指定的字符(默认为空格或换行符)或字符序列
    ip = lines[i].strip("\n").split("\t")
    proxy_host = "http://" + ip[0] + ":" + ip[1]
    proxy_temp = {"http": proxy_host}
    proxys.append(proxy_temp)
url = "http://ip.chinaz.com/getip.aspx"
# 第二步：检测ip是否可用
n = 0
for proxy in proxys:
    n = n + 1
    print("第" + str(n) + "条记录")
    print(proxy)
    try:
        res = urllib.urlopen(url, proxies=proxy).read()
        print("OK")
        f2.write(proxy['http'] + "\n")
    except Exception, e:
        print e
        continue

f2.close()
