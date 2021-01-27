from pymouse import PyMouse
from pykeyboard import PyKeyboard
'''
m = PyMouse()
a = m.position()    #获取当前坐标的位置
print(a)

m.move(31, 223)   #鼠标移动到(x,y)位置
a = m.position()
print(a)

m.click(31, 223)  #移动并且在(x,y)位置左击
'''

k = PyKeyboard()
print(dir(k))