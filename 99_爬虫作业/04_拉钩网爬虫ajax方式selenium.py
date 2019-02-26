# encoding: utf-8
"""
通过利用好selenium模块来实现浏览器是自动搜索数据
利用xpath和正则re来解析文本
通过time模块来放慢搜索的速度模拟人的动作
selenium.webdriver.support import expected_conditions as EC和WebDriverWait模块来实现显示等待
"""
from selenium import webdriver
from lxml import etree
import re
import time
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By


class LagouSpider(object):
    """这是一个爬取拉勾网信息的爬虫类"""
    # 定义类属性
    driver_path = r"E:\chromedriver\chromedriver.exe"
    # 定义对象属性
    def __init__(self):
        self.driver = webdriver.Chrome(executable_path=LagouSpider.driver_path)
        self.url = 'https://www.lagou.com/jobs/list_python?labelWords=&fromSearch=true&suginput='
        self.positions = []

    # 爬虫入口
    def run(self):
        self.driver.get(self.url)   # 打开浏览器进入网站
        while True:
            # 显示等待(等待一段时间)(这里有必要等一下,等到下一页的元素加载了之后再往下执行)
            WebDriverWait(driver=self.driver,timeout=10).until(
                EC.presence_of_element_located((By.XPATH,"//div[@class='pager_container']/span[last()]"))  # 参数要放到元组中
            )

            source = self.driver.page_source    # 利用driver返回来的源码包含Ajax返回的内容
            self.parse_list_page(source)    # 用来解析本页职位列表的地址

            """点击下一页进行下一页的解析"""
            next_btn = self.driver.find_element_by_xpath("//div[@class='pager_container']/span[last()]")    # 获取下一页的按键
            if "pager_next_disabled" in next_btn.get_attribute("class"):             # 如果还存在下一页就点击否则退出
                break
            else:
                next_btn.click()

            # 沉睡一秒进行下一页的解析不容易被封掉
            time.sleep(1)

    def parse_list_page(self,source):
        """
        通过页面源码来获取每页职位详情页面地址
        :param source:
        :return:
        """
        html = etree.HTML(source)
        links = html.xpath("//a[@class='position_link']/@href")
        for link in links:
            self.request_detail_page(link)
            # 隔一秒解析一个详情页面
            time.sleep(1)

    def request_detail_page(self,url):
        """
        通过职位详情地址来请求详情页面
        """
        # self.driver.get(url)
        self.driver.execute_script("window.open('%s')"%url)             # 打开另一个窗口
        self.driver.switch_to.window(self.driver.window_handles[1])        # driver地址转换为新打开的页面
        # 显示等待(等待一段时间)(等到详情页面中的元素加载完毕之后再进行解析)
        WebDriverWait(self.driver,timeout=10).until(
            EC.presence_of_element_located((By.XPATH,"//div[@class='job-name']/span[@class='name']")) #xpath不能请求文本,只能是元素
        )
        source = self.driver.page_source
        self.parse_detail_page(source)  # 通过页面的源代码来提取详情信息

        # 关闭当前这个详情页
        self.driver.close()
        # 继续切换回职位列表页
        self.driver.switch_to.window(self.driver.window_handles[0])


    def parse_detail_page(self,source):
        """
        通过页面的源代码来提取详情信息
        :param source:
        :return:
        """
        html = etree.HTML(source)
        position_name = html.xpath("//span[@class='name']/text()")[0]
        job_request_spans = html.xpath("//dd[@class='job_request']//span")
        salary = job_request_spans[0].xpath('.//text()')[0].strip()
        city = job_request_spans[1].xpath(".//text()")[0].strip()
        city = re.sub(r"[\s/]", "", city)
        work_years = job_request_spans[2].xpath(".//text()")[0].strip()
        work_years = re.sub(r"[\s/]", "", work_years)
        education = job_request_spans[3].xpath(".//text()")[0].strip()
        education = re.sub(r"[\s/]", "", education)
        desc = "".join(html.xpath("//dd[@class='job_bt']//text()")).strip()
        company_name = html.xpath("//h2[@class='fl']/text()")[0].strip()
        position = {
            'name': position_name,
            'company_name': company_name,
            'salary': salary,
            'city': city,
            'work_years': work_years,
            'education': education,
            'desc': desc
        }
        self.positions.append(position)
        for i in  position:
            print(i+':'+position[i])
        # print(position)
        print('='*80)

if __name__ == '__main__':
    spider = LagouSpider()
    spider.run()