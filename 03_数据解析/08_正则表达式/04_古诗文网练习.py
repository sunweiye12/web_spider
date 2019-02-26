#encoding: utf-8

import requests
import re

def parse_page(url):
    headers = {
        'User-Agent': "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/62.0.3202.94 Safari/537.36"
    }
    response = requests.get(url,headers)
    text = response.text
    # print(text)  # 打印一下网页源码
    # re.DOTALL：可以让.匹配\n
    titles = re.findall(r'<div\sclass="cont">.*?<b>(.*?)</b>',text,re.DOTALL)               # 搜索到所有的题目(获取到分组中的内容)
    dynasties = re.findall(r'<p class="source">.*?<a.*?>(.*?)</a>',text,re.DOTALL)          # 搜索到所有的朝代
    authors = re.findall(r'<p class="source">.*?<a.*?>.*?<a.*?>(.*?)</a>',text,re.DOTALL)  # 搜索到所有的诗人
    content_tags = re.findall(r'<div class="contson" .*?>(.*?)</div>',text,re.DOTALL)       # 搜索到所有的诗(包括中间的<br/>)

    contents = []
    for content in content_tags:        # 去除所有诗词内容中的中间的<br/> 用/n换行符代替
        # print(content)
        x = re.sub(r'<.*?>',"",content)
        contents.append(x.strip())

    poems = []
    for value in zip(titles,dynasties,authors,contents):    # 打包为元组的列表 zip([1,2,3],[4,5,6]) -->[(1, 4), (2, 5), (3, 6)]
        title,dynasty,author,content = value
        poem = {
            '题目':title,
            '朝代': dynasty,
            '作者': author,
            '---': content
        }
        poems.append(poem)


    for poem in poems:
        print('='*120)
        for p in poem:
            print(p +":"+poem[p])




def main():
    for x in range(1,11):   # 爬取第1页到10页的诗句
        url = "http://www.gushiwen.org/default_%s.aspx" % x     # % 很好的应用
        parse_page(url)


if __name__ == '__main__':
    main()