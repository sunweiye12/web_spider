#encoding: utf-8
from urllib import parse

'''urlparse和urlsplit函数是用于将URL分段解析
'''
url = 'http://www.baidu.com/s?wd=python&username=abc#1'

result1 = parse.urlparse(url)
result2 = parse.urlsplit(url)   # urlsplit()函数查询结果中没有params属性   url = 'http://www.baidu.com/s;SUSSECE?wd=python&username=abc#1'
                                                                            # params = SUSSECE 这个属性用的特别少
print(result1)
print(result2)
print("-------------------------result1---------------------------------")
print('scheme:',result1.scheme)
print('netloc:',result1.netloc)
print('path:',result1.path)
print('params:',result1.params)
print('query:',result1.query)
print('fragment:',result1.fragment)
print("-------------------------result2---------------------------------")
print('scheme:',result2.scheme)
print('netloc:',result2.netloc)
print('path:',result2.path)
# print('params:',result2.params)
print('query:',result2.query)
print('fragment:',result2.fragment)