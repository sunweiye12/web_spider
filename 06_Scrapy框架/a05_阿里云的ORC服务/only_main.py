#encoding: utf-8

##  **************使用淘宝的orc引擎实现的图像验证码识别************************

import urllib.request
import urllib.parse
import requests
import json
import time
import base64

with open('b.png', 'rb') as f:  # 以二进制读取本地图片
    data = f.read()
    encodestr = str(base64.b64encode(data),'utf-8')

#请求头
headers = {
         'Authorization': 'APPCODE ' + 'cbd1933b9f69482382c62701085bba2a', # 用于识别身份的APPCODE
         'Content-Type': 'application/json; charset=UTF-8'
    }
def posturl(url,data={}):
  try:
    params=json.dumps(dict).encode(encoding='utf-8')    # 将字典对象转化成json
    response = requests.post(url, data=params, headers=headers)
    result = response.json()    # 返回json对象
    return result               # 返回json对象
  except urllib.error.HTTPError as e:
      print(e.code)
      print(e.read().decode("utf-8"))
  time.sleep(1)

if __name__=="__main__":
    # 引擎调用地址
    url_request="https://ocrapi-ecommerce.taobao.com/ocrservice/ecommerce"
    # 图片解析后的编码
    dict = {'img': encodestr}
    # 调用方法来解析
    html = posturl(url_request, data=dict)

    # 打印解析结果
    print(html)         # 如果返回401说明没有获得权限

    print("="*80)
    # 提取关键文字
    for i in html['prism_wordsInfo']:
        print(i['word'])
