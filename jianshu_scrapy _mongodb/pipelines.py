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
from items import JianshuScrapyItem
from items import relationItem 

class JianshuScrapyPipeline(object):
    def __init__(self):
        self.col_user=MongoClient('localhost',27017).jianshu_scrapy.jianshu_user

    def process_item(self, item, spider):
        if isinstance(item,JianshuScrapyItem):
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
            self.update(post1,post2)
            return item

"""
class JianshuScrapyPipeline(object):
    def __init__(self):
        dbargs = dict (
            host ='localhost',
            db='jianshu_scrapy',
            user='root',
            passwd='root',
            charset='utf8',
            cursorclass = MySQLdb.cursors.DictCursor,
            use_unicode = True,
            )
        self.dbpool = adbapi.ConnectionPool('MySQLdb',**dbargs)

    def process_item(self, item, spider):
	if isinstance(item,JianshuScrapyItem):
		res = self.dbpool.runInteraction(self.item_a_insert,item)
		return item
	if isinstance(item,relationItem):
		res = self.dbpool.runInteraction(self.item_b_insert,item)
		return item
	
    
    def item_a_insert(self,conn,item):
        try:
            sql="insert into jianshu_user(uid,nickname,head_pic,gender,following_num,follower_num,articles_num,words_num,beliked_num) values('%s','%s','%s','%s',%d,%d,%d,%d,%d) ;"%(item['uid'],item['nickname'],item['head_pic'],item['gender'],int(item['following_num']),int(item['follower_num']),int(item['articles_num']),int(item['words_num']),int(item['beliked_num']))
            conn.execute(sql)
        except Exception,e:
            print e

    def item_b_insert(self,conn,item):
        try:
            conn.execute('insert into jianshu_user_relation(uid,follower_uid) values (%s,%s)',(item['uid'],item['follower'] ))
	except Exception,e:
            print e
"""