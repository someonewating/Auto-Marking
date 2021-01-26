from pymouse import PyMouse
import os
import shutil
import io
import sys

def copy():
   source = input("Enter source file with full path: ")
   target = input("Enter target file with full path: ")
   shutil.copy(source, target)

copy()