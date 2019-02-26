# -*- coding: utf-8 -*-
'''
# 此类是为了处理传递的数据并保存数据-----------------------(框架是规定的,不能够修改方法名)
    如下所示一共有三种方式(最常用的是前两种--都是框架提供的方式)
    #第一种是每次传来数据都直接写到文件中,一行一行的写入,因此这种方法占用内存少,但是不在符合json文件的格式
    #第二种是每次传来数据先积累到内存中,在调用expoeter.finish_exporting()方法时一起写入,缺点是占用内存,优点是符合json文件的格式
'''

#------------------------------------------利用JsonLinesItemExporter来实现文件的存储---------------------------------------------
from  scrapy.exporters import JsonLinesItemExporter # 利用scrapy内置的导出器来实现

class A01QsbkPipeline(object):
    def __init__(self):
        """初始化的时候打开一个json文件用于后序写入操作"""
        self.fp = open("段子.json",'wb')         # wb 以二进制来打开
        self.expoeter = JsonLinesItemExporter(self.fp , ensure_ascii = False , encoding='utf-8')

    def open_spider(self,spider):
        """开启爬虫时进行的操作"""
        print("爬虫开始啦")

    def process_item(self, item, spider):       # 在爬虫函数中 yield 传递的值会赋值给 item 并执行这个方法******************
        self.expoeter.export_item(item)     # 执行expoeter任务(将每一行的数据逐一写入文本)
        return item

    def close_spider(self,spider):
        """关闭爬虫时进行的操作"""
        self.fp.close()                         # 关闭文件
        print("爬虫结束啦")


# #------------------------------------------利用JsonItemExporter来实现文件的存储---------------------------------------------
# from  scrapy.exporters import JsonItemExporter,JsonLinesItemExporter
#
# class A01QsbkPipeline(object):
#     def __init__(self):
#         """初始化的时候打开一个json文件用于后序写入操作"""
#         self.fp = open("段子.json",'wb')         # wb 以二进制来打开
#         self.expoeter = JsonItemExporter(self.fp , ensure_ascii = False , encoding='utf-8')
#
#     def open_spider(self,spider):
#         """开启爬虫时进行的操作"""
#         self.expoeter.start_exporting()  # 开启expoeter
#         print("爬虫开始啦")
#
#     def process_item(self, item, spider):       # 在爬虫函数中 yield 传递的值会赋值给 item 并执行这个方法******************
#         self.expoeter.export_item(item)     # 执行expoeter任务(分别将每一项添加到一个列表中)   (8888888888888缺点:耗内存8888888888888)
#         return item
#
#     def close_spider(self,spider):
#         """关闭爬虫时进行的操作"""
#         self.expoeter.finish_exporting()        # 结束expoeter(统一写入)
#         self.fp.close()                         # 关闭
#         print("爬虫结束啦")


        #------------------------------------------利用json来实现文件的存储---------------------------------------------
# import json
# class A01QsbkPipeline(object):
#
#     def __init__(self):
#         """初始化的时候打开一个json文件用于后序写入操作"""
#         self.fp = open("段子.json",'w',encoding='utf-8')
#
#     def open_spider(self,spider):
#         """开启爬虫时进行的操作"""
#         print("爬虫开始啦")
#
#     def process_item(self, item, spider):       # 在爬虫函数中 yield 传递的值会赋值给 item 并执行这个方法******************
#         item_json = json.dumps(dict(item),ensure_ascii=False)        # 将字典对象dumps成json格式文件
#         self.fp.write(item_json + '\n')
#         return item
#
#     def close_spider(self,spider):
#         """关闭爬虫时进行的操作"""
#         self.fp.close()
#         print("爬虫结束啦")