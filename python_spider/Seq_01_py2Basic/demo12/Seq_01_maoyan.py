# encoding=utf-8
import sys

reload(sys)
sys.setdefaultencoding('utf-8')
import json
from multiprocessing import Pool
import requests
from requests.exceptions import RequestException
from bs4 import BeautifulSoup


def get_one_page(url):  # 判断页面的请求状态来做异常处理
    headers = {'Accept': '*/*',
               'Accept-Language': 'en-US,en;q=0.8',
               'Cache-Control': 'max-age=0',
               'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/48.0.2564.116 Safari/537.36',
               'Connection': 'keep-alive',
               }
    try:
        response = requests.get(url, headers=headers)
        if response.status_code == 200:  # 200是请求成功
            return response.text
        return None
    except RequestException:
        return None


def parse_one_page(html):
    soup = BeautifulSoup(html, 'lxml')
    items = soup.find_all("dd")
    for item in items:
        name = str(item.select("p.star")[0].string.strip())
        name = name[9:len(name)]

        ialls = item.select("p.score")[0].find_all("i")
        print ialls[0].string + ialls[1].string
        yield {
            '排名：': item.find("i").string,
            '电影：': item.select("p.name")[0].find("a").string,
            '主演：': name,
            '上映时间：': item.select("p.releasetime")[0].string.strip(),
            '评分：': ialls[0].string + ialls[1].string
        }


def write_to_file(content):  # 写入文件“result.txt”中
    with open('result.txt', 'a') as f:
        f.write(content + "\n")
        f.close()


def main(page):
    url = "http://maoyan.com/board/3?offset=%s" % (str(page))  # page 为页码数
    html = get_one_page(url)

    for item in parse_one_page(html):
        # 解决dict的中文乱码问题
        text = json.dumps(item).decode('unicode-escape')
        write_to_file(text)


if __name__ == '__main__':
    pool = Pool()  # 建立进程池
    pool.map(main, (i for i in range(10)))  # 映射到主函数中进行循环
