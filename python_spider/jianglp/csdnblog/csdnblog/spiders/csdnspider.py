# -*- coding: utf-8 -*-

import scrapy
from csdnblog.items import CsdnblogItem


class CsdnspiderSpider(scrapy.Spider):
    name = 'csdnspider'
    allowed_domains = ['csdn.com']
    start_urls = ['https://blog.csdn.net/oscer2016/article/details/75000148']

    def parse(self, response):
        item = CsdnblogItem()

        # 新版主题博客数据抽取
        item['url'] = response.url
        print(item['url'])
        item['title'] = response.xpath('//h1[@class="title-article"]/text()').extract()[0]
        print(item['title'])
        item['releaseTime'] = response.xpath('//span[@class="time"]/text()').extract()[0]
        print(item['releaseTime'])
        item['readnum'] = response.xpath('//span[@class="read-count"]/text()').extract()[0]
        print(item['readnum'])
        print(response)
        t = response.xpath("//*[@id='content_views']//*/text()").extract()
        text = ""
        try:
            for a in range(0, len(t)):
                text = text + t[a]
            item['article'] = text
        except Exception as e:
            print(e)
        yield item
