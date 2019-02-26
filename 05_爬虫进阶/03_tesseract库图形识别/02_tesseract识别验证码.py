#encoding: utf-8

import pytesseract
from urllib import request # 用于将验证码加载到本地
from PIL import Image
import time

def main():
    pytesseract.pytesseract.tesseract_cmd = r"E:\Tesseract-OCR\tesseract.exe"
    url = "https://passport.lagou.com/vcode/create?from=register&refresh=1513082291955" # 网站中验证码的地址(每次刷新变一张)
    # 一直循环知道识别为止
    while True:
        request.urlretrieve(url,r'99_Test\captcha.png') # 将验证码保存到本地
        image = Image.open(r'99_Test\captcha.png')
        text = pytesseract.image_to_string(image)
        print(text)
        time.sleep(3)


if __name__ == '__main__':
    main()