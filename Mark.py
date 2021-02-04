from pymouse import PyMouse
from PIL import ImageGrab
from aip import AipOcr
from time import sleep
from pykeyboard import PyKeyboard
import shutil
import os
import io
import sys
import json

#path = input('输入源文件夹路径：')
path = r'E:\\KSWJJ\\Answers'
temp_target = r'e:\\Homework\\Auto-Marking\\Temp'
target = r'e:\\KSWJJ\\65000001'
filename = 0
filename = str(filename)
x1,x2,x3,x4,x5,x6,x7,x8,x9,x10,x11 = 0,0,0,0,0,0,0,0,0,0,0
y1,y2,y3,y4,y5,y6,y7,y8,y9,y10,y11 = 0,0,0,0,0,0,0,0,0,0,0
d = {}

def mark():
   #user_position()
   judg_status()
   copy_temp(path,temp_target)

def copy_temp(path,temp_target):
   path_list = os.listdir(path)        #path_list:读取path中存在的所有文件或文件夹的名称
   path_list.sort()        #对path_list进行排序
   global filename
   for filename in path_list:       #循环：按filename对path_list中所有文件进行遍历
      program()
      bank1()
      if os.path.exists(temp_target):        #如果temp_target存在
         shutil.rmtree(temp_target)       #删除
      print(os.path.join(path,filename))
      shutil.copytree(os.path.join(path, filename), temp_target)        #复制文件夹到目标文件夹
      print (filename + '复制就位！')
      copy_result(temp_target,target)
      print (filename + '复制到result成功')
      bank_general()
   return filename

def copy_result(temp_target,target): 
   temp_target_list = os.listdir(temp_target)
   temp_target_list.sort()
   for filename in temp_target_list:
      shutil.copy(os.path.join(temp_target, filename), target)
'''以上两个函数是为了防止filename错误的传递导致遍历无法成功进行。第一个filename是对源文件夹中文件夹名称的遍历；第二个
filename是对临时文件夹中文件（即是将要直接提供给 阅卷程序 批阅的文件）进行遍历。'''
def program():
   #app_dir = input ('输入未来教育程序位置:')
   app_dir = 'E:\\Tools\\Temp\\未来教育.exe'
   os.startfile(app_dir)

def ocr(filename):
#使用win10自带的截屏工具对分数区域进行截屏
   m = PyMouse()
   k = PyKeyboard()
   k.press_key(k.control_l_key)        #PyMouse库中对左侧Windows键的命名
   sleep(0.5)
   k.press_key(k.alt_l_key)
   sleep(0.5)
   k.tap_key('a')
   sleep(0.5)
   m.press(x10, y10,button=1)       #截屏。从成绩信息的左上角开始
   sleep(0.5)
   m.release(x11, y11,button=1)        #截屏。到成绩信息的右下角结束
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
   for i in result:
      temp = i["words"]
   print (temp)

#将结果写入文档
   with open('result.txt','a',encoding='utf-8') as f:
      f.write(filename +',' + temp + '\n')

def bank1():
   m = PyMouse()
   m.move(x1, y1)        #鼠标移动到 考试题库 的位置
   sleep(3)       #等待3秒，等待 未来教育 程序启动
   m.click(x1, y1)       #在 考试题库 处左键单击
   a = m.position()
   a = str(a)
   print ('在“考试题库”处单击一次，坐标:'+a)
   m.move(x2, y2)        #鼠标移动到 真考题库试卷1 的位置
   sleep(0.5)
   m.click(x2, y2)       #在 真考题库试卷1 处左键单击
   a = m.position()
   a = str(a)
   print ('在“真考题库试卷1”处单击一次，坐标:'+a)
   m.move(x3, y3)
   sleep(2)
   m.click(x3, y3)
   a = m.position()
   a = str(a)
   print ('在“字处理”处单击一次，坐标:'+a)
   m.move(x4, y4)
   sleep(1)
   m.click(x4, y4)
   a = m.position()
   a = str(a)
   print ('在“考生文件夹”处单击一次，坐标:'+a)
   m.move(x5, y5)
   sleep(1)
   m.click(x5, y5)
   a = m.position()
   a = str(a)
   print ('在“叉号”处点击一次，坐标:'+a)
   sleep(0.5)

def bank_general():        
   m = PyMouse()
   k = PyKeyboard()
   m.move(x6, y6)
   sleep(0.5)
   m.click(x6, y6)
   a = m.position()
   a = str(a)
   print ('在“交卷”处单击一次，坐标:'+a)
   m.move(x7, y7)
   sleep(0.5)
   m.click(x7, y7)
   a = m.position()
   a = str(a)
   print ('在“确定”处单击一次，坐标:'+a)
   k.tap_key(k.enter_key)
   sleep(0.5)
   k.tap_key(k.enter_key)

#可能出现1-4个确认窗口
   #第一个
   sleep(0.5)
   k.tap_key('y')
   #第二个
   sleep(0.5)
   k.tap_key('y')
   #第三个
   sleep(0.5)
   k.tap_key('y')
   sleep(0.5)
   k.tap_key('y')

#对分数区域识别并返回结果
   ocr(filename)
   m.move(x8, y8)
   sleep(1)
   m.click(x8, y8)
   a = m.position()
   a = str(a)
   print ('在‘叉号’处单击一次，坐标:'+a)

   m.move(x9, y9)
   sleep(2)
   m.click(x9, y9)
   a = m.position()
   a = str(a)
   print ('在退出程序处的‘叉号’处单击一次，坐标:'+a)        #退出程序，等待下一轮循环

def user_position1():
   global x1,y1,x2,y2,x3,y3,x4,y4,x5,y5,x6,y6,x7,y7,x8,y8,x9,y9,x10,y10,x11,y11
   m = PyMouse()
   print('点击回车以确认当前鼠标的所在位置的坐标')
   for i in range(1,8):       #需要7次
      i = str(i)
      _ = input()         # input起到阻塞程序的作用
      a = m.position()
      a = str(a)
      print ('第' + i + '次时在' + a + '处确认了一个坐标')
      with open('位置信息.txt','a',encoding='utf-8') as f:
         f.write('第' + i + '次时在' + a + '处确认了一个坐标' + '\n')
   print('依照‘位置信息.txt’内存储的数据依次输入数据。' +'\n')
   os.system('pause')
   x1 = input('输入“考试题库”的x坐标:')
   y1 = input('输入“考试题库”的y坐标:')
   x2 = input('输入“真考题库试卷X”的x坐标:')
   y2 = input('输入“真考题库试卷X”的y坐标:')
   x3 = input('输入“字处理”的x坐标:')
   y3 = input('输入“字处理”的y坐标:')
   x4 = input('输入“考生文件夹”的x坐标:')
   y4 = input('输入“考生文件夹”的y坐标:')
   x5 = input('输入“考生文件夹”窗口左上角关闭按钮的x坐标:')
   y5 = input('输入“考生文件夹”窗口左上角关闭按钮的y坐标:')
   x6 = input('输入“交卷”的x坐标:')
   y6 = input('输入“交卷”的y坐标:')
   x7 = input('输入“确定”的x坐标:')
   y7 = input('输入“确定”的y坐标:')
   x10 = input('输入截屏左上角的x坐标:')
   y10 = input('输入截屏左上角的y坐标:')
   x11 = input('输入截屏右下角的x坐标:')
   y11 = input('输入截屏右下角的y坐标:')
   x8 = input('输入“关闭”按钮的x坐标:')
   y8 = input('输入“关闭”按钮的y坐标:')
   x9 = input('输入新的窗口中“关闭”按钮的x坐标:')
   y9 = input('输入新的窗口中“关闭”按钮的y坐标:')
   print ('坐标信息捕获成功' )
   d = {'x1' : x1,'y1' : y1,'x2' : x2,'y2' : y2,'x3' : x3,'y3' : y3,'x4' : x4 ,'y4' : y4,
   'x5' : x5,'y5' : y5,'x6' : x6,'y6' : y6,'x7' : x7,'y7' : y7,'x8' : x8,'y8' : y8,
   'x9' : x9,'y9' : y9,'x10' : x10,'y10' : y10,'x11' : x11,'y11' : y11}
   with open ('position.json','w+') as f_file:
      json.dump(d,f_file)
   str2int()
   return x1,y1,x2,y2,x3,y3,x4,y4,x5,y5,x6,y6,x7,y7,x8,y8,x9,y9,x10,y10,x11,y11,d
def judg_status():
   global x1,y1,x2,y2,x3,y3,x4,y4,x5,y5,x6,y6,x7,y7,x8,y8,x9,y9,x10,y10,x11,y11,d
   print('是否为第一次运行？‘位置信息.txt’内的位置信息是否正确？' + '\n')
   print('1.一切正确' + '\n')
   print('2.仍需检查' + '\n')
   print('请选择(输入‘1’或‘2’)：')
   t = input()
   t = int(t)
   if t == 1:
      with open ('position.json','r') as f_file:
         d = json.load(f_file)
      d = str(d)
      print (d)
      d = eval(d)
      os.system('pause')
      x1 = d['x1']
      y1 = d['y1']
      x2 = d['x2']
      y2 = d['y2']

      x3 = d['x3']
      y3 = d['y3']
      x4 = d['x4']
      y4 = d['y4']

      x5 = d['x5']
      y5 = d['y5']
      x6 = d['x6']
      y6 = d['y6']

      x7 = d['x7']
      y7 = d['y7']
      x8 = d['x8']
      y8 = d['y8']

      x9 = d['x9']
      y9 = d['y9']
      x10 = d['x10']
      y10 = d['y10']

      x11 = d['x11']
      y11 = d['y11']
      str2int()
      return x1,y1,x2,y2,x3,y3,x4,y4,x5,y5,x6,y6,x7,y7,x8,y8,x9,y9,x10,y10,x11,y11
   elif t == 2:
      program()
      user_position1()

def str2int():
   global x1,y1,x2,y2,x3,y3,x4,y4,x5,y5,x6,y6,x7,y7,x8,y8,x9,y9,x10,y10,x11,y11
   x1 = int(x1)
   y1 = int(y1)
   x2 = int(x2)
   y2 = int(y2)

   x3 = int(x3)
   y3 = int(y3)
   x4 = int(x4)
   y4 = int(y4)

   x5 = int(x5)
   y5 = int(y5)
   x6 = int(x6)
   y6 = int(y6)

   x7 = int(x7)
   y7 = int(y7)
   x8 = int(x8)
   y8 = int(y8)

   x9 = int(x9)
   y9 = int(y9)
   x10 = int(x10)
   y10 = int(y10)

   x11 = int(x11)
   y11 = int(y11)

mark()