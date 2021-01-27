from pymouse import PyMouse
import os
from shutil import copy
import io
import sys
from time import sleep
from pykeyboard import PyKeyboard

#path = input('输入源文件夹路径：')
#path_list = os.listdir(path)

def num(path):
   path_list.remove('.git')
   path_list.sort()        #按顺序排列文件夹

   return path,path_list

def copy(path,path_list):
   num(path)
   target = r'e:\\Homework\\Auto-Copy\\test'
   for filename in path_list:
      print(os.path.join(path,filename))
      shutil.copy(os.path.join(path, filename), target)        #复制到目标文件夹

def program():
   #app_dir = input ('输入未来教育程序位置:')
   app_dir = 'E:\\Tools\\Temp\\未来教育.exe'
   os.startfile(app_dir)

def bank1():
   m = PyMouse()
   k = PyKeyboard()
   m.move(478, 197)        #鼠标移动到 考试题库 的位置
   sleep(3)       #等待4秒，等待 未来教育 程序启动
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
   m.move(1484, 19)
   sleep(3)
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
   #
   #
   #
   #此处应有获取分数的函数调用
   #
   #
   #
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

#copy(path,path_list)
mark()