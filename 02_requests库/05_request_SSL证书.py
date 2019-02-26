#encoding: utf-8
import requests
# 如果有些网站的SSL证书是没有经过认证的话,应该在访问连接的时候加上verify=True,可以不检查SSL证书
resp = requests.get('http://www.12306.cn/mormhweb/',verify=True)
with open('99_test//12306.html','w',encoding='utf-8') as fp:
    fp.write(resp.text)