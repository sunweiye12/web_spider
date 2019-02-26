# encoding: utf-8

import time
from selenium import webdriver
from selenium.webdriver.support.ui import Select

"""常见的表单元素"""
# input type='text/password/email/number'
# buttton、input[type='submit']
# checkbox：input='checkbox'     点击按钮(例如:记住我)
# select：                       下拉选择列表

"""操作输入框"""
'''
driver_path = r"E:\chromedriver\chromedriver.exe"
driver = webdriver.Chrome(executable_path=driver_path)
driver.get('https://www.baidu.com/')
inputTag = driver.find_element_by_id('kw')  # 获取输入框
inputTag.send_keys('python')        # 在输入框输入字符
time.sleep(3)
inputTag.clear()                    # 清楚输入框内容
'''

"""操作checkbox"""
'''
driver_path = r"E:\chromedriver\chromedriver.exe"
driver = webdriver.Chrome(executable_path=driver_path)
driver.get('https://www.douban.com/')           # 访问豆瓣首页
rememberBtn = driver.find_element_by_name('remember')   # 获取checkbox框标签

rememberBtn.click()                             # 选中checkbox框
time.sleep(3)
rememberBtn.click()                             # 点击两次变成未选中
'''


"""操作select标签"""
'''
driver_path = r"E:\chromedriver\chromedriver.exe"
driver = webdriver.Chrome(executable_path=driver_path)

driver.get('http://www.dobai.cn/')
selectBtn = Select(driver.find_element_by_name('jumpMenu'))     # 选择复选框元素(需要导入Select模块方法)

selectBtn.select_by_index(1)                          # 通过复选框的索引来选择
selectBtn.select_by_value("http://m.95xiu.com/")      # 通过每一个select的value值来选择
selectBtn.select_by_visible_text("95秀客户端")        # 通过显示的文本来选择
selectBtn.deselect_all()                              # 取消所有的选中
'''


"""鼠标点击事件"""
'''
driver_path = r"E:\chromedriver\chromedriver.exe"
driver = webdriver.Chrome(executable_path=driver_path)

driver.get('https://www.baidu.com/')

inputTag = driver.find_element_by_id('kw')
inputTag.send_keys('python')

submitTag = driver.find_element_by_id('su')
submitTag.click()
'''