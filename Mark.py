from pymouse import PyMouse
from PIL import ImageGrab
from aip import AipOcr
from time import sleep
from pykeyboard import PyKeyboard
import shutil
import os
import io
import sys

#path = input('输入源文件夹路径：')
path = r'E:\\KSWJJ\\Answers'
temp_target = r'e:\\Homework\\Auto-Marking\\Temp'
target = r'e:\\KSWJJ\\65000001'

def copy_temp(path,temp_target):
   path_list = os.listdir(path)
   path_list.sort()
   for filename in path_list:
      if os.path.exists(temp_target):
         shutil.rmtree(temp_target)
      print(os.path.join(path,filename))
      shutil.copytree(os.path.join(path, filename), temp_target)        #复制文件夹到目标文件夹
      print (filename + '复制就位！')
      sleep(0)
      copy_result(temp_target,target)
      print (filename + '复制到result成功')

def copy_result(temp_target,target): 
   temp_target_list = os.listdir(temp_target)
   temp_target_list.sort()
   for filename in temp_target_list:
      shutil.copy(os.path.join(temp_target, filename), target)

def program():
   #app_dir = input ('输入未来教育程序位置:')
   app_dir = 'E:\\Tools\\Temp\\未来教育.exe'
   os.startfile(app_dir)

def ocr():
#使用win10自带的截屏工具对分数区域进行截屏
   m = PyMouse()
   k = PyKeyboard()
   k.press_key(k.windows_l_key)
   sleep(0.5)
   k.press_key(k.shift_key)
   sleep(0.5)
   k.tap_key('s')
   sleep(0.5)
   m.press(582, 183,button=1)       #截屏。从成绩信息的左上角开始
   sleep(0.5)
   m.release(720, 224,button=1)        #截屏。到成绩信息的右下角结束
   sleep(0.5)
   k.release_key(k.windows_l_key)
   sleep(0.5)
   k.release_key(k.shift_key)
   sleep(0.5)

#使用PIL的ImageGrab从剪贴板中保存存储的图片
   image = ImageGrab.grabclipboard()
   image.save("images/screen.png")

#利用百度API识别截图中的文字
   APP_ID = '23595421'
   API_KEY = 'Gtka59iMG4IIise8hdWiBswG'
   SECRET_KEY = 'p1MnOAgTj5x1NoSLO2COVoLckQmhyBfW'
   client = AipOcr(APP_ID, API_KEY, SECRET_KEY)
   with open("images/screen.png", 'rb') as f:
      image = f.read()

#调用百度API通用文字识别(标准版),识别分数
   text = client.basicGeneral(image)
   result = text["words_result"]
   result = str(result)
   print (result)

   with open('result.txt','a',encoding='utf-8') as f:
      f.write(result + '\n')

def bank1():
   m = PyMouse()
   k = PyKeyboard()
   m.move(478, 197)        #鼠标移动到 考试题库 的位置
   sleep(3)       #等待3秒，等待 未来教育 程序启动
   m.click(478, 197)       #在 考试题库 处左键单击
   a = m.position()
   a = str(a)
   print ('在“考试题库”处单击一次，坐标:'+a)
   m.move(630, 310)        #鼠标移动到 真考题库试卷1 的位置
   sleep(0.5)
   m.click(630, 310)       #在 真考题库试卷1 处左键单击
   a = m.position()
   a = str(a)
   print ('在“真考题库试卷1”处单击一次，坐标:'+a)
   m.move(163, 120)
   sleep(2)
   m.click(163, 120)
   a = m.position()
   a = str(a)
   print ('在“字处理”处单击一次，坐标:'+a)
   m.move(1466, 146)
   sleep(1)
   m.click(1466, 146)
   a = m.position()
   a = str(a)
   print ('在“考生文件夹”处单击一次，坐标:'+a)
   m.move(1512, 10)
   sleep(1)
   m.click(1512, 10)
   a = m.position()
   a = str(a)
   print ('在“叉号”处点击一次，坐标:'+a)
   sleep(0.5)
#调用copy函数
   copy_temp(path,temp_target)

   m.move(1484, 19)
   sleep(0.5)
   m.click(1484, 19)
   a = m.position()
   a = str(a)
   print ('在“交卷”处单击一次，坐标:'+a)
   m.move(693, 670)
   sleep(0.5)
   m.click(693, 670)
   a = m.position()
   a = str(a)
   print ('在“确定”处单击一次，坐标:'+a)
   k.tap_key(k.enter_key)
   sleep(0.5)
   k.tap_key(k.enter_key)

#可能出现1-3个确认窗口
   #第一个
   sleep(0.5)
   k.tap_key('y')
   #第二个
   sleep(0.5)
   k.tap_key('y')
   #第三个
   sleep(0.5)
   k.tap_key('y')

#对分数区域识别并返回结果
   ocr()
   m.move(1146, 119)
   sleep(1)
   m.click(1146, 119)
   a = m.position()
   a = str(a)
   print ('在‘叉号’处单击一次，坐标:'+a)

   m.move(1198, 125)
   sleep(2)
   m.click(1198, 125)
   a = m.position()
   a = str(a)
   print ('在退出程序处的‘叉号’处单击一次，坐标:'+a)        #退出程序，等待下一轮循环

def mark():
   program()
   bank1()

mark()