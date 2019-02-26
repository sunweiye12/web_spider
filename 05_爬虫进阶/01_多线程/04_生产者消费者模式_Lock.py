#encoding: utf-8

import threading
import random
import time

gLock = threading.Lock()    # 定义线程锁

gMoney = 1000       # 定义当前金钱数量
gTotalTimes = 10    # 生产者最多生产的次数(生产者生产10此以后结束)
gTimes = 0          # 生产者生产金钱的数量


class Producer(threading.Thread):
    """生产者"""
    def run(self):
        global gMoney
        global gTimes
        while True:
            money = random.randint(100,1000)

            gLock.acquire()
            if gTimes >= gTotalTimes:
                gLock.release()
                break
            gMoney += money
            print('%s生产了%d元钱，剩余%d元钱'%(threading.current_thread(),money,gMoney))
            gTimes += 1
            gLock.release()

            time.sleep(0.5)


class Consumer(threading.Thread):
    """消费者"""
    def run(self):
        global gMoney
        while True:
            money = random.randint(100,1000)

            gLock.acquire()
            if gMoney >= money:
                gMoney -= money
                print('%s消费者消费了%d元钱，剩余%d元钱' % (threading.current_thread(),money,gMoney))
            else:
                if gTimes >= gTotalTimes:
                    gLock.release()
                    break
                print('%s消费者准备消费%d元钱，剩余%d元钱，不足！'%(threading.current_thread(),money,gMoney))
            gLock.release()

            time.sleep(0.5)


def main():
    for x in range(3):
        """定义三个消费者"""
        t = Consumer(name='消费者线程%d'%x)      # 初始化时定义线程名字
        t.start()

    for x in range(5):
        """定义五个生产者"""
        t = Producer(name="生产者线程%d"%x)
        t.start()

if __name__ == '__main__':
    main()