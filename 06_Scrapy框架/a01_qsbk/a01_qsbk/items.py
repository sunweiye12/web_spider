# -*- coding: utf-8 -*-

"""
此类的目的是为了约束传递的数据(在将网页数据下载下来的时候)
    当爬虫文件爬取下来数据,要将数据存储到A01QsbkItem对象中
    然后通过yield 关键字传递给pipelines文件进行处理
"""

import scrapy

# 相当于将传递的数据封装成一个类,
class A01QsbkItem(scrapy.Item): # 此处的属性就是传递的字段信息
    '''表名传递的对象只能有这两个属性'''
    author = scrapy.Field() # 固定写法
    content = scrapy.Field()
