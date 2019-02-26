# encoding: utf-8

from selenium import webdriver
'''
chromedriver下载到本地,并配置path路径,下载的时候版本要和chrome版本对应
selennium模块直接通过pip来添加
'''

driver_path = r"E:\chromedriver\chromedriver.exe"   # chromedriver的地址

driver = webdriver.Chrome(executable_path=driver_path)  # webdriver可以驱动各种浏览器,(前提是将浏览器驱动装到电脑上)

driver.get('https://www.baidu.com/')    # 会自动打开谷歌浏览器,访问此URL

print(driver.page_source)                  # 打印网页源代码