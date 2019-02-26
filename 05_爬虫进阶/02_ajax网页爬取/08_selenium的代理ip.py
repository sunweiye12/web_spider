#encoding: utf-8

from selenium import webdriver

driver_path = r"E:\chromedriver\chromedriver.exe"

options = webdriver.ChromeOptions()     # 创建一个谷歌浏览器的options对象
options.add_argument("--proxy-server=http://27.24.197.129:9999")

driver = webdriver.Chrome(executable_path=driver_path,chrome_options=options)

driver.get("http://httpbin.org/ip")


