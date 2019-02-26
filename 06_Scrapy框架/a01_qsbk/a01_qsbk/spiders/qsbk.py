# -*- coding: utf-8 -*-
"""爬取糗事百科网站 第一个爬虫,将爬去的信息存放到json文件中"""
import scrapy
from a01_qsbk.items import A01QsbkItem


class QsbkSpider(scrapy.Spider):
    name = 'qsbk'                                     # 爬虫名字
    allowed_domains = ['qiushibaike.com']           # 允许爬取的域名
    start_urls = ['https://www.qiushibaike.com/text/page/1/']           # 开始的url
    base_domain = 'https://www.qiushibaike.com'

    # 在此方法中解析网页内容
    def parse(self, response):      # 在response中存放着访问start_urls得到的网页源码
        # contentLeft = response.xpath("//div[@id ='content-left']")
        # print("="*80)
        # print(type(contentLeft))            # SelectorList类型
        # print("="*80)

        duanzidivs = response.xpath("//div[@id ='content-left']/div")       # 通过xpath解析网页获取到所有段子

        for duanzidiv in duanzidivs:
            author = duanzidiv.xpath(".//h2/text()").get().strip()
            content = duanzidiv.xpath(".//div[@class='content']//text()").getall()
            content = "".join(content).strip()

            # 利用约束对象将数据封装成类传递给pipelines,进行数据的处理(存储)
            item = A01QsbkItem(author=author, content=content)
            # 通过yield关键字将内容传递给pipelines
            yield item


        # ****爬取下一页的标签****
        next_url = response.xpath("//ul[@class='pagination']/li[last()]/a/@href").get()   # 获取页面中点击下一页的标签
        if not next_url:
            return         # 如果找不到下一页的标签说明爬取截止,因此结束方法
        else:
            # scrapy.Request方法(第一个参数是url 第二个参数是执行的方法)
            yield scrapy.Request(self.base_domain + next_url, callback=self.parse)  # 返回新地址重新执行此类中的parse()方法