# encoding=utf8
# 在西刺网站上爬取前100页的ip地址，并存入并存入文件
import urllib2
import BeautifulSoup
import sys

reload(sys)
sys.setdefaultencoding('utf8')
User_Agent = 'Mozilla/5.0 (Windows NT 6.3; WOW64; rv:43.0) Gecko/20100101 Firefox/43.0'
headers = {}
headers['User-Agent'] = User_Agent
n = 1;
f = open("Seq_06_xici_ip.txt", "a")
while n <= 100:
    url = "http://www.xicidaili.com/nn/" + str(n)
    req = urllib2.Request(url, headers=headers)
    html = urllib2.urlopen(req).read()
    # print(html)
    soup = BeautifulSoup.BeautifulSoup(html)
    trs = soup.findAll("tr")
    for x in range(1, len(trs)):
        tds = trs[x].findAll("td")
        print("第" + str(n) + "页数据,第" + str(x) + "条数据")
        print(tds[1].contents[0], tds[2].contents[0])
        text = tds[1].contents[0] + "\t" + tds[2].contents[0] + "\n"
        f.write(text)
    print("#####")
    n = n + 1
