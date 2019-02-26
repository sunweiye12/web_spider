# -*- coding: utf-8 -*-
import scrapy
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule


class WxappSpiderSpider(CrawlSpider):
    name = 'wxapp_spider'
    allowed_domains = ['wxapp-union.com']
    start_urls = ['http://www.wxapp-union.com/portal.php?mod=list&catid=2&page=1']  # 设置于起始爬取页面

    rules = (   # allow中包含的是所有符合规则的地址(正则表达式)
        Rule(LinkExtractor(allow=r'.+mod=list&catid=2&page=\d'),  follow=True), # 教程列表页面的地址,去掉的回调函数,follow代表是否跟进
        Rule(LinkExtractor(allow=r'.+article-4909-1\.html'),callback='')                                            # 教程详情的地址
    )

    def parse_item(self, response):
        i = {}
        #i['domain_id'] = response.xpath('//input[@id="sid"]/@value').extract()
        #i['name'] = response.xpath('//div[@id="name"]').extract()
        #i['description'] = response.xpath('//div[@id="description"]').extract()
        return i
