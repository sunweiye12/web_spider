# encoding: utf-8

import csv

def read_csv_demo1():
    with open('stock.csv', 'r') as fp:
        # reader是一个迭代器
        reader = csv.reader(fp)  # 返回一个迭代器(迭代器中存放的是列表)
        for i in reader:        # 遍历迭代器
            print(i)             # 打印每一行的信息

        # next(reader)            # 将迭代器指针移到下一行,(相当于从下一行数据开始)
        # for x in reader:
        #     name = x[3]
        #     volumn = x[-1]
        #     print({'name': name, 'volumn': volumn})


def read_csv_demo2():
    with open('stock.csv','r') as fp:
        # 使用DictReader创建的reader对象
        # 不会包含标题那行的数据(*****)
        reader = csv.DictReader(fp)   # 返回一个迭代器(迭代器中存放的是字典(此字典为有序字典))
        for i in reader:            # 每一行是是一个字典(数据从第二行开始,字典的key为第一行)
            name = i['secShortName']
            volumn = i['turnoverVol']
            print({'name': name, 'volumn': volumn})

if __name__ == '__main__':
    read_csv_demo2()
