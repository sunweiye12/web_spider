#encoding: utf-8

from selenium import webdriver
import time

driver_path = r"E:\chromedriver\chromedriver.exe"
driver = webdriver.Chrome(executable_path=driver_path)
driver.get('https://www.baidu.com/')

time.sleep(5)

driver.close()  # 关闭当前页面
# driver.quit()   # 退出浏览器