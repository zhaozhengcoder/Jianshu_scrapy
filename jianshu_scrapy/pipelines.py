# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html

from twisted.enterprise import adbapi
import MySQLdb
import MySQLdb.cursors
from scrapy.crawler import Settings as settings
from items import JianshuScrapyItem
from items import relationItem

class JianshuScrapyPipeline(object):
    def __init__(self):
        dbargs = dict (
            host ='localhost',
            db='test3',
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
            conn.execute('insert into jianshu_user(uid,nickname,head_pic,gender,following_num,follower_num,articles_num,words_num,beliked_num) values(%s,%s,%s,%s,%d,%d,%d,%d,%d)', (item['uid'],item['nickname'],item['head_pic'],item['gender'],item['following_num'],item['follower_num'],item['articles_num'],item['words_num'],item['beliked_num']))
        except Exception,e:
            print e

    def item_b_insert(self,conn,item):
        try:
            conn.execute('insert into jianshu_user_relation(uid,follower) values (%s,%s)',(item['uid'],item['follower'] ))
	except Exception,e:
            print e
