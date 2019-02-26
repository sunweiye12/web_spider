#encoding: utf-8

import requests

data = {
    'first':"true",
    'pn': '1',
    'kd': 'python'
}
headers = {
    'Referer': 'https://www.lagou.com/jobs/list_python?labelWords=&fromSearch=true&suginput=',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.84 Safari/537.36'
}
# data数据不用编码成url的格式,(自动转换)
response = requests.post('https://www.lagou.com/jobs/positionAjax.json?city=%E6%B7%B1%E5%9C%B3&needAddtionalResult=false&isSchoolJob=0',data=data,headers=headers)
# 返回的数据时字符串类型的json数据
print(response.text)
# 将返回是json数据转化为字典或列表
print(type(response.json()))
# print(response.json())