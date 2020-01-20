# -*- coding: utf-8 -*-

BOT_NAME = 'fictiontodb'

SPIDER_MODULES = ['fictiontodb.spiders']
NEWSPIDER_MODULE = 'fictiontodb.spiders'
ROBOTSTXT_OBEY = False

## add
ITEM_PIPELINES = {'fictiontodb.pipelines.RuDaoZhiShengPipeline':100}
#Mysql数据库的配置信息
MYSQL_HOST = 'localhost'
MYSQL_DBNAME = 'scrapy_data'
MYSQL_USER = 'root'
MYSQL_PASSWD = '123456'
MYSQL_PORT = 3306

