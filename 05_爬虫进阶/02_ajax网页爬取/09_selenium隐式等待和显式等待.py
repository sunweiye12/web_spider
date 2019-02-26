#encoding: utf-8

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC    # 导入条件
from selenium.webdriver.support.ui import WebDriverWait

"""
    等待的必要性在于,当你打开页面然后执行获取页面元素或者点击按钮时,
    操作之前要等待元素加载完毕
隐式等待:等待指定的时间(无论期间是否获得)
显示等待:指定最多指定是时间,如果在时间内得到,就不在等待,继续执行
"""
driver_path = r"E:\chromedriver\chromedriver.exe"
driver = webdriver.Chrome(executable_path=driver_path)
driver.get('https://www.douban.com/')

# driver.implicitly_wait(20)      # 隐式等待

# 显示等待
element = WebDriverWait(driver,10).until(
    EC.presence_of_element_located((By.ID,'form_email'))        # 参数放到元组中(目的是为了通过id来获取一个元素)
    # 还有很多条件可以添加
)

# inputTag = driver.find_element_by_id('kwasdasda')
print(element)
