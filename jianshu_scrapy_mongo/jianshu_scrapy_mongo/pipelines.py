# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html

from twisted.enterprise import adbapi
#　换成mongodb 之后　不需要mysql的东西了
#import MySQLdb
#import MySQLdb.cursors
import pymongo
from pymongo import MongoClient
from scrapy.crawler import Settings as settings
from items import JianshuScrapyMongoItem
from items import relationItem

class JianshuScrapyMongoPipeline(object):
    def __init__(self):
        self.col_user=MongoClient('localhost',27017).jianshu_scrapy.jianshu_user

    def process_item(self, item, spider):
        if isinstance(item,JianshuScrapyMongoItem):
            doc={
                "uid" : item['uid'],
                "nickname" : item['nickname'],
                "head_pic" : item['head_pic'],
                "gender" : "todo",
                "following_num" : item['following_num'],
                "follower_num" : item['follower_num'],
                "follower_uid" : [],
                "articles_num" : item['articles_num'],
                "words_num" : item['words_num'],
                "beliked_num" : item['beliked_num'],
            }
            self.col_user.insert(doc)
            return item
        if isinstance(item,relationItem):
            post1={"uid" : item['uid']}
            post2={'$addToSet':{'follower_uid':item['follower']}}
            self.col_user.update(post1,post2)
            return item
