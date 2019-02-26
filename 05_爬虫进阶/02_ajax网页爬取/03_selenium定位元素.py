#encoding: utf-8

from selenium import webdriver
from lxml import etree
from selenium.webdriver.common.by import By

driver_path = r"E:\chromedriver\chromedriver.exe"
driver = webdriver.Chrome(executable_path=driver_path)
driver.get('https://www.baidu.com/')


"""获取百度首页的输入标签"""

# inputTag = driver.find_element_by_id('kw')                            # 通过id来获取
# inputTag = driver.find_element_by_name('wd')                          # 通过name来获取
# inputTag = driver.find_element_by_class_name('s_ipt')                 # 通过name来获取
# inputTag = driver.find_element_by_xpath("//input[@class='s_ipt']")    # 通过xpath来获取
inputTag = driver.find_element_by_css_selector(".quickdelete-wrap > input")     # 通过css选择器来获取

"""另一种方式实现上面操作"""
# inputTag = driver.find_elements(By.CSS_SELECTOR,".quickdelete-wrap > input")[0]
# print(inputTag)

inputTag.send_keys('python')        # 填充字符


"""因为以上操作都是由python写的所以比较慢,实际应用时可以用下面操作"""

# html = etree.HTML(driver.page_source)     # 利用lxml来解析网页源码
# html.xpath("")

"""
1. 如果只是想要解析网页中的数据，那么推荐将网页源代码扔给lxml来解析。因为lxml底层使用的是C语言，所以解析效率会更高。
2. 如果是想要对元素进行一些操作，比如给一个文本框输入值，或者是点击某个按钮，那么就必须使用selenium给我们提供的查找元素的方法。
"""