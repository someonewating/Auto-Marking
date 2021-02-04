import json
import os

x1 = input('输入“考试题库”的x坐标:')
y1 = input('输入“考试题库”的y坐标:')
d = {'x1':x1,'y1':y1}
d = str(d)
print (d)
#os.system('pause')

with open ('position.json','w+') as f_file:
    json.dump(d,f_file)
print ('success')

with open ('position.json','r',encoding='utf-8') as f_file:
    json.load(f_file)
x1 = d['x1']
print (x1)
