# encoding: utf-8

import json

"""只有基本类型才能够转换为json字符串"""
"""将python对象转换为json字符串"""

# 创建两个对象(用列表中字典代替)
persons = [
    {
        'username':"张三",
        'age': 18,
        'country': 'china'
    },
    {
        'username': '李赛',
        'age': 20,
        'country': 'china'
    }
]

# 直接将数据转化为字符串           ********.dumps()
json_str = json.dumps(persons)         # .dumps()函数 将数据转化为字符串
print(type(json_str))   # json字符串格式
print(json_str)

# 将数据写到文件中                  *******.dump()
with open('person.json','w',encoding='utf-8') as fp:
    # fp.write(json_str)
    json.dump(persons,fp,ensure_ascii=False)  # ensure_ascii=False 支持中文信息



# 只有基本类型才能够转换为json字符串,所以下面会报错
# class Person(object):
#     country = 'china'
#
# a = {
#     'person': Person()
# }
# json.dumps(a)
