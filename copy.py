import os
import shutil
import io
import sys
from time import sleep

#path = input('输入源文件夹路径：')
path = r'E:\\KSWJJ\\Answers'
path_list = os.listdir(path)
temp_target = r'e:\\Homework\\Auto-Copy\\test\\temp'
temp_target_list = os.listdir(temp_target)
target = r'e:\Homework\Auto-Copy\test\result'

def num():
   path_list.sort()        #按顺序排列文件夹
   return path,path_list

def copy2temp(path,path_list,temp_target):
   #num()
   path_list.sort()
   for filename in path_list:
      if os.path.exists(temp_target):
         shutil.rmtree(temp_target)
      print(os.path.join(path,filename))
      shutil.copytree(os.path.join(path, filename), temp_target)        #复制文件夹到目标文件夹
      print (filename + '复制就位！')
      sleep(5)
      copy2result(temp_target,target)
      print ('复制到result成功')
      
def copy2result(temp_target,target): 
   #num()
   temp_target_list.sort()
   for filename in temp_target_list:
      shutil.copy(os.path.join(temp_target, filename), target)

copy2temp(path,path_list,temp_target)

