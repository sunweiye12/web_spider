#encoding: utf-8

from lxml import etree
import requests

BASE_DOMAIN = 'http://dytt8.net'
HEADERS = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/61.0.3163.100 Safari/537.36',
    'Referer': 'http://www.dytt8.net/html/gndy/dyzz/list_23_1.html'
}

def get_detail_urls(url):
    response = requests.get(url, headers=HEADERS)
    # response.text
    # response.content
    # requests库，默认会使用自己猜测的编码方式将
    # 抓取下来的网页进行解码，然后存储到text属性上去
    # 在电影天堂的网页中，因为编码方式，requests库猜错了。所以就会产生乱码
    text = response.text
    html = etree.HTML(text)
    detail_urls = html.xpath("//table[@class='tbspan']//a/@href")   # 返回一个列表
    detail_urls = map(lambda url:BASE_DOMAIN+url,detail_urls) # lambda url:BASE_DOMAIN+url 是一个函数,参数为url 操作为BASE_DOMAIN+url
    # 返回得到的还是一个列表元素
    return detail_urls

def parse_detail_page(url):
    movie = {}
    response = requests.get(url,headers=HEADERS)
    text = response.content.decode('gbk')
    html = etree.HTML(text)
    title = html.xpath("//div[@class='title_all']//font[@color='#07519a']/text()")[0]
    movie['title'] = title

    zoomE = html.xpath("//div[@id='Zoom']")[0]
    imgs = zoomE.xpath(".//img/@src")
    cover = imgs[0]         # 封面图片
    screenshot = imgs[1]    # 预告图片
    # 将提取的信息添加到字典中
    movie['cover'] = cover
    movie['screenshot'] = screenshot

    def parse_info(info,rule):      # 去掉多余的字符串
        return info.replace(rule,"").strip()

    infos = zoomE.xpath(".//text()")
    for index,info in enumerate(infos):
        # print(info)
        # print(index)
        # print('='*30)
        if info.startswith("◎年　　代"):
            info = parse_info(info,"◎年　　代")     # 去掉  ◎年　　代
            movie['year'] = info
        elif info.startswith("◎产　　地"):
            info = parse_info(info,"◎产　　地")
            movie['country'] = info
        elif info.startswith("◎类　　别"):
            info = parse_info(info,"◎类　　别")
            movie['category'] = info
        elif info.startswith("◎豆瓣评分"):
            info = parse_info(info,"◎豆瓣评分")
            movie['douban_rating'] = info
        elif info.startswith("◎片　　长"):
            info = parse_info(info,"◎片　　长")
            movie['duration'] = info
        elif info.startswith("◎导　　演"):
            info = parse_info(info,"◎导　　演")
            movie['director'] = info
        # elif info.startswith("◎主　　演"):
        #     info = parse_info(info,"◎主　　演")
        #     actors = [info]
        #     for x in range(index+1,len(infos)):
        #         actor = infos[x].strip()
        #         if actor.startswith("◎"):
        #             break
        #         actors.append(actor)
        #     movie['actors'] = actors
        elif info.startswith("◎简　　介"):
            info = parse_info(info,"◎简　　介")

            for x in range(index+1,len(infos)):
                if infos[x].strip() != None:
                    profile = infos[x].strip()
                    movie["profile"] = profile
                    break

    download_url = html.xpath("//td[@bgcolor='#fdfddf']/a/@href")[0]
    movie['download_url'] = download_url
    return movie

def spider():
    base_url = "http://dytt8.net/html/gndy/dyzz/list_23_{}.html"
    movies = []
    for x in range(1,8):    # range为[1,7]
        # 第一个for循环，是用来控制总共有7页的
        url = base_url.format(x)        # 将数字添加到{}中
        detail_urls = get_detail_urls(url)    # 通过函数,得到此页面所有电影的详情连接`
        for detail_url in detail_urls:
            # 第二个for循环，是用来遍历一页中所有电影的详情url
            movie = parse_detail_page(detail_url)
            movies.append(movie)
            print("-------------------------------------------------------------------------------"
                  "------------------------------------------------------------------------------")
            for i in movie:     # 打印每个电影的信息
                print(i+":"+movie[i])

    # print(movies)

if __name__ == '__main__':
    spider()
