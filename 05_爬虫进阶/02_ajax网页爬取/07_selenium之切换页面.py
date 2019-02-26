#encoding: utf-8

from selenium import webdriver

"""
打开多个页面,切换页面
1.通过JS打开新页面
2.通过driver.switch_to_window(driver.window_handles[1])切换driver所在的页面地址
"""

driver_path = r"E:\chromedriver\chromedriver.exe"
driver = webdriver.Chrome(executable_path=driver_path)

driver.get('https://www.baidu.com/')            # 启动浏览器打开一个页面
# driver.get("https://www.douban.com/")     # 在原来的页面上跳转带豆瓣

driver.execute_script("window.open('https://www.douban.com/')") # 通过JS来打开另一个页面(但是driver的地址没有变还是百度)

print(driver.current_url)   #打印当前驱动的URL

# print(driver.window_handles)      # 展现所有的窗口id
driver.switch_to.window(driver.window_handles[1])   #将driver的地址切换到第二个窗口的URL

print(driver.current_url)   #打印当前驱动的URL

# print(driver.page_source)

# 虽然在窗口中切换到了新的页面。但是driver中还没有切换。
# 如果想要在代码中切换到新的页面，并且做一些爬虫。
# 那么应该使用driver.switch_to_window来切换到指定的窗口
# 从driver.window_handlers中取出具体第几个窗口
# driver.window_handlers是一个列表，里面装的都是窗口句柄。
# 他会按照打开页面的顺序来存储窗口的句柄。