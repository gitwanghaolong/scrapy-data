# -*- coding: utf-8 -*-

import pymysql
from twisted.enterprise import adbapi
from scrapy.utils.project import get_project_settings

class DBHelper():

    def __init__(self):
        settings = get_project_settings()
        dbparams = dict(
            host=settings['MYSQL_HOST'],
            db=settings['MYSQL_DBNAME'],
            user=settings['MYSQL_USER'],
            passwd=settings['MYSQL_PASSWD'],
            charset='utf8',
            cursorclass=pymysql.cursors.DictCursor,
            use_unicode=False,
        )
        #**表示将字典扩展为关键字参数,相当于host=xxx,db=yyy....
        dbpool = adbapi.ConnectionPool('pymysql', **dbparams)
        self.dbpool = dbpool

    def connect(self):
        return self.dbpool

    #插入数据
    def insert(self, item):
        sql =  " INSERT INTO fiction (fiction_name, fiction_title, fiction_url, fiction_content, create_time) " \
               " VALUES (%s,%s,%s,%s,%s) ";
        query = self.dbpool.runInteraction(self._conditional_insert, sql, item)
        #调用异常处理方法
        query.addErrback(self._handle_error)
        return item

    #写入数据库中
    def _conditional_insert(self, canshu, sql, item):
        params = (item['fictionName'], item['fictionTitle'], item['fictionUrl'],item['fictionContent'], item['createTime'])
        canshu.execute(sql, params)

    #错误处理方法
    def _handle_error(self, failue):
        print('--------------database operation exception!!-----------------')
