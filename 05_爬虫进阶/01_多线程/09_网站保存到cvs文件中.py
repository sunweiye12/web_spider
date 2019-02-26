# coding:utf-8

import csv
import requests
import threading
from queue import Queue
from lxml import etree
import time

'''通过多线程来下载百思不得姐的文本'''
'''
生产者消费者模式
    生产者将通过每个页面的连接来获得每个段子,并放到队列中
    消费者通过每个段子将内容保存到文件中
'''

HEADERS = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/62.0.3202.94 Safari/537.36'
}
NUM = 1
class Product(threading.Thread):
    """生产者"""

    def __init__(self,page_queue,joke_queue,*args,**kwargs):
        super(Product, self).__init__(*args,**kwargs)
        self.page_queue = page_queue
        self.joke_queue = joke_queue

    def run(self):
        while True:
            if self.page_queue.empty():
                break
            else:
                url = self.page_queue.get()
                response = requests.get(url,headers = HEADERS)
                text = response.text
                html = etree.HTML(text)
                jokes = html.xpath("//div[@class='j-r-list-c-desc']")
                users = html.xpath("//div[@class='u-txt']")         # 里面包含作者还有发布时间

                myjoke = []
                for joke in jokes:      # 处理每一个笑话返回笑话列表
                    joke = joke.xpath(".//text()")
                    joke = "\n".join(joke).strip()
                    myjoke.append(joke)

                myuser = []
                mytime = []
                for user in users:      # 处理每一个用户和发布时间的列表
                    user = user.xpath(".//text()")
                    u = user[1].strip()         # 用户名
                    t = user[3].strip()         # 发表时间
                    myuser.append(u)
                    mytime.append(t)


                li = zip(myuser,mytime,myjoke)   # 返回一个以元素为元素的列表

                for i in li:
                    self.joke_queue.put(i)      # 将每一个元组放到列表中 元组(user,time,joke)

                print(self.joke_queue.empty())      #------------------------
                print('=' * 50 + "第%s页下载完成！" % url.split('/')[-1] + "=" * 50)


class Consumer(threading.Thread):
    """消费者"""
    def __init__(self,joke_queue,writer,gLock,*args,**kwargs):
        super(Consumer, self).__init__(*args,**kwargs)
        self.joke_queue = joke_queue
        self.writer = writer
        self.lock = gLock

    def run(self):
        global NUM
        while True:
            try:
                if not self.joke_queue.empty():         # 因为前面有了一段积累了一段时间的数据,所以可以在这判断,如果没有了可以直接结束程序
                    joke_info = self.joke_queue.get(timeout=40)
                    self.lock.acquire()
                    self.writer.writerow(joke_info)
                    self.lock.release()
                    print('保存成功%d 条' %NUM)
                    NUM += 1
                else:
                    break
            except:
                break

def main():
    page_queue = Queue(10)
    joke_queue = Queue(200)
    gLock = threading.Lock()        #########重点  有括号

    fp = open('99_test//bsbdj.csv', 'a', newline='', encoding='utf-8')
    writer = csv.writer(fp)
    writer.writerow(('user', 'time','joke'))    # 先写表头

    for x in range(1,11):
        url = "http://www.budejie.com/text/%d" %x
        # print(url)
        page_queue.put(url)

    for i in range(5):
        p = Product(page_queue,joke_queue)
        p.start()

    time.sleep(1)   # 沉睡一秒是为了使得joke_queue队列中存有数据然后消费者那去消费

    for i in range(5):
        c = Consumer(joke_queue,writer,gLock)
        c.start()

if __name__ == '__main__':
    main()