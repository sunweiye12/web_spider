# -*- coding: utf-8 -*-
import scrapy
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule
from a02_wxapp.items import A02WxappItem
from scrapy.http.response.html import HtmlResponse

class WxappSpiderSpider(CrawlSpider):
    name = 'wxapp_spider'
    allowed_domains = ['wxapp-union.com']
    start_urls = ['http://www.wxapp-union.com/portal.php?mod=list&catid=2&page=1']  # 设置于起始爬取页面

    rules = (   # allow表示在当前页面爬取所有符合规则的地址(正则表达式)
        Rule(LinkExtractor(allow=r'.+mod=list&catid=2&page=\d'),follow=True),     # 列表页面的地址,去掉的回调函数,follow代表是否跟进(在爬取到的页面继续按照规则查找)
        Rule(LinkExtractor(allow=r".+article-.+\.html"),
             callback='parse_detail',follow=False)  # 每项详情的地址,调用函数,如果在页面中检索到符合规则的链接不进行跟进
    )

    def parse_detail(self, response):
        '''回调函数'''
        # 解析网页,提取信息
        title = response.xpath("//h1[@class='ph']/text()").get()    # 获取每一篇文章的开头
        author = response.xpath("//p[@class='authors']/a/text()").get()
        pub_time = response.xpath("//p[@class='authors']/span/text()").get()
        article_content = response.xpath("//td[@id='article_content']//text()").getall()
        content = "".join(article_content).strip()

        # 解析好的信息封装成类
        item = A02WxappItem(title=title, author=author, pub_time=pub_time, content=content)
        # 通过yield关键字将内容传递给pipelines(进行下载)
        yield item