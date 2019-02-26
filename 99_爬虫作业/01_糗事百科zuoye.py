#encoding: utf-8
"""
利用正则表达式来爬取糗事百科第1页到3页的糗事内容
"""
import requests
import re

def parse_page(url):
    headers = {
        'User-Agent': "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/62.0.3202.94 Safari/537.36"
    }
    proxy = {
        'http': '119.101.116.156:9999'
    }
    response = requests.get(url,proxies=proxy,headers=headers)
    text = response.text
    # print(text)                                                               # 打印一下网页源码
    # re.DOTALL：可以让.匹配\n
    authors = re.findall(r'<h2>\n(.*?)\n</h2>',text,re.DOTALL)                  # 搜索所有的糗事作者
    content = re.findall(r'<div\sclass="content">.*?<span.*?>(.*?)</span>',text,re.DOTALL)      # 搜索到所有的糗事文本
    # print(contents)
    # print(authors)

    contents = []
    for cont in content:        # 去除所有诗词内容中的中间的<br/> 用/n换行符代替
        # print(cont)
        x = re.sub(r'<.*?>',"",cont)
        # print(x)
        contents.append(x.strip())

    qiushis = []
    for value in zip(authors,contents):    # 打包为元组的列表 zip([1,2,3],[4,5,6]) -->[(1, 4), (2, 5), (3, 6)]
        author,content = value
        qiushi = {
            '作者': author,
            '内容': content
        }
        qiushis.append(qiushi)

    for qiushi in qiushis:
        print('='*120)
        for p in qiushi:
            print(p +":"+qiushi[p])

def main():
    # url = "https://www.qiushibaike.com/text/page/1"
    # parse_page(url)
    for x in range(1,4):   # 爬取第1页到3页的内容
        url = "https://www.qiushibaike.com/text/page/%s/" % x     # % 很好的应用
        parse_page(url)


if __name__ == '__main__':
    main()