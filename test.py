from pymouse import PyMouse

m = PyMouse()
print('点击回车查看当前鼠标的坐标')
d = {}
while True:
    for i in range(0,5):
        _ = input()         # input起到阻塞程序的作用
        print(m.position())  # 获取当前鼠标指针的坐标
        a = m.position()
        d[i] = a
        print (i)
    print (d)