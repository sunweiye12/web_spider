# coding:utf_8

"""
通过利用好selenium模块来实现浏览器是自动搜索数据
利用xpath和正则re来解析文本
通过time模块来放慢搜索的速度模拟人的动作
selenium.webdriver.support import expected_conditions as EC和WebDriverWait模块来实现显示等待
csv模块将文件保存到csv文件中
"""



from selenium import webdriver
from lxml import etree
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
import time
import csv
import pytesseract
from urllib import request
from PIL import Image
import re

KEYWORAD = 'python'     # 填写查询关键字

class BossZhiPin(object):
    '''创建一个爬取boss直聘的爬虫'''
    driver_path = r"E:\chromedriver\chromedriver.exe"   # 获取浏览器驱动
    url = 'https://www.zhipin.com/job_detail/?query={}&scity=100010000&industry=&position=' # 网页链接
    base_url = 'https://www.zhipin.com'
    fp = open('99_test//招聘信息.csv', 'a', newline='', encoding='utf-8')  # 设置要写入scv文件地址
    headers = ['公司', '工作', '工资','地址','职位描述']

    def __init__(self):
        self.driver = webdriver.Chrome(executable_path=BossZhiPin.driver_path)
        self.url = BossZhiPin.url.format(KEYWORAD)
        self.positions = []         # 存放职位信息
        # self.writer = writer
        self.writer = csv.DictWriter(BossZhiPin.fp,BossZhiPin.headers)
        self.writer.writeheader()

    def run(self):
        '''执行爬虫任务'''
        self.driver.get(self.url)  # 打开浏览器进入网站
        while True:
            # 显示等待(等待一段时间)(这里有必要等一下,等到点击下一页的元素加载了之后再往下执行)
            WebDriverWait(driver=self.driver, timeout=10).until(
                EC.presence_of_element_located((By.XPATH, "//div[@class='page']/a[@ka='page-next']"))  # 参数要放到元组中
            )

            source = self.driver.page_source  # driver返回来的源码 -> 包含Ajax返回的内容
            self.parse_list_page(source)      # (调用方法,将本页的源码传递过去)用来解析本页职位列表的地址
            # break       # -------------------------------------------------------------------------设置断点(每页断点)
            """点击下一页进行下一页的解析"""
            next_btn = self.driver.find_element_by_xpath("//div[@class='page']/a[@ka='page-next']")  # 获取下一页的按键
            if "next disabled" in next_btn.get_attribute("class"):  # 如果还存在下一页就点击否则退出
                break
            else:
                next_btn.click()

            # 沉睡一秒进行下一页的解析不容易被封掉
            time.sleep(1)

    def parse_list_page(self,source):
        html = etree.HTML(source)
        links = html.xpath("//div[@class='info-primary']//a[position()=1]/@href")
        for link in links:
            link = BossZhiPin.base_url + link
            self.request_detail_page(link)      # (调用方法)将每一个职位的页面传递过去进行解析
            # 隔一秒解析一个详情页面
            time.sleep(1)
            break       # -------------------------------------------------------------------------设置断点(每个职位详情断点)

    def request_detail_page(self,link):
        '''用来解析每一个职位详情页面'''

        # self.driver.get(url)
        self.driver.execute_script("window.open('%s')"%link)             # 打开另一个窗口
        self.driver.switch_to.window(self.driver.window_handles[1])        # driver地址转换为新打开的页面
        # 显示等待(等待一段时间)(等到详情页面中的元素加载完毕之后再进行解析)
        WebDriverWait(self.driver,timeout=10).until(
            EC.presence_of_element_located((By.XPATH,"//div[@class='recommend-box']")) #xpath不能请求文本,只能是元素
        )
        source = self.driver.page_source    # 获得此网页的源码
        self.parse_detail_page(source)      # (调用方法)通过页面的源代码来提取详情信息

        # 关闭当前这个详情页
        self.driver.close()
        # 继续切换回职位列表页
        self.driver.switch_to.window(self.driver.window_handles[0])

    def parse_detail_page(self,source):
        """ 通过页面的源代码来提取详情信息"""
        html = etree.HTML(source)

        company_name = html.xpath("//div[@class='job-primary detail-box']/div[@class='info-company']/h3/a/text()")[0].strip()
        job_name = html.xpath("//div[@class='job-primary detail-box']/div[@class='info-primary']/div[@class='name']/h1/text()")[0].strip()
        job_range = html.xpath("//div[@class='job-primary detail-box']/div[@class='info-primary']/div[@class='name']/span/text()")[0].strip()
        job_location = html.xpath("//div[@class='detail-content']//div[@class='location-address']/text()")[0].strip()
        job_seclist = html.xpath("//div[@class='detail-content']/div[position()=1]/div[@class='text']/text()")
        job_sec = '\n'.join(job_seclist).strip()    # 获取职位描述的信息

        print(company_name)
        print(job_name)
        print(job_range)
        print(job_location)
        print(job_sec)
        print('*' * 80)
        position = {
            '公司': company_name,
            '工作': job_name,
            '工资': job_range,
            '地址': job_location,
            '职位描述': job_sec
        }
        self.writer.writerow(position)       #将信息写到scv文件中
        self.positions.append(position)


if __name__ == '__main__':

    spider = BossZhiPin()
    spider.run()
