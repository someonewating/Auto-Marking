from aip import AipOcr # 调用百度接口（pip install baidu-aip）
from PIL import ImageGrab
import pykeyboard
import pymouse
from time import sleep
'''
a = pymouse()
k = pykeyboard()
k.press_key(k.windows_key)
sleep(0.5)
k.press_key(k.shift_key)
sleep(0.5)
k.tap_key(k.s_key)
sleep(0.5)
k.tap_key(k.enter_key)
a.click(582, 183)
a.click(720, 224)
'''

APP_ID = '23595421'
API_KEY = 'Gtka59iMG4IIise8hdWiBswG'
SECRET_KEY = 'p1MnOAgTj5x1NoSLO2COVoLckQmhyBfW '

image = ImageGrab.grabclipboard()
image.save("screen.png")
image = ImageGrab.grabclipboard()
image.save("screen.png")
 
 # 3、利用百度API识别截图中的文字
client = AipOcr(APP_ID, API_KEY, SECRET_KEY)
with open("screen.png", 'rb') as f:
image = f.read()
  # 调用百度API通用文字识别（高精度版），提取图片中的内容
text = client.basicAccurate(image)
result = text["words_result"]
for i in result:
    print(i["words"])