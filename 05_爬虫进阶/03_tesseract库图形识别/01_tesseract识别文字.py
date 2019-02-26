# encoding: utf-8

import pytesseract
from PIL import Image

# 指定tesseract文件所在位置
pytesseract.pytesseract.tesseract_cmd = r"E:\Tesseract-OCR\tesseract.exe"

# 选择要识别的图片
image1 = Image.open(r'99_Test\a.png')
image2 = Image.open('99_Test\c.png')

# 利用本地的tesseract模块来识别图片中的文字
text1 = pytesseract.image_to_string(image=image1)
print(text1)

# 用来识别中文版文本(前提是在seseract库的tessdata下下载好了中文包)
text2 = pytesseract.image_to_string(image=image2,lang='chi_sim')
print(text2)
