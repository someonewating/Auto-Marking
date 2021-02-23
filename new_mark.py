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

user_pos_dic = {}
global filename
filename = 0
filename = str(filename)
global app_dir
app_dir_dic = input ('输入未来教育程序位置:')
app_dir = str(app_dir_dic) + str('\\未来教育.exe')

def mark():
    judg_status()

def program():

    try:
        os.startfile(app_dir)
    except Exception:
        print('未来教育路径不正确，请更正路径或确认程序名称为‘未来教育.exe’')
        sys.exit()

def judg_status():
    global user_pos_dic
    print('是否为第一次运行？' + '\n')
    print('1.是' + '\n')
    print('2.否' + '\n')
    print('请选择(输入‘1’或‘2’)：')
    t = input()
    t = int(t)
    if t == 2:
        with open ('position.json','r') as f_file:
            user_pos_dic = json.load(f_file)
        user_pos_dic = dict(user_pos_dic)
        get_position.choice_pos()
        return user_pos_dic
    elif t == 1:
      program()
      get_position.user_pos()

class file_ope:

    path = input('输入源文件夹路径：')
    temp_target = r'Temp\\'
    target = r'e:\\KSWJJ\\65000001'

    def copy_temp(self,path,temp_target,target):

        global filename

        path_list = os.listdir(path)        #path_list:读取path中存在的所有文件或文件夹的名称
        path_list.sort()        #对path_list进行排序
        for filename in path_list:       #循环：按filename对path_list中所有文件进行遍历
            program()
            general_click.gen_1()
            try:
                general_click.gen_2()
            except Exception:
                print('general_click.gen_2()发生了错误.')
            if os.path.exists(temp_target):        #如果temp_target存在
                shutil.rmtree(temp_target)       #删除
            print(os.path.join(path,filename))
            shutil.copytree(os.path.join(path, filename), temp_target)        #复制文件夹到目标文件夹
            print (filename + '复制就位！')
            file_ope.copy_result(temp_target, target)
            print (filename + '复制到result成功')
            general_click.gen_3()
        return filename

    def copy_temp_once_click(self,path,temp_target,target):

        global filename

        path_list = os.listdir(path)        #path_list:读取path中存在的所有文件或文件夹的名称
        path_list.sort()        #对path_list进行排序
        for filename in path_list:       #循环：按filename对path_list中所有文件进行遍历
            program()
            general_click.gen_1()
            general_click.slid_click()
            try:
                general_click.gen_2()
            except Exception:
                print('general_click.gen_2()发生了错误.')
            if os.path.exists(temp_target):        #如果temp_target存在
                shutil.rmtree(temp_target)       #删除
            print(os.path.join(path,filename))
            shutil.copytree(os.path.join(path, filename), temp_target)        #复制文件夹到目标文件夹
            print (filename + '复制就位！')
            file_ope.copy_result(temp_target, target)
            print (filename + '复制到result成功')
            general_click.gen_3()
        return filename

    def copy_temp_double_click(self,path,temp_target,target):
        
        global filename

        path_list = os.listdir(path)        #path_list:读取path中存在的所有文件或文件夹的名称
        path_list.sort()        #对path_list进行排序
        for filename in path_list:       #循环：按filename对path_list中所有文件进行遍历
            program()
            general_click.gen_1()
            general_click.slid_double_click()
            try:
                general_click.gen_2()
            except Exception:
                print('general_click.gen_2()发生了错误.')
            if os.path.exists(temp_target):        #如果temp_target存在
                shutil.rmtree(temp_target)       #删除
            print(os.path.join(path,filename))
            shutil.copytree(os.path.join(path, filename), temp_target)        #复制文件夹到目标文件夹
            print (filename + '复制就位！')
            file_ope.copy_result(temp_target, target)
            print (filename + '复制到result成功')
            general_click.gen_3()
        return filename

    def copy_result(self,temp_target,target): 
        temp_target_list = os.listdir(temp_target)
        temp_target_list.sort()
        for filename in temp_target_list:
            shutil.copy(os.path.join(temp_target, filename), target)

    '''以上两个函数是为了防止filename错误的传递导致遍历无法成功进行。第一个filename是对源文件夹中文件夹名称的遍历；第二个
filename是对临时文件夹中文件（即是将要直接提供给 阅卷程序 批阅的文件）进行遍历。'''

    def ocr(self,filename):

        global user_pos_dic

        #使用win10自带的截屏工具对分数区域进行截屏
        m = PyMouse()
        k = PyKeyboard()

        k.press_key(k.control_l_key)        #PyMouse库中对左侧Windows键的命名
        sleep(1)

        k.press_key(k.alt_l_key)
        sleep(1)

        k.tap_key('a')
        sleep(1)

        m.move(user_pos_dic['x8'], user_pos_dic['y8'])
        m.press(user_pos_dic['x8'], user_pos_dic['y8'],button=1)       #截屏。从成绩信息的左上角开始
        sleep(1)

        m.move(user_pos_dic['x9'], user_pos_dic['y9'])
        m.release(user_pos_dic['x9'], user_pos_dic['y9'],button=1)        #截屏。到成绩信息的右下角结束
        sleep(1)

        k.release_key(k.windows_l_key)
        sleep(1)

        k.release_key(k.shift_key)
        sleep(1)

        k.press_key(k.enter_key)
        sleep(1)
        k.release_key(k.enter_key)

        try:

            #使用PIL的ImageGrab从剪贴板中保存存储的图片
            image = ImageGrab.grabclipboard()
            image.save("images/screen.png")

        except Exception:
            print('截图保存失败。确认截图快捷键是否为‘ctrl’+‘alt’+‘a’。')
            sys.exit()

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

class get_position:

    def user_pos(self):
        global user_pos_dic
        des_val = {'1' : '考试题库','2' : '真考题库试卷X','3' : '字处理',
        '4' : '考生文件夹','5' : '叉号','6' : '交卷',
        '7' : '确定','8' : '分数区域左上角','9' : '分数区域右下角',
        '10' : '当前窗口关闭按钮','11' : '新窗口关闭按钮'}
        user_pos_x = {}
        user_pos_y = {}
        m = PyMouse()
        for i in range(1,12):       #需要7次
            i = str(i)
            print('点击回车以确认 ' + des_val[i] + ' 的坐标. . . ')
            _ = input()         # input起到阻塞程序的作用
            t = m.position()
            t = tuple(t)
            user_pos_x[i] = t[0]
            user_pos_y[i] = t[1]
            t = str(t)
            print (des_val[i] + ' 的坐标是:' + t + '\n')
            with open('位置信息.txt','a',encoding='utf-8') as f:
                f.write('第' + i + '次时在' + des_val[i] + '处确认了一个坐标' + '\n')
        user_pos_dic = {'x1' : user_pos_x['1'],'y1' : user_pos_y['1'],'x2' : user_pos_x['2'],'y2' : user_pos_y['2'],
        'x3' : user_pos_x['3'],'y3' : user_pos_y['3'],'x4' : user_pos_x['4'],'y4' : user_pos_y['4'],
        'x5' : user_pos_x['5'],'y5' : user_pos_y['5'],'x6' : user_pos_x['6'],'y6' : user_pos_y['6'],
        'x7' : user_pos_x['7'],'y7' : user_pos_y['7'],'x8' : user_pos_x['8'],'y8' : user_pos_y['8'],
        'x9' : user_pos_x['9'],'y9' : user_pos_y['9'],'x10' : user_pos_x['10'],'y10' : user_pos_y['10'],
        'x11' : user_pos_x['11'],'y11' : user_pos_y['11']}
        with open ('position.json','w+') as f_file:
            json.dump(user_pos_dic,f_file)
        get_position.choice_pos()
        return user_pos_dic

    def slid_click(self):

        m = PyMouse()

        with open ('position2','r') as f_file:
            user_pos_dic_2 = json.load(f_file)

        user_pos_dic_2 = dict(user_pos_dic_2)
        m.move(user_pos_dic_2['x12'], user_pos_dic_2['y12'])
        sleep(1)
        m.click(user_pos_dic_2['x12'], user_pos_dic_2['y12'])

    def choice_pos(self):
        print('所选题库位于第一页、第二页还是第三页？')
        print('1.第一页')
        print('2.第二页')
        print('3.第三页')
        print('请选择(输入‘1’或‘2’或‘3’)：')
        t = input()
        if int(t) == 1:
            file_ope.copy_temp(file_ope.path,file_ope.temp_target,file_ope.target)
        elif int(t) == 2:
            print('在右侧滚动条底部回车以确认坐标')
            m = PyMouse()
            _ = input()         # input起到阻塞程序的作用
            t = m.position()
            t = tuple(t)
            x12 = t[0]
            y12 = t[1]
            user_pos_dic_2 = {'x12' : x12,'y12' : y12}
            with open ('position2.json','w+') as f_file:
                json.dump(user_pos_dic_2,f_file)
            file_ope.copy_temp_once_click(file_ope.path,file_ope.temp_target,file_ope.target)
        elif int(t) == 3:
            print('在右侧滚动条底部回车以确认坐标')
            m = PyMouse()
            _ = input()         # input起到阻塞程序的作用
            t = m.position()
            t = tuple(t)
            x12 = t[0]
            y12 = t[1]
            user_pos_dic_2 = {'x12' : x12,'y12' : y12}
            with open ('position2.json','w+') as f_file:
                json.dump(user_pos_dic_2,f_file)
            file_ope.copy_temp_double_click(file_ope.path,file_ope.temp_target,file_ope.target)

class general_click:

    def gen_1(self):

        global user_pos_dic

        m = PyMouse()

        print(user_pos_dic)
        sleep(6)       #等待3秒，等待程序启动 
        m.move(user_pos_dic.get('x1'), user_pos_dic.get('y1'))
        m.click(user_pos_dic.get('x1'), user_pos_dic.get('y1'))       #在 考试题库 处左键单击
        a = m.position()
        print ('在“考试题库”处单击一次，坐标:' + str(a))
        sleep(2)
    
    def gen_2(self):
        m = PyMouse()

        m.move(user_pos_dic['x2'], user_pos_dic['y2'])
        m.click(user_pos_dic['x2'], user_pos_dic['y2'])       #在 真考题库试卷1 处左键单击
        a = m.position()
        print ('在“真考题库试卷X”处单击一次，坐标:'+ str(a))
        sleep(4)

        m.move(user_pos_dic['x3'], user_pos_dic['y3'])
        m.click(user_pos_dic['x3'], user_pos_dic['y3'])
        a = m.position()
        print ('在“字处理”处单击一次，坐标:'+ str(a))
        sleep(1)

        m.move(user_pos_dic['x4'], user_pos_dic['y4'])
        m.click(user_pos_dic['x4'], user_pos_dic['y4'])
        a = m.position()
        print ('在“考生文件夹”处单击一次，坐标:'+ str(a))
        sleep(3)

        m.move(user_pos_dic['x5'], user_pos_dic['y5'])
        m.click(user_pos_dic['x5'], user_pos_dic['y5'])
        a = m.position()
        print ('在“叉号”处点击一次，坐标:'+ str(a))
        sleep(1)

    def gen_3(self):
        m = PyMouse()
        k = PyKeyboard()

        m.move(user_pos_dic['x6'], user_pos_dic['y6'])
        m.click(user_pos_dic['x6'], user_pos_dic['y6'])
        a = m.position()
        print ('在“交卷”处单击一次，坐标:'+ str(a))
        sleep(1)

        m.move(user_pos_dic['x7'], user_pos_dic['y7'])
        m.click(user_pos_dic['x7'], user_pos_dic['y7'])
        a = m.position()
        print ('在“确定”处单击一次，坐标:'+ str(a))
        k.tap_key(k.enter_key)
        sleep(1)

        k.tap_key(k.enter_key)
        sleep(1)

        #可能出现1-4个确认窗口

        #第一个
        k.tap_key('y')
        sleep(1)
        #第二个
        sleep(1)
        k.tap_key('y')
        #第三个
        sleep(1)
        k.tap_key('y')
        #第四个
        sleep(1)
        k.tap_key('y')

        file_ope.ocr(filename)

        sleep(2)
        m.move(user_pos_dic['x10'], user_pos_dic['y10'])
        m.click(user_pos_dic['x10'], user_pos_dic['y10'])
        a = m.position()
        print ('在‘叉号’处单击一次，坐标:'+ str(a))

        sleep(4)
        m.move(user_pos_dic['x11'], user_pos_dic['y11'])
        m.click(user_pos_dic['x11'], user_pos_dic['y11'])
        a = m.position()
        print ('在退出程序处的‘叉号’处单击一次，坐标:'+ str(a))        #退出程序，等待下一轮循环

    def slid_click(self):

        m = PyMouse()

        with open ('position2.json','r') as f_file:
            user_pos_dic_2 = json.load(f_file)

        user_pos_dic_2 = dict(user_pos_dic_2)
        m.move(user_pos_dic_2['x12'], user_pos_dic_2['y12'])
        sleep(1)
        m.click(user_pos_dic_2['x12'], user_pos_dic_2['y12'])

    def slid_double_click(self):
        m = PyMouse()

        with open ('position2.json','r') as f_file:
            user_pos_dic_2 = json.load(f_file)

        user_pos_dic_2 = dict(user_pos_dic_2)
        m.move(user_pos_dic_2['x12'], user_pos_dic_2['y12'])
        sleep(1)
        m.click(user_pos_dic_2['x12'], user_pos_dic_2['y12'])
        sleep(1)
        m.click(user_pos_dic_2['x12'], user_pos_dic_2['y12'])

get_position = get_position()
general_click = general_click()
file_ope = file_ope()

try:
    mark()
except Exception:
    sys.exit()
