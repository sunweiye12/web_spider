#encoding: utf-8

import re

'''分组'''
# text = "apple's price $99,orange's price is $10"
# ret = re.search('.*(\$\d+).*(\$\d+)',text)  # 两个括号代表有两个分组
# print(ret.group())      # 获得匹配诶的所有内容
# print(ret.group(0))     # 获得匹配诶的所有内容
# print(ret.group(1))     # 获得匹配诶的第一个分组
# print(ret.group(2))     # 获得匹配诶的第二个分组  以上返回字符串
# print(ret.group(1,2))   # 返回第一和第二个分组的元组
# print(ret.groups())     # 返回所有分组的元组


'''find_all函数：'''
text = "apple's price $99,orange's price is $10哈$78997"
ret = re.findall('\$\d+',text)  # 寻找所有匹配的字符串,返回一个列表
print(ret)


'''sub函数：(替换)'''
# text = "apple's price $99,orange's price is $10"
# ret = re.sub('\$\d+',"10",text)     # 将匹配到的值转换成第二个参数,返回字符串
# print(ret)


'''split函数：'''
# text = "hello&world ni hao"
# ret = re.split('[^a-zA-Z]',text)    # 通过字符串切片,返回列表
# print(ret)

# html = """
# <dd class="job_bt">
#         <h3 class="description">职位描述：</h3>
#         <div>
#         <p>参与公司新一代面向生命科学行业云服务应用及平台的开发。</p>
# <p><br></p>
# <p>【工作职责】</p>
# <p>云服务软件产品的架构设计与开发</p>
# <p>与设计、产品及前端人员沟通，保证产品的质量和开发进度</p>
# <p>研究新兴技术，对产品进行持续优化</p>
# <p><br></p>
# <p>【职位要求】</p>
# <p>计算机相关专业本科及以上学历</p>
# <p>对常见数据结构和面向对象设计有深入理解</p>
# <p>熟练掌握Python语言，3年以上实际经验</p>
# <p>熟悉Python Web开发框架如Django</p>
# <p>熟练掌握数据库开发和设计</p>
# <p>基本的英文读写能力</p>
#         </div>
#     </dd>
# """
# ret = re.sub('<.+?>',"",html)   # 去除所有标签
# print(ret)

'''compile()函数:(用于提高编译效率)'''
text = "the number is 20.50"
r = re.compile('\d+\.?\d*')         # 如果经常使用正则的话,可以考虑将他编译到内存中
r = re.compile(r"""        # VERBOSE注释(用来解释自己的正则表达式)
    \d+ # 小数点前面的数字
    \.? # 小数点本身
    \d* # 小数点后面的数字
""",re.VERBOSE)

ret = re.search(r,text)
print(ret.group())