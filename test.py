from pymouse import PyMouse
import os

m = PyMouse()
print('点击回车查看当前鼠标的坐标')
d = {}
#while True:
for i in range(0,2):
    i = str(i)
    _ = input()         # input起到阻塞程序的作用
    #print(m.position())  # 获取当前鼠标指针的坐标
    a = m.position()
    a = str(a)
    d[i] = a
    print ('第' + i + '次时在' + a + '处确认了一个坐标')
    os.system('pause')
d = str(d)
print ('存储在字典中的信息:' + d)
d = eval(d)
b1 = d['0']
print (b1)