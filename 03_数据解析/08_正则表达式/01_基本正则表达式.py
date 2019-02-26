# encoding: utf-8

import re

'''.在正则表达式中有特殊意义,因此在匹配字符串中的.时要使用转义字符\.'''

'''1. 匹配某个字符串：'''
# text = "hello"
# ret = re.match('hell', text) #  match(str,str) 将前面的字符串和后面的匹配,只能从后面字符串的头部开始匹配
# print(ret.group())


'''2. 点：匹配任意的字符(不可以匹配换行符)'''
# text = "hello\n"
# ret = re.match('.',text)    # 匹配后返回一个match对象
# print(type(ret))
# print(ret.group())          # 通过.group()方法将match对象转化为字符串

'''3. \d：匹配任意的数字（0-9）'''
# text = "312+"
# ret = re.match('\d',text)
# print(ret.group())

'''4. \D：匹配任意的非数字'''
# text = "we2"
# ret = re.match('\D',text)
# print(ret.group())

'''5. \s：匹配空白字符（\n，\t，\r，空格）'''
# text = "\t"
# ret = re.match('\s',text)
# print(ret.group())

'''6. \w：匹配的是a-z,A-Z,数字和下划线'''
# text = "_1qw+"
# ret = re.match('\w',text)
# print(ret.group())

'''7. \W：与\w相反。'''
# text = ")+)a"
# ret = re.match('\W',text)
# print(ret.group())

'''8. []组合的方式，只要满足中括号中的字符，就可以匹配 (从前往后匹配,知道匹配不上为止)'''
# text = "0731-88888888asfa"
# ret = re.match('[\d\-]+',text)
# print(ret.group())

'''8.1. 中括号的形式代替\d (\d相当于[0-9] 只能匹配一个字符)'''
# text = "09"
# ret = re.match('[0-9]',text)
# print(ret.group())

'''8.2. 中括号的形式代替\D ([^0-9]其中的^符号代表取反)'''
# text = "a1"
# ret = re.match('[^0-9]',text)
# print(ret.group())

'''8.3. 中括号的形式代替\w'''
# text = "a1_"
# ret = re.match('[a-zA-Z0-9_]',text)
# print(ret.group())

'''8.4. 中括号的形式代替\W'''
# text = "){0"
# ret = re.match('[^a-zA-Z0-9_]',text)
# print(ret.group())


######################## 匹配多个字符 ########################
'''9. *：可以匹配0或者任意多个字符'''
# text = "abcd()123()"
# ret = re.match('\D*',text)
# print(ret.group())

'''10. +：匹配1个或者多个字符'''
# text = "abcd+"
# ret = re.match('\w+',text)
# print(ret.group())

'''11. ?：匹配一个或者0个（要么没有，要么就只有一个）'''
# text = "123abcd"
# ret = re.match('\w?',text)
# print(ret.group())

'''12. {m}：匹配m个字符。'''
# text = "ab-cd"
# ret = re.match('\w{2}',text)
# print(ret.group())

'''13. {m,n}：匹配m-n个字符 (匹配的个数至少为m最大为n 否则报错)'''
# text = "324abcdab"
# ret = re.match('\w{1,5}',text)
# print(ret.group())


######################## 小案例 ########################
'''14. 验证手机号码：'''
# text = "13578900980"
# ret = re.match('1[34578]\d{9}',text)
# print(ret.group())

'''15. 验证邮箱：'''
# text = "hynever12_@163.com"
# ret = re.match('\w+@[a-z0-9]+\.[a-z]+',text)  # 因为.在正则表达式中有特殊意义,因此在匹配字符串中的.时要使用转义字符\.
# print(ret.group())

'''16. 验证URL'''
# text = "https://baike.baidu.com/item/Python/407313?fr=aladdin"
# ret = re.match('(http|https|ftp)://[^\s]+',text)
# print(ret.group())

'''17. 验证身份证：'''
# text = "31131118908123230x"
# ret = re.match('\d{17}[\dxX]',text)
# print(ret.group())

'''18. ^（脱字号）：表示以...开头'''
# text = "hello"
# ret = re.search('^he',text)
# print(ret.group())

'''19. $：表示以...结尾：(必须以$前面的匹配符结尾)'''
# text = "xxx@163.com"
# ret = re.match('\w+@163.com$',text)
# print(ret.group())

'''20. |：匹配多个字符串或者表达式：'''
# text = "https"
# ret = re.match('(ftp|http|https)$',text)        # 此处必须加上&符,因为不加的话也可能匹配上http
# print(ret.group())

'''******21：贪婪模式与非贪婪模式：'''
# text = "0123456"
# ret = re.match('\d+?',text)    #(\d+    贪婪模式,尽量去匹配多的字符)
# print(ret.group())             # (\d+?  非贪婪模式,匹配到很多,但是只取一个)

# text = "<h1>标题</h1>"
# ret = re.match('<.+>',text)       # <.+>      贪婪模式,会全都匹配到)
# ret1 = re.match('<.+?>',text)      # <.+?>      非贪婪模式,会查找满足<.+?>条件最短的,只取到 <h1>
# print(ret.group())
# print(ret1.group())

'''22：匹配0-100之间的数字'''
# 可以出现的：1，2，3，10，100，99
# 有三种情况：1，99，100
# 不可以出现的：09，101
text = "10"
ret = re.match('[1-9]\d?$|100$',text)
print(ret.group())
