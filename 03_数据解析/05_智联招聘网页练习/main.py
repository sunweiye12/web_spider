#encoding: utf-8

# 腾讯招聘网爬虫作业

from lxml import etree
import requests
# 输入相关的职业
KEYWORD = "python"
# 基础域名
BASE_DOMAIN = "https://sou.zhaopin.com/"
# 代理引擎
PROXY = {
     'http': '119.101.116.156:9999'
}
# 请求头
HEADERS = {
    "User-Agent": "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/55.0.2883.87 UBrowser/6.2.4094.1 Safari/537.36",
    "Cookie": "sts_deviceid=164bcfc1e8a54-02a8e03950faef-71292b6e-1764000-164bcfc1e8b685; urlfrom=121122523; urlfrom2=121122523; adfcid=u3782246.k95735843897.a24711517170.pb; adfcid2=u3782246.k95735843897.a24711517170.pb; adfbid=0; adfbid2=0; dywez=95841923.1545725177.2.2.dywecsr=baiduPC|dyweccn=ty|dywecmd=CPC|dywectr=8816174|dywecct=pp; sts_sg=1; sts_chnlsid=121122523; zp_src_url=https%3A%2F%2Fwww.baidu.com%2Fbaidu.php%3Fsc.a00000apJPO0FYNyJzmAJJQSGgAlCjstJDOdgi7rN2_3-BTFpEI98en7q1p7nMaCBOtbK0WvxXUrVQdRsrTN7qz_qr-_ugi1GJJmvTfT9mvkbI5YBFiMCTcikVZ4nteQwQ8rXBtfxlhSDYq43Dv1F1PXAsFwQ1VjaGqaPmFCBp9WPAQqmNAYxEM7PqQY7bJr1JNpZ_YLhP-bPjgzS6.7Y_NR2Ar5Od669BCXgjRzeASFDZtwhUVHf632MRRt_Q_DNKnLeMX5DkgboozuPvHWdWxfik63Sr1FberMzeISek3eVMukvUOZzuzIMWgg8otpOA1zkLqTDd7BJ9fkkOS_D7a5z3phgmLkc6z3PrrjUzkF3rxxKfYt_U_DY2yQvTyjtLsqT7jHzlRL5spy59OPt5gKfYtVKnv-Wu_olpOZ_l32AM-9I7fH7fmk3S8a9G4myIrP-SJFB9CyFB1FuvUer1Wz4r1-kl-9h9me2Sh1BC.U1Y10ZDqdIjA80Kspynqn0KY5Igfko60pyYqnWcd0ATqIyNsT100Iybqmh7GuZN_UfKspyfqnfKWpyfqn16d0AdY5HDsnHIxnH0krNtznjmzg1nvnjD0pvbqn0KzIjYknHc0uy-b5HDYn1FxnWDsP19xnW6znjuxnW6kn17xnWTLPH7xnW6kPjKxnWckPW00mhbqPj0zg1csP0KVm1Y3nH03nHbLPW-xnH0snNt1nH64nWfYnjTdg100TgKGujYs0Z7Wpyfqn0KzuLw9u1Ys0A7B5HKxn0K-ThTqn0KsTjY1nHmvrHfvP10d0A4vTjYsQW0snj0snj0s0AdYTjYs0AwbUL0qn0KzpWYs0Aw-IWdsmsKhIjYs0ZKC5H00ULnqn0KBI1Ykn0K8IjYs0ZPl5fKYIgnqnHRknjnsPWfvPWRYn10znWcYnH60ThNkIjYkPHfdP1cdnHc3n16k0ZPGujdbnWRdnhmvn10snj01ny7b0AP1UHdDPYuDn1n1fHF7wHR1Pbf10A7W5HD0TA3qn0KkUgfqn0KkUgnqn0KlIjYs0AdWgvuzUvYqn7tsg1Kxn0Kbmy4dmhNxTAk9Uh-bT1Ysg1Kxn7ts0ZK9I7qhUA7M5H00uAPGujYs0ANYpyfqQHD0mgPsmvnqn0KdTA-8mvnqn0KkUymqn0KhmLNY5H00uMGC5H00uh7Y5H00XMK_Ignqn0K9uAu_myTqnfK_uhnqn0KWThnqnWmdPj6%26word%3D%25E6%258B%259B%25E8%2581%2598%26ck%3D7818.15.95.312.412.240.213.223%26shh%3Dwww.baidu.com%26sht%3D02049043_24_pg%26us%3D2.12414.2.0.2.818.0%26bc%3D110101; __xsptplus30=30.2.1545725179.1545725179.1%231%7CbaiduPC%7CCPC%7Cty%7C8816174%7Cpp%23%23uC3jlaRgsU37jaTYxWmNffm2VQlqjRQg%23; _jzqy=1.1532178998.1545725180.2.jzqsr=baidu|jzqct=%E8%B5%B6%E9%9B%86%E7%BD%91%E5%85%BC%E8%81%8C%E6%8B%9B%E8%81%98.jzqsr=baidu|jzqct=%E6%8B%9B%E8%81%98; _jzqckmp=1; sajssdk_2015_cross_new_user=1; qrcodekey=f05c82d34e20415298316655bbfbb690; _jzqa=1.1833510942124285700.1532178998.1532178998.1545725180.2; _jzqc=1; firstchannelurl=https%3A//passport.zhaopin.com/login; lastchannelurl=https%3A//ts.zhaopin.com/jump/index_new.html%3Futm_source%3DbaiduPC%26utm_medium%3DCPC%26utm_term%3D8816174%26utm_content%3Dpp%26utm_campaign%3Dty%26utm_provider%3Dpartner%26sid%3D121122523%26site%3Du3782246.k95735843897.a24711517170.pb; index-c=2; JsNewlogin=2125602371; JSloginnamecookie=17801020179; JSShowname=; at=973e290c2aad4ee99231a0ca91811855; Token=973e290c2aad4ee99231a0ca91811855; rt=6a254aa8be2c42e0b8c2fbb5a6478697; JSpUserInfo=36672168546b5c7541775d7142654471516356655a69586b4e713b653f775877406554675d68596b5a75417757714765467152635e6553692e6b38714a65027710771f6514670068006b12751477257146654571536349650b69046b18714c65227731774c6552675e68286b3f754c77547146655a715763476559695d6b4f7140654a7724773d655e675468526b3e75307758713d653b7155635f655d69586b41714665437756774165586730683d6b567540775e7124653e715863576553691; uiioit=213671340f69426b5d6a507941644074023505325b75586d51683b7420734936053409698; jobRiskWarning=true; acw_tc=3ccdc16315457252526385353e1d0cc728192e6d887e78d64429608dd328c9; dywea=95841923.2335120292649629700.1532178997.1532178997.1545725177.2; dywec=95841923; __utma=269921210.824213735.1532178997.1532178997.1545725178.2; __utmc=269921210; __utmz=269921210.1545725178.2.2.utmcsr=baiduPC|utmccn=ty|utmcmd=CPC|utmctr=8816174|utmcct=pp; loginreleased=1; ZP_OLD_FLAG=false; sensorsdata2015jssdkcross=%7B%22distinct_id%22%3A%22708534123%22%2C%22%24device_id%22%3A%22167e46696c2228-0180aeab98c36-7623246e-1310720-167e46696c34c7%22%2C%22props%22%3A%7B%22%24latest_traffic_source_type%22%3A%22%E4%BB%98%E8%B4%B9%E5%B9%BF%E5%91%8A%E6%B5%81%E9%87%8F%22%2C%22%24latest_referrer%22%3A%22https%3A%2F%2Fwww.baidu.com%2Fbaidu.php%22%2C%22%24latest_referrer_host%22%3A%22www.baidu.com%22%2C%22%24latest_search_keyword%22%3A%22%E6%8B%9B%E8%81%98%22%2C%22%24latest_utm_source%22%3A%22baiduPC%22%2C%22%24latest_utm_medium%22%3A%22CPC%22%2C%22%24latest_utm_campaign%22%3A%22ty%22%2C%22%24latest_utm_content%22%3A%22pp%22%2C%22%24latest_utm_term%22%3A%228816174%22%7D%2C%22first_id%22%3A%22167e46696c2228-0180aeab98c36-7623246e-1310720-167e46696c34c7%22%7D; Hm_lvt_38ba284938d5eddca645bb5e02a02006=1545725177; Hm_lpvt_38ba284938d5eddca645bb5e02a02006=1545725737; GUID=0a469aabe588443a9772985c468b4024; LastCity=%E5%85%A8%E5%9B%BD; LastCity%5Fid=489; ZL_REPORT_GLOBAL={%22sou%22:{%22actionid%22:%2202fa523a-d440-4e6f-8523-370fcde002af-sou%22%2C%22funczone%22:%22smart_matching%22}%2C%22//jobs%22:{%22actionid%22:%2276ecb5aa-08ae-4808-87c4-2c395576d6aa-jobs%22%2C%22funczone%22:%22dtl_best_for_you%22}}; sts_evtseq=2; sts_sid=167e497dd49292-0026c135b69b38-7623246e-1310720-167e497dd4a58c",
    "Host": "sou.zhaopin.com",
    "Referer":"https://i.zhaopin.com/",
    "Upgrade-Insecure-Requests":"1"
}

def parse_detail_page(url):
    position = {}
    response = requests.get(url,proxies = PROXY,headers=HEADERS)
    html = etree.HTML(response.text)
    title = html.xpath("//td[@id='sharetitle']/text()")[0]
    tds = html.xpath("//tr[@class='c bottomline']/td")
    address = tds[0].xpath(".//text()")[1]
    category = tds[1].xpath(".//text()")[1]
    nums = tds[2].xpath(".//text()")[1]
    more_infos = html.xpath("//ul[@class='squareli']")
    duty = more_infos[0].xpath(".//text()")
    require = more_infos[1].xpath(".//text()")

    position['title'] = title
    position['address'] = address
    position['category'] = category
    position['nums'] = nums
    position['duty'] = duty
    position['require'] = require
    return position


def get_detail_urls(url):
    response = requests.get(url,proxies = PROXY,headers=HEADERS)
    # print(response.url)   # 判断传入的URL
    text = response.text
    '''
    # ***将文件打印出来
    # print(text)
    # ***将文件写到文件里
    # with open('99_test//zhilian.html', 'w', encoding='utf-8') as fp:
    #     fp.write(response.content.decode('utf-8'))
    '''

    html = etree.HTML(text)
    links = html.xpath("//div[@class='contentpile__content__wrapper__item clearfix']/a/@href")
    # links = map(lambda url:BASE_DOMAIN+url,links)    # 此处无需添加基础域名
    print(len(links))       # 输出为0 因此无法在网页上获取每个职位的详细链接,说明源码中不存在
    return links

def spider():
    base_url = "https://sou.zhaopin.com/?p={}&jl=530&kw={}&kt=3"
    positions = []
    for x in range(0,5):
        url = base_url.format(x,KEYWORD)
        detail_urls = get_detail_urls(url)
        for detail_url in detail_urls:
            position = parse_detail_page(detail_url)
            positions.append(position)
            print("-----------------------------------------------------------------------------------------"
                  "-----------------------------------------------------------------------------------------")
            # print(position)
            for i in position:
                print(i,end=":")
                print(position[i])
    # print(positions)

if __name__ == '__main__':
    # spider()
    get_detail_urls("https://sou.zhaopin.com/?jl=530&kw=java&kt=3")  # 获取详细职位链接