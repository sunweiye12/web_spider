# encoding: utf-8
"""
利用多线程爬取斗图啦上1至6页的图片
利用xpath解析网页
利用urllib中的request.urlretrieve将图片下载到本地
利用正则表达式来替换文件名中的特殊符号
利用Queue来存放线程数据
os.path.splitext    获取文件的后缀
"""
import requests
from lxml import etree
from urllib import request
import os
import re
from queue import Queue
import threading

class Procuder(threading.Thread):
    """生产者,产出图片的URL"""
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/62.0.3202.94 Safari/537.36'
    }
    def __init__(self,page_queue,img_queue,*args,**kwargs):
        super(Procuder, self).__init__(*args,**kwargs)
        self.page_queue = page_queue
        self.img_queue = img_queue

    def run(self):
        while True:
            if self.page_queue.empty():
                break
            url = self.page_queue.get()
            self.parse_page(url)    # 调用方法

    def parse_page(self,url):
        response = requests.get(url,headers=self.headers)
        text = response.text
        html = etree.HTML(text)
        imgs = html.xpath("//div[@class='page-content text-center']//img[@class!='gif']")
        for img in imgs:
            img_url = img.get('data-original')      # 获取图片的地址
            alt = img.get('alt')                       # 获取图片文字
            alt = re.sub(r'[\?？\.，。！!\*]','',alt)
            suffix = os.path.splitext(img_url)[1]       # 获取文件的后缀
            suffix = suffix.split("!")[0]               # 获得文件后缀
            filename = alt + suffix
            self.img_queue.put((img_url,filename))      #将URL和Filename存到队列里

class Consumer(threading.Thread):
    """消费者,通过URL将图片下载到本地"""
    def __init__(self,page_queue,img_queue,*args,**kwargs):
        super(Consumer, self).__init__(*args,**kwargs)
        self.page_queue = page_queue
        self.img_queue = img_queue

    def run(self):
        while True:
            if self.img_queue.empty() and self.page_queue.empty():
                break
            img_url,filename = self.img_queue.get()
            request.urlretrieve(img_url, 'images/' + filename)  # 将图片下载到本地文件夹中
            print(filename+'  下载完成！')


def main():
    page_queue = Queue(100)     # 页面的队列
    img_queue = Queue(1000)     # 图片地址的队列
    for x in range(1,7):        # 爬取网页的个数
        url = 'http://www.doutula.com/photo/list/?page=%d' % x
        page_queue.put(url)

    for x in range(5):
        t = Procuder(page_queue,img_queue)
        t.start()

    for x in range(5):
        t = Consumer(page_queue,img_queue)
        t.start()


if __name__ == '__main__':
    main()
