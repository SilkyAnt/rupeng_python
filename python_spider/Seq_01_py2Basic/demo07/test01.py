#!/usr/bin/env python
# -*- encoding: utf-8 -*-
# Created on 2018-01-08 20:58:58
# Project: newzhihu

from pyspider.libs.base_handler import *
import pymysql
import random
import re


class Handler(BaseHandler):
    crawl_config = {
        'headers': {
            'User-Agent': 'GoogleBot',
        }
    }

    @every(minutes=24 * 60)
    def on_start(self):
        self.crawl('https://www.zhihu.com/topic/19550517/top-answers', callback=self.index_page, validate_cert=False)

    @config(age=10 * 24 * 60 * 60)
    def index_page(self, response):
        print("index_page")
        for each in response.doc('div[@class="List-item TopicFeedItem"]').items():
            text1 = each.find(
                'button[@class="Button ContentItem-action Button--plain Button--withIcon Button--withLabel"]').text()
            self.comment_counts = re.sub("\D", "", text1)
            print(self.comment_counts)
            self.user = each.find('span[@class="UserLink AuthorInfo-name"]').text()
            print(self.user)
            a = each.find('h2.ContentItem-title a')
            self.title = a.text()
            print(self.title)
            self.crawl(a.attr.href, callback=self.detail_page, validate_cert=False,
                       save={"title": self.title, "user": self.user, "comment_counts": self.comment_counts})

    @config(priority=2)
    def detail_page(self, response):
        print("detail_page")
        self.text2 = "hello"
        for each in response.doc('div[@class="RichContent-inner"]').items():
            self.text2 = each.text()
            print(each.text())
        if self.text2 == "hello":
            for each in response.doc('div[@class="RichText ztext Post-RichText"]').items():
                self.text2 = each.text()
                print(each.text())
        self.add_question(response.save['title'], self.text2, response.save['user'], response.save['comment_counts'])
        print("OK")
        return {
            "title": response.save['title'],
            "text": self.text2,
            "user": response.save['user'],
            "comment_counts": response.save['comment_counts'],
        }

    def add_question(self, title2, content2, user2, comment_count2):
        db = pymysql.connect(host="localhost", user="root", password="root", db="club", charset="utf8")
        print("db", db)
        try:
            cursor = db.cursor()
            # 注意此处字符串的占位符要加双引号"%s"
            sql = 'INSERT INTO question (title,content,user_id,created_date,comment_count) VALUES("%s","%s","%s",now(),"%s")' % (
                title2, content2, user2, comment_count2)
            print(sql)
            cursor.execute(sql)
            print(cursor.lastrowid)
            db.commit()
        except Exception, e:
            print(e)
            db.rollback()
