# -*- coding: utf-8 -*-
import scrapy
import time
from fictiontodb.items import Fiction
from scrapy import Request


class RudaozhishengSpider(scrapy.Spider):
    name = 'rudaozhisheng'
    allowed_domains = ['www.xbiquge.la']
    start_urls = ['http://www.xbiquge.la/0/119/']
    base_url = 'http://www.xbiquge.la'
    def parse(self, response):
        fictionName = response.xpath('//*[@id="info"]/h1/text()').extract_first()
        fictionTitles = response.xpath('//*[@id="list"]/dl/dd/a')
        for each_fictionTitles in fictionTitles:
            fictionTitle = each_fictionTitles.xpath('./text()').extract()[0]
            fictionUrl = self.base_url + each_fictionTitles.xpath('./@href').extract()[0]
            yield Request(url=fictionUrl, meta={'fictionUrl':fictionUrl,'fictionTitle': fictionTitle, 'fictionName': fictionName},
                                 callback=self.fiction_content_parse)

    def fiction_content_parse(self, response):
        print(response.meta['fictionName']+"---"+response.meta['fictionTitle'])
        fictionContentList = response.xpath('//*[@id="content"]/text()').extract()
        fiction = Fiction()
        fiction['fictionName'] = response.meta['fictionName']
        fiction['fictionTitle'] = response.meta['fictionTitle']
        fiction['fictionUrl'] = response.meta['fictionUrl']
        fiction['fictionContent'] = ''.join(fictionContentList)
        fiction['createTime'] = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
        yield fiction