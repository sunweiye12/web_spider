#encoding: utf-8

'''
每次通过调用此方法来实现爬虫的开启
'''

from scrapy import cmdline

cmdline.execute('scrapy crawl renren'.split())