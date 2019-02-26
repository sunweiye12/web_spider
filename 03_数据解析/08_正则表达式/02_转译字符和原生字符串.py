#encoding: utf-8
import re

'''匹配转译字符'''
# text = "apple price is $299"
# ret = re.search("\$\d+",text)   # search()方法,不是从头开始匹配,而是在字符串中搜索匹配
# print(ret.group())

# text = '\\n'    # \n代表换行,如果只想打印\n而不是换行,在前面加一个\
# print(text)

'''匹配原生字符串'''
# r = raw = 原生的(代表使用原生字符串,在前面加上r)
# text = r'\n'        # 前面加r 代表为原生字符串,不做任何处理
# print(text)

# text = "\\n"    #= '\n'
# python：
# '\\n' = \n
# '\\\\n' =》 \\n
# \\c

# 正则表达式中：\n =
# \\n =》 \n
# \\c =》 \c

text = "\\n"            # 匹配出 \n
ret = re.match(r'\\n',text)
# ret = re.match('\\\\n',text)
print(ret.group())