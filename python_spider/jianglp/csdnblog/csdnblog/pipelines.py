# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html
import re


class CsdnblogPipeline(object):
    def process_item(self, item, spider):
        data = re.findall("https://blog.csdn.net/(.*?)/article/details/(\d*)", item['url'])

        # 构造文件名
        filename = data[0][0] + '_' + data[0][1] + '.txt'
        text = "标题: " + item['title'] + "\n博文链接: " + item['url'] + "\n发布时间: " \
               + item['releaseTime'] + "\n\n正文: " + item['article']
        fp = open(filename, 'wb')
        fp.write(text.encode("utf-8"))
        fp.close()
        return item
