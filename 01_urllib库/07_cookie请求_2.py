#encoding: utf-8

from urllib import request
from http.cookiejar import MozillaCookieJar
'''
MozillaCookieJar可以将cookie信息保存到本地
ignore_discard=True 包含过期的cookie
'''

# 利用MozillaCookieJar创建爱你一个cookiejar对象并关联文件cookie.txt
cookiejar = MozillaCookieJar('cookie.txt')
# 将关联文件中的cookie信息加载到cookiejar中
cookiejar.load(ignore_discard=True)

# 创建opener对象
handler = request.HTTPCookieProcessor(cookiejar)
opener = request.build_opener(handler)

# 访问网页(携带了cookie信息)
resp = opener.open('http://httpbin.org/cookies')
# resp = opener.open('http://www.baidu.com')

for cookie in cookiejar:
    print(cookie)

# 将cookie中的内容你保存到本地(一般的cookie信息在访问结束后就会过期)
# cookiejar.save()
# 将即将过期的信息也保存到关联文件
cookiejar.save(ignore_discard=True)