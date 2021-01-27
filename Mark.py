from pymouse import PyMouse
import os
import shutil
import io
import sys

def copy():
   path = r'e:\\Homework\\Auto-Book'
   path_list = os.listdir(path)
   path_list.remove('.git')    # macos中的文件管理文件，默认隐藏，这里可以忽略
   path_list.remove('.gitattributes')
   path_list.sort()
   #print(path_list)
   target = r'e:\\Homework\\Auto-Copy\\test'
   for filename in path_list:
      print(os.path.join(path,filename))
      shutil.copy(os.path.join(path, filename), target)
copy()