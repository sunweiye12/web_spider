#encoding: utf-8


import requests

proxy = {
    'http': '118.187.58.34:53281'
}
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.84 Safari/537.36'
}
response = requests.get("http://httpbin.org/ip",proxies=proxy,headers=headers)
print(response.text)