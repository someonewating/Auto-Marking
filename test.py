# -*- coding:utf-8 -*-
 
# Author : MaYi
# Blog  : http://www.cnblogs.com/mayi0312/
# Date  : 2020-03-02
# Name  : test_ocr
# Software : PyCharm
# Note  : 用Python开发截图识别OCR小工具
#import keyboard # 用于监控键盘按下，触发事件（pip install keyboard）
import time
from aip import AipOcr # 调用百度接口（pip install baidu-aip）
 
 
# 百度识别接口配置信息
APP_ID = '23595421'
API_KEY = 'Gtka59iMG4IIise8hdWiBswG'
SECRET_KEY = 'p1MnOAgTj5x1NoSLO2COVoLckQmhyBfW'

# 利用百度API识别截图中的文字
client = AipOcr(APP_ID, API_KEY, SECRET_KEY)
with open("E:/Images/2020-12-31 172209.png", 'rb') as f:
    image = f.read()
# 调用百度API通用文字识别（高精度版），提取图片中的内容
    text = client.basicAccurate(image)
    result = text["words_result"]
    for i in result:
        print(i["words"])
# 我是分隔线
print("-" * 50)