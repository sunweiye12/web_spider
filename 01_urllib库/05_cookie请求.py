#encoding: utf-8

# 大鹏董成鹏主页：http://www.renren.com/880151247/profile
# 人人网登录url：http://www.renren.com/PLogin.do

from urllib import request
# from bs4 import BeautifulSoup

'''当你登录到一个网站的时候,这个网站就会将你的信息已cookie的方式返回到你的浏览器中,下次浏览器访问此网站(携带cookie),就不用重新登录'''

# 1. 不使用cookie去请求大鹏的主页
dapeng_url = "http://www.renren.com/880151247/profile"
headers = {
    'User-Agent':"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/62.0.3202.94 Safari/537.36",
    "Cookie":"anonymid=jpkyssjd-c4jm3c; depovince=BJ; _r01_=1; JSESSIONID=abceZ5dbyKtn3aKeaUHEw; ick_login=9ac7c38d-3f2f-4b7c-9ea7-f4c020b579ec; t=63fdff89c8773a5be8a363607ea75c4a4; societyguester=63fdff89c8773a5be8a363607ea75c4a4; id=969093794; xnsid=5e2d976b; jebecookies=4c7cfc8b-f075-4c88-9c39-3a55697c31c9|||||; ver=7.0; loginfrom=null; jebe_key=7e7bb028-3117-403b-a5e3-15caf7265368%7C52cd80d5302f54f641c624f72a65595c%7C1544608184570%7C1%7C1544608187630; wp_fold=0"
}
req = request.Request(url=dapeng_url,headers=headers)
resp = request.urlopen(req)

# 将读取到的数据写到99_test/renren.html文件中       ---   request.urlretrieve方法中只能加url 不能加Request修饰后的req
with open('99_test//0_renren.html','w',encoding='utf-8') as fp:
    # write函数必须写入一个str的数据类型
    # resp.read()读出来的是一个bytes数据类型
    # bytes -> decode -> str (将下载下来的源码解码成字符串)
    # str -> encode -> bytes (将字符串写入到新的文件中,并编码为源码)
    fp.write(resp.read().decode('utf-8'))


'''
 "Cookie":"anonymid=jacdwz2x-8bjldx; depovince=GW; _r01_=1; _ga=GA1.2.1455063316.1511436360; "
             "_gid=GA1.2.862627163.1511436360; wp=1; JSESSIONID=abcrs0queAwRp_sk9dS-v; ch_id=10016; "
             "jebecookies=c68b9b55-b6a1-4661-8d11-832862cfa246|||||; ick_login=7e3299f4-1e31-4455-b2a4-e5317c9e2ccf; "
             "_de=EA5778F44555C091303554EBBEB4676C696BF75400CE19CC; p=a96969b7912d80d95127b7935c1b729e1; "
             "first_login_flag=1; ln_uact=970138074@qq.com; "
             "ln_hurl=http://hdn.xnimg.cn/photos/hdn121/20170428/1700/main_nhiB_aebd0000854a1986.jpg; "
             "t=4d2ccb81ee83a6b1d3925b94779d22e21; societyguester=4d2ccb81ee83a6b1d3925b94779d22e21; "
             "id=443362311; xnsid=13bf03ea; loginfrom=syshome; "
             "jebe_key=9c062f5a-4335-4a91-bf7a-970f8b86a64e%7Ca022c303305d1b2ab6b5089643e4b5de%7C1511449232839%7C1; wp_fold=0"
'''