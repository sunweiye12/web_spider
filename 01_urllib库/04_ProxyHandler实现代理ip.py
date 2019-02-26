#encoding: utf-8

from urllib import request

# 没有使用代理的
url = 'http://httpbin.org/ip'               # 这是一个网站可以打印你当前计算机的外网对应的ip地址
resp = request.urlopen(url)
print(resp.read())

# 使用代理的
url = 'http://httpbin.org/ip'
# 1. 使用ProxyHandler，传入代理构建一个handler  ---> 传入字典形式的参数  (key=网站的请求方式(http/https) value=(代理ip:此ip对应端口号)  )
handler = request.ProxyHandler({"http":"42.55.94.226:1133"})
# 2. 使用上面创建的handler构建一个opener
opener = request.build_opener(handler)
# 3. 使用opener去发送一个请求
resp = opener.open(url)
print(resp.read())