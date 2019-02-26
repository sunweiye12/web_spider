'''啦啦啦啦啦啦啦爬虫爬虫爬虫爬虫爬虫爬虫爬虫爬虫爬虫爬虫爬虫爬虫爬虫爬虫爬虫'''

# 在urllib库中导出request模块
from urllib import request
# 利用request去访问一个地址
resp = request.urlopen("http://www.baidu.com")
# 1将地址数据读取出来
# print(resp.read())
# 2读取10个字符
# print(resp.read(10))
# 3读取网页的一行
# print(resp.readline())
# 4将网页一行一行的读取出来
# print(resp.readlines())
# 5获取请求状态码
print(resp.getcode())