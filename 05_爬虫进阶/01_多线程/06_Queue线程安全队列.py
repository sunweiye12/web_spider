#encoding: utf-8

from queue import Queue
import time
import threading

# q = Queue(4)
#
# for x in range(4):
#     q.put(x)
#
# for x in range(4):
#     print(q.get())

def set_value(q):
    index = 0
    while True:
        q.put(index)       # 默认block=True ,当队列为满的时候会默认等待,直到有空间以后再添加进去
        index += 1
        time.sleep(1)

def get_value(q):
    while True:
        print(q.get())   # 默认block=True ,当队列中没有值的时候会默认等待

def main():
    q = Queue(4)        # 设置队列的容积为4
    # q.put()   添加一个元素
    # q.get()   在底部拿走一个元素
    t1 = threading.Thread(target=set_value,args=[q])        # 设置开启线程的函数和参数
    t2 = threading.Thread(target=get_value,args=[q])

    t1.start()
    t2.start()

if __name__ == '__main__':
    main()

