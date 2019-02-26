#encoding: utf-8

from urllib import request,parse
'''
request为了增加请求部分的内容
可以用来设置请求头
    有一些网站是设置了反爬虫机制,如果没有请求头信息,就无法获取到有价值的网页,因此设置请求头是有必要的
'''
# 没有请求头去访问拉勾网关于python的信息
# url = 'https://www.lagou.com/jobs/list_python?labelWords=&fromSearch=true&suginput='
# resp = request.urlopen(url)
# print(resp.read())


url = 'https://www.lagou.com/jobs/positionAjax.json?city=%E6%B7%B1%E5%9C%B3&needAddtionalResult=false&isSchoolJob=0'

'''有一些网站设置反爬虫机制,原理是基于有些网页是从上一个网页跳到此网页中的,所以他访问到此网页的时候会检查一下
    上个网页的地址是不是实际地址,所以设置headers 中的 Referer参数是有必要的
'''
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/62.0.3202.94 Safari/537.36',
    'Referer': 'https://www.lagou.com/jobs/list_python?labelWords=&fromSearch=true&suginput='
}
# 有必要设置一下data
data = {
    'first': 'true',
    'pn': 1,
    'kd': 'python'
}

req = request.Request(url,headers=headers,data=parse.urlencode(data).encode('utf-8'),method='POST')
resp = request.urlopen(req)
print(resp.read().decode('utf-8'))  #将读取的源码网页解码为utf-8格式