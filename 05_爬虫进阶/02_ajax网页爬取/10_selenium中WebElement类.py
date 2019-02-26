#encoding: utf-8

from selenium import webdriver
from selenium.webdriver.remote.webelement import WebElement

driver_path = r"E:\chromedriver\chromedriver.exe"
driver = webdriver.Chrome(executable_path=driver_path)
driver.get('https://www.baidu.com/')


submitBtn = driver.find_element_by_id('su')
print(type(submitBtn))              # 返回的是一个WebElement对象
print(submitBtn.get_attribute("value"))     # 获取标签的value
driver.save_screenshot('baidu.png')        # 保存截图