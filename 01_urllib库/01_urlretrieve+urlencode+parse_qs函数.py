#encoding: utf-8
from urllib import request
from urllib import parse

'''urlretrieve函数的用法
    将网页或网络资源下载到本地
'''
# 在网页上下载一个图片
# request.urlretrieve('https://timgsa.baidu.com/timg?image&quality=80&size=b9999_10000&sec=1511283869079&
# di=da3892a20ff8b4d535152e303f0c9ae6&imgtype=0&src=http%3A%2F%2Fi2.17173cdn.com%2F2fhnvk%2FYWxqaGBf%2Fcms3%2FESweDEbleCrnwrx.jpg','luban.jpg')
# 将访问的网页下载到本地(下载的是网页源码)
request.urlretrieve("http://www.baidu.com","baidu.html")

'''urlencode函数的用法
    将传送的给字符串的数据进行编码
'''
# 编辑要传递的字段信息
params = {'name':'张三',"age":18,'greet':'hello world'}
# 通过pares模块的urlencode函数进行编码
result = parse.urlencode(params)
# 打印编码后的结果
print(result)


url = 'http://www.baidu.com/s'      # 编写搜索的网址
params = {"wd":"刘德华"}              # 编写查询字段
qs = parse.urlencode(params)           # 编码字段
#
url = url + "?" + qs                   # 将网址信息和查询字段拼接起来

request.urlretrieve(url,'刘德华.html')  # 通过urlretrieve方法将查询的结果网页下载到本地
# --  --  -->打开网页并,在本地打印
# resp = request.urlopen(url)
# print(resp.read())


# parse_qs函数的用法
params = {'name':'张三',"age":18,'greet':'hello world'}
qs = parse.urlencode(params)        # 编码字段
print(qs)
result = parse.parse_qs(qs)         # 解码字段
print(result)

