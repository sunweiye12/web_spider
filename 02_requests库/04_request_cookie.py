#encoding: utf-8

import requests

# response = requests.get('https://www.baidu.com/')
# print(response.cookies.get_dict())      # 获取到cookies并转化为字典形式

url = "http://www.renren.com/PLogin.do"
data = {"email":"970138074@qq.com",'password':"pythonspider"}
headers = {
    'User-Agent': "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/62.0.3202.94 Safari/537.36"
}

session = requests.Session()    # 创建一个session会话,将所有信息保存在session中,有他代替requests执行操作

session.post(url,data=data,headers=headers)     # 访问这个网址过后,相应的cookie信息就会被session携带

response = session.get('http://www.renren.com/880151247/profile')  # 访问大鹏主页
with open('99_test//renren.html','w',encoding='utf-8') as fp:
    fp.write(response.text)
