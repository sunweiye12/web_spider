# encoding: utf-8

import threading
import time

VALUE = 0       # 全局变量

myLock = threading.Lock()   # 定义一个线程锁(在锁中只允许存在一个线程)

def add_value():
    global VALUE    # 在函数中引用(修改)全局变量,要用global声明一下

    myLock.acquire()    # 开启线程锁(在锁内修改全局变量)
    for x in range(1000000):
        VALUE += 1
    myLock.release()    # 释放线程锁

    print('value：%d'%VALUE)

def main():
    for x in range(2):  # 开启两个线程
        t = threading.Thread(target=add_value)
        t.start()

if __name__ == '__main__':
    main()