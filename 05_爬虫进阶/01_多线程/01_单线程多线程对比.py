#encoding: utf-8

import time
import threading # 内置模块


"""---------------------采用单线程的方式：---------------------"""

def coding1():
    for x in range(3):
        print('正在写代码%s'%x)
        time.sleep(1)   # 沉睡一秒

def drawing1():
    for x in range(3):
        print('正在画图%s'%x)
        time.sleep(1)


def main1():
    print(threading.enumerate())
    coding1()
    drawing1()




"""--------------采用多线程的方式：---------------------"""

def coding2():
    for x in range(3):
        print('正在写代码%s'%threading.current_thread())
        time.sleep(1)

def drawing2():
    for x in range(3):
        print('正在画图%s' %threading.current_thread())   # threading.current_thread() 当前线程
        time.sleep(1)

def main2():

    t1 = threading.Thread(target=coding2)    # 准备一个线程,并绑定方法( 不用加括号 ******)
    t2 = threading.Thread(target=drawing2)

    t1.start()                      # 开启线程,当方法执行完毕自动关闭线程
    t2.start()

    print(threading.enumerate())    # threading.enumerate() 枚举出当前所有的线程数

if __name__ == '__main__':
    main2()
    pass