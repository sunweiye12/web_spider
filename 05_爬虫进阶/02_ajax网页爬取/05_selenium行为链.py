#encoding: utf-8

from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains

driver_path = r"E:\chromedriver\chromedriver.exe"
driver = webdriver.Chrome(executable_path=driver_path)
driver.get('https://www.baidu.com/')                # 百度的url

inputTag = driver.find_element_by_id('kw')
submitBtn = driver.find_element_by_id('su')

actions = ActionChains(driver)      # 创建行为链条
actions.move_to_element(inputTag)   # 绑定一个元素
actions.send_keys_to_element(inputTag,'python') # 进行此元素的操作
actions.move_to_element(submitBtn)  # 绑定第二个元素
actions.click(submitBtn)            # 进行第二个元素的操作
actions.perform()               # 执行行为链的内容