# encoding=utf-8
# 常规方法实现
# -*- coding=utf-8 -*-
import time
import Queue
from lxml import etree
import requests


class DouBanSpider():
    def __init__(self, url, q):
        self.url = url
        self.q = q
        self.headers = {
            'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8',
            'Host': 'movie.douban.com',
            'Cookie': 'll="108288"; bid=bhvtbmAkRLQ; __yadk_uid=H6jfIntvlnYMjon2sxWD1kdmWmcts69X; _vwo_uuid_v2=D652B95809735047444880272C0445BFD|c4e27b2ddf29c5a0c0e49dfc1f4bc7eb; __utmc=30149280; __utmc=223695111; ps=y; dbcl2="169309213:k1nb+a+fLqM"; ck=pIxu; _pk_ref.100001.4cf6=%5B%22%22%2C%22%22%2C1531363222%2C%22https%3A%2F%2Faccounts.douban.com%2Flogin%3Fredir%3Dhttps%3A%2F%2Fmovie.douban.com%2Ftop250%3Fstart%3D25%26source%3DNone%26login_type%3Dsms%22%5D; _pk_ses.100001.4cf6=*; __utma=30149280.228920766.1531190370.1531358360.1531363222.3; __utmb=30149280.0.10.1531363222; __utmz=30149280.1531363222.3.2.utmcsr=accounts.douban.com|utmccn=(referral)|utmcmd=referral|utmcct=/login; __utma=223695111.1625218182.1531190370.1531358360.1531363222.3; __utmb=223695111.0.10.1531363222; __utmz=223695111.1531363222.3.2.utmcsr=accounts.douban.com|utmccn=(referral)|utmcmd=referral|utmcct=/login; push_noty_num=0; push_doumail_num=0',
            'Upgrade-Insecure-Requests': '1',
            'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.132 Safari/537.36'
        }

    def parse_page(self):
        '''
                解析网站源码，并采用ｘｐａｔｈ提取　电影名称和平分放到队列中
                :return:
                '''
        response = self.send_request(self.url)
        html = etree.HTML(response)
        # 　获取到一页的电影数据
        node_list = html.xpath("//div[@class='item']")
        for move in node_list:
            # 电影名称
            title = move.xpath('.//a/span/text()')[0]
            # 评分
            score = move.xpath('.//div[@class="bd"]//span[@class="rating_num"]/text()')[0]
            # 将每一部电影的名称跟评分加入到队列
            self.q.put(score + "\t" + title)

    def send_request(self, url):
        '''
        用来发送请求的方法
        :return: 返回网页源码
        '''
        # 请求出错时，重复请求３次,
        i = 0
        while i <= 3:
            try:
                print u"[INFO]请求url:" + url
                return requests.get(url=url, headers=self.headers).content
            except Exception as e:
                print u'[INFO] %s%s' % (e, url)
                i += 1


def main():
    q = Queue.Queue()
    base_url = 'https://movie.douban.com/top250?start='
    # 构造所有ｕｒｌ
    url_list = [base_url + str(num) for num in range(0, 225 + 1, 25)]
    for url in url_list:
        d = DouBanSpider(url, q)
        d.parse_page()
    while not q.empty():
        print q.get()


if __name__ == "__main__":
    start = time.time()
    main()
    print '[info]耗时：%s' % (time.time() - start)
