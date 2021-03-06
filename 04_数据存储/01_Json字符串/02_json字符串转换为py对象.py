# encoding: utf-8
import json

json_str = '[{"username": "张三", "age": 18, "country": "china"}, {"username": "李赛", "age": 20, "country": "china"}]'
# 将json格式的字符串转换成python对象                **********.loads()方法
persons = json.loads(json_str)
print(type(persons))
for person in persons:
    print(person)

# 将存有json数据类型的json文件转换成python对象
# **********.load()方法
with open('person.json','r',encoding='utf-8') as fp:
    persons = json.load(fp)
    print(type(persons))
    for person in persons:
        print(person)