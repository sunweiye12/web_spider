#encoding: utf-8

import requests

response = requests.get("https://www.baidu.com/")
# (自动解码)查看相应内容,返回的数unicode编码格式的信息ISO-8859-1 --->  要想其转换成中文显示,向用ISO-8859-1转换成字节流.灾后用utf-8转换成字符串
print(type(response.text))
print(response.text)

# (手动解码)查看相应内容,返回的数字节流编码格式的信息
print(type(response.content))
print(response.content.decode('utf-8'))
#
# # 查看完整的url
# print(response.url)
# # 查看响应头字符编码/
# print(response.encoding)
# # 查看响应吗
# print(response.status_code)

params = {
    'wd': '中国'
}
headers = {
    'User-Agent': 'ozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.84 Safari/537.36'
}

# 参数接受一个字典或字符串的查询参数,字典类型自动转换为url编码,不需要urlencode
response = requests.get("https://www.baidu.com/s",params=params,headers=headers)

with open('99_test//baidu.html','w',encoding='utf-8') as fp:
    fp.write(response.content.decode('utf-8'))
    # write只能传递str格式,因此要先解码(decode),写进去的网页要字节流的格式,所以还要编码(encoding)

print(response.url)