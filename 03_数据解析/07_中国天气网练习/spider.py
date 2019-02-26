#encoding: utf-8

import requests
from bs4 import BeautifulSoup
from pyecharts import Bar       # 新增模块

ALL_DATA = []

HEADERS = {
        'User-Agent': "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/62.0.3202.94 Safari/537.36"
    }

def parse_page(url):

    response = requests.get(url,headers=HEADERS)
    text = response.content.decode('utf-8')
    # print(text)     # 打印一下网页看一下

    # html5lib
    # pip install html5lib      这个解析器兼容能力出众
    soup = BeautifulSoup(text,'html5lib')
    conMidtab = soup.find('div',class_='conMidtab')     # 只找到第一个
    tables = conMidtab.find_all('table')
    for table in tables:
        trs = table.find_all('tr')[2:]
        for index,tr in enumerate(trs):
            tds = tr.find_all('td')
            city_td = tds[0]       # 获取城市名的标签,其中每个trs开头的tr城市名称在第二个td中(第一个td存放的是省的名称)
            if index == 0:
                city_td = tds[1]
            city = list(city_td.stripped_strings)[0]    # 获取城市的名称
            temp_td = tds[-2]           # 获取 ,显示最低温度的标签
            min_temp = list(temp_td.stripped_strings)[0]    # 获取最低温度
            ALL_DATA.append({"city":city,"min_temp":int(min_temp)}) #将数据以字典的形式存放到ALL_DATA列表中
            # print({"city":city,"min_temp":int(min_temp)})         # 打印一下需要的信息

def main():
    urls = [
        'http://www.weather.com.cn/textFC/hb.shtml',
        'http://www.weather.com.cn/textFC/db.shtml',
        'http://www.weather.com.cn/textFC/hd.shtml',
        'http://www.weather.com.cn/textFC/hz.shtml',
        'http://www.weather.com.cn/textFC/hn.shtml',
        'http://www.weather.com.cn/textFC/xb.shtml',
        'http://www.weather.com.cn/textFC/xn.shtml',
        'http://www.weather.com.cn/textFC/gat.shtml'
    ]

    for url in urls:
        parse_page(url)

    # 分析数据
    # ALL_DATA中的数据根据最低气温进行排序
    ALL_DATA.sort(key=lambda data:data['min_temp'])     # 对一个列表中存在的字典进行排序操作,并执行比较每个字典中的min_temp数据

    data = ALL_DATA[0:10]   # 截取前十个数据
    # map(fun,list) 第一个参数为函数,第二个参数为列表元组等,将每一个元素执行函数操作,返回一个map,强转为list
    cities = list(map(lambda x:x['city'],data))
    temps = list(map(lambda x:x['min_temp'],data))
    # pyecharts
    # pip install pyecharts
    chart = Bar("中国天最低天气温排行榜")  # *****绘制可视化图像
    chart.add('',cities,temps)

    chart.render('temperature.html')

if __name__ == '__main__':
    main()


    '''对一个列表中存在的字典进行排序操作,并执行比较每个字典中的min_temp数据'''
    # ALL_DATA = [
    #     {"city": "北京", 'min_temp': 0},
    #     {"city": "天津", 'min_temp': -8},
    #     {"city": "石家庄", 'min_temp': -10}
    # ]
    # ALL_DATA.sort(key=lambda data:data['min_temp'])  # data代表列表中的元素也就是一个字典
    # print(ALL_DATA)