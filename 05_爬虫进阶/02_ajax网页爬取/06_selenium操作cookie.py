#encoding: utf-8

from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
import time

driver_path = r"E:\chromedriver\chromedriver.exe"
driver = webdriver.Chrome(executable_path=driver_path)
driver.get('https://www.baidu.com/')


# get_cookies()  # 获取所有的cookie信息
for cookie in driver.get_cookies():
    print(cookie)

print('='*30)
print(driver.get_cookie("PSTM"))        # 获取name属性为"PSTM"的cookie
driver.delete_cookie("PSTM")            # 删除name属性为"PSTM"的cookie
print('='*30)
print(driver.get_cookie('PSTM'))
# driver.delete_all_cookies()             # 删除所有的cookie信息