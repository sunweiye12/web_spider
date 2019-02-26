# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class A02WxappItem(scrapy.Item):
    # 将传递的对象封装成类
    '''表名传递的对象只能有这两个属性'''
    title = scrapy.Field()  # 固定写法
    author = scrapy.Field()
    pub_time = scrapy.Field()
    content = scrapy.Field()
