# encoding=utf-8
"""
1、https://www.doutula.com/article/list/?page=6
爬取图片
2、采用request.get爬取
3、BeautifulSoup分析提取页面
4、采取Queue存储图片的地址
5、根据每个系列图片的张数启动对应个数的线程，
每个线程分别同时对队列out_queue中的一个url进行访问，这样就实现了高效率的多线程爬图

# 1、导入相关模块
# 2、定义一个方法get_html(url),根据url获取网页内容
# 3、定义一个def get_img_html(html2):爬取html2上的图片的href，并保存到一个列表中
# 4、定义一个方法，get_img():获取imgUrl_list,并存入队列中，启动线程
# 5、自定义线程
# 6、保存图片
"""
import Queue
import threading

import requests
from bs4 import BeautifulSoup
from lxml import etree

out_queue = Queue.Queue()


# 定义一个方法get_html(url),根据url获取网页内容
def get_html(url):
    header = {
        'user-agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/47.0.2526.80 Safari/537.36 Core/1.47.516.400 QQBrowser/9.4.8186.400'
    }
    response = requests.get(url, headers=header).content
    return response


def get_img_html(html):
    y = []
    soup = BeautifulSoup(html, "lxml")
    alists = soup.find_all("a", class_="list-group-item random_list")
    for a in alists:
        y.append(a.get("href"))
    return y


x = 1


def get_img(i):
    html = get_html(i)
    soup = etree.HTML(html)
    divs = soup.xpath("//div[@class='artile_des']")
    for div in divs:
        imgurl_list = div.xpath('table/tbody/tr/td/a/img/@onerror')
        out_queue.put(div.xpath('table/tbody/tr/td/a/img/@onerror'))
    print out_queue.qsize()


class ThreadDownload(threading.Thread):
    def __init__(self, que, no, url):
        threading.Thread.__init__(self)
        self.que = que
        self.no = no
        self.url = url

    def run(self):
        print(self.no)
        print("run")
        start_html = get_html(self.url)
        b = get_img_html(start_html)
        for i in b:
            get_img(i)
        while not self.que.empty():
            save_img(self.que.get()[0])


x = 1


def save_img(urls):
    global x
    url = urls.split("=")[1][1:-1]
    img_content = requests.get(url).content
    with open('doutu/%s.jpg' % x, mode="wb") as f:
        f.write(img_content)

    x = x + 1


def main():
    # 指定爬取图片网站地址
    start_url = 'https://www.doutula.com/article/list/?page='
    threads = []
    for j in range(0, 2):
        threadid = ThreadDownload(out_queue, j, start_url + str(j))
        threads.append(threadid)
        threadid.start()
    for t in threads:
        t.join()


if __name__ == "__main__":
    main()
