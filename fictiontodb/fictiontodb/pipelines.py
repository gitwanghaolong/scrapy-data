# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html
from fictiontodb.common.db.dbhelper import DBHelper


class FictiontodbPipeline(object):
    def process_item(self, item, spider):
        return item


# 持久化到数据库
class RuDaoZhiShengPipeline(object):
    def __init__(self):
        self.db = DBHelper()

    def process_item(self, item, spider):
        self.db.insert(item)
        return item
