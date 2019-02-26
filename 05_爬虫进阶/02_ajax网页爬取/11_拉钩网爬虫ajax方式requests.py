# encoding: utf-8

import requests
from lxml import etree
import time
import re

# 因为拉勾网反爬虫机制比较强,所有要将请求头写完整
headers = {
     'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/62.0.3202.94 Safari/537.36',
    "Referer": 'https://www.lagou.com/jobs/list_python?labelWords=&fromSearch=true&suginput=',
    "Cookie": 'user_trace_token=20180913114808-fb106c01-781c-4a6d-805e-3aa66e13477a; LGUID=20180913114810-d502923f-b707-11e8-95da-525400f775ce; WEBTJ-ID=20190107104724-1682635271e378-0b3c1a0bf2ea95-7623246e-1310720-1682635271f682; sensorsdata2015jssdkcross=%7B%22distinct_id%22%3A%22167a67804419d-0eeb340580b524-7623246e-1310720-167a67804426e6%22%2C%22%24device_id%22%3A%22167a67804419d-0eeb340580b524-7623246e-1310720-167a67804426e6%22%2C%22props%22%3A%7B%22%24latest_traffic_source_type%22%3A%22%E7%9B%B4%E6%8E%A5%E6%B5%81%E9%87%8F%22%2C%22%24latest_referrer%22%3A%22%22%2C%22%24latest_referrer_host%22%3A%22%22%2C%22%24latest_search_keyword%22%3A%22%E6%9C%AA%E5%8F%96%E5%88%B0%E5%80%BC_%E7%9B%B4%E6%8E%A5%E6%89%93%E5%BC%80%22%7D%7D; JSESSIONID=ABAAABAAAGGABCBFAAC5A3EB552331EF883904A67B61ABF; _putrc=CDB81FAE9C7DD6A3123F89F2B170EADC; login=true; unick=%E6%8B%89%E5%8B%BE%E7%94%A8%E6%88%B70179; hasDeliver=0; gate_login_token=9d7a8cca4b342294b9fb39a45d1eb6ce23d151cc749df1fc2036b5863ccc4c6e; _gat=1; X_MIDDLE_TOKEN=c20dc6065097a368ea8598a063d63a65; TG-TRACK-CODE=index_search; _ga=GA1.2.175870042.1536810499; _gid=GA1.2.2015377061.1546829245; LGSID=20190107104721-8e5d8768-1226-11e9-b2af-5254005c3644; LGRID=20190107113325-fd7ed58b-122c-11e9-b2af-5254005c3644; Hm_lvt_4233e74dff0ae5bd0a3d81c6ccf756e6=1544685978,1546436617,1546568877,1546829245; Hm_lpvt_4233e74dff0ae5bd0a3d81c6ccf756e6=1546832008; SEARCH_ID=bc80009fd58a46e3958d5ba2fdad4d4c; index_location_city=%E5%85%A8%E5%9B%BD',
    'Origin': 'https://www.lagou.com',
    "X-Anit-Forge-Code": "0",
    "X-Anit-Forge-Token": "None",
    'X-Requested-With': "XMLHttpRequest"
}
proxy = {
    'https': '58.58.213.55:8888'
}

def request_list_page():
    url = 'https://www.lagou.com/jobs/positionAjax.json?city=%E6%B7%B1%E5%9C%B3&needAddtionalResult=false&isSchoolJob=0'
    data = {
        'first': "false",
        'pn': 1,
        'kd': 'java'
    }
    for x in range(1,2):
        data['pn'] = x

        # 注意! 此处应该注意,用的是post方式来请求,英雌可能存在Form Date数据
        response = requests.post(url, headers=headers,data=data)
        # json方法：如果返回来的是json数据。那么这个方法会自动的load成字典(如果返回的不是json数据,此方法报错)
        # 可以通过返回的response数据来判断是否为json数据
        result = response.json()    # 返回字典
        print(result)
        positions = result['content']['positionResult']['result']   # 通过字典逐一向下查询返回所有职位
        for position in positions:
            positionId = position['positionId']                        # 查找每一个职位的id信息
            position_url = 'https://www.lagou.com/jobs/%s.html' % positionId    # 通过职位的id来拼接出每一个职位的详细信息页面网址
            parse_postion_detail(position_url)                          # 通过调用方法提取详细信息
            break   # 获取第一个职位信息后就结束
            time.sleep(1)
        break       # 获取第一页信息,后结束

def parse_postion_detail(url):
    response = requests.get(url,headers=headers)
    text = response.text
    html = etree.HTML(text)
    position_name = html.xpath("//span[@class='name']/text()")[0]
    job_request_spans = html.xpath("//dd[@class='job_request']//span")
    salary = job_request_spans[0].xpath('.//text()')[0].strip()
    city = job_request_spans[1].xpath(".//text()")[0].strip()
    city = re.sub(r"[\s/]","",city)
    work_years = job_request_spans[2].xpath(".//text()")[0].strip()
    work_years = re.sub(r"[\s/]","",work_years)
    education = job_request_spans[3].xpath(".//text()")[0].strip()
    education = re.sub(r"[\s/]","",education)
    desc = "".join(html.xpath("//dd[@class='job_bt']//text()")).strip()
    print(desc)


def main():
    request_list_page()

if __name__ == '__main__':
    main()