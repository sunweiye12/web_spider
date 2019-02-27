#encoding: utf-8

from urllib import request
from base64 import b64encode
import requests
import json

# 验证码地址
captcha_url = 'https://passport.lagou.com/vcode/create?from=register&refresh=1513082291955'
# 下载图片验证码
request.urlretrieve(captcha_url,'captcha.png')

# 识别验证码的一个引擎地址(阿里云服务)
recognize_url = 'https://ocrapi-ecommerce.taobao.com/ocrservice/ecommerce'

formdata = {}
with open('captcha.png','rb') as fp:    # 以二进制读取本地图片
    data = fp.read()
    encodestr = str(b64encode(data), 'utf-8')
    formdata['img'] = encodestr

appcode = 'cbd1933b9f69482382c62701085bba2a'        # 购买服务后获得的appcode(用于身份识别)
# 请求头
headers = {
    'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
    'Authorization': 'APPCODE ' + appcode
}

# 发送请求
params=json.dumps(formdata).encode(encoding='utf-8')    # 将数据转化json格式
response = requests.post(recognize_url,data=params,headers=headers)
result = response.json()
code = result['prism_wordsInfo'][0]['word']
print(result)
print(code)
