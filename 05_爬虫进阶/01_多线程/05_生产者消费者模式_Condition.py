#encoding: utf-8

import threading
import random
import time

gCondition = threading.Condition()

gMoney = 1000
gTotalTimes = 10
gTimes = 0


class Producer(threading.Thread):
    '''生产者'''
    def run(self):
        global gMoney
        global gTimes
        while True:
            money = random.randint(100,1000)

            gCondition.acquire()
            if gTimes >= gTotalTimes:
                gCondition.release()
                break
            gMoney += money
            print('%s生产了%d元钱，剩余%d元钱'%(threading.current_thread(),money,gMoney))
            gTimes += 1
            gCondition.notify_all()     # 通知在等待的线程(生产完钱以后就通知所有等待的线程)
            gCondition.release()        # 释放线程

            time.sleep(0.5)


class Consumer(threading.Thread):
    '''消费者'''
    def run(self):
        global gMoney
        while True:
            money = random.randint(100,1000)

            gCondition.acquire()
            while gMoney < money:
                print('%s准备消费%d元钱，剩余%d元钱，不足！' % (threading.current_thread(),money,gMoney))
                gCondition.wait()   # 如果余额不足就先等待
            if gTimes >= gTotalTimes:
                gCondition.release()
                return
            gMoney -= money
            print('%s消费了%d元钱，剩余%d元钱' % (threading.current_thread(),money,gMoney))
            gCondition.release()

            time.sleep(0.5)


def main():
    for x in range(3):
        t = Consumer(name='消费者线程%d'%x)
        t.start()

    for x in range(5):
        t = Producer(name="生产者线程%d"%x)
        t.start()

if __name__ == '__main__':
    main()