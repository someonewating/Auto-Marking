from pymouse import PyMouse
import os
import shutil
import io
import sys

path = input('输入目标文件夹：')
path_list = os.listdir(path)

def num(path):
   path_list.remove('.git')
   path_list.sort()

   return path,path_list

def copy(path,path_list):
   num(path)
   target = r'e:\\Homework\\Auto-Copy\\test'
   for filename in path_list:
      print(os.path.join(path,filename))
      shutil.copy(os.path.join(path, filename), target)

copy(path,path_list)