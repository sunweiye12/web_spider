#encoding: utf-8

import requests
from lxml import etree
from urllib import request     # 用于将文图片保存到本地
import os                       # 用于提取图片名的后缀
import re

def parse_page(url):
    headers = {
        'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/62.0.3202.94 Safari/537.36'
    }

    response = requests.get(url,headers=headers)
    text = response.text
    html = etree.HTML(text)

    # //a[@class='col-xs-6col-sm-3']/img[last()]/@src

    imgs = html.xpath("//div[@class='page-content text-center']//img[@class!='gif']")
    for img in imgs:
        # print(etree.tostring(img))
        img_url = img.get('data-original')
        alt = img.get('alt')    # 通过get来获取元素属性
        alt = re.sub(r'[\?? \.，。！!]','',alt)    # 通过正则表达式获取文件名(去除文件名中的标点符号)
        suffix = os.path.splitext(img_url)[1]       # 通过os模块开获取文件后缀(分割路径，返回路径名和文件扩展名的元组)
        filename = alt + suffix
        # print(filename)
        request.urlretrieve(img_url,'images/'+filename)     # 将图片下载到本地文件夹中

def main():
    for x in range(1,2):
        url = 'http://www.doutula.com/photo/list/?page=%d' % x
        parse_page(url)

if __name__ == '__main__':
    main()