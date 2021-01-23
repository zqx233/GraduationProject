import base64
import json
from tkinter import *
import tkinter.filedialog
import tkinter.messagebox
from tkinter import ttk

import requests
from PIL import Image
from PIL import ImageTk
import functions as fc


class Home(Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.master = master
        self.grid()
        # 标题组件
        self.title_label = Label(self.master, text='人脸识别系统', font=('', 20))
        # 按钮组件图标
        self.fun1_img = PhotoImage(file='src/img/face.png')
        self.fun2_img = PhotoImage(file='src/img/compare.png')
        self.fun3_img = PhotoImage(file='src/img/search.png')
        self.fun4_img = PhotoImage(file='src/img/detect.png')
        self.fun5_img = PhotoImage(file='src/img/about.png')
        # 按钮组件
        self.fun1_but = Button(self.master, width=140, height=130, text='人脸识别与属性分析', font=('', 12), image=self.fun1_img,
                               compound='top')
        self.fun2_but = Button(self.master, width=140, height=130, text='人脸对比', font=('', 12), image=self.fun2_img,
                               compound='top')
        self.fun3_but = Button(self.master, width=140, height=130, text='人脸搜索', font=('', 12), image=self.fun3_img,
                               compound='top')
        self.fun4_but = Button(self.master, width=140, height=130, text='图片活体检测', font=('', 12), image=self.fun4_img,
                               compound='top')
        self.fun5_but = Button(self.master, width=140, height=130, text='关于', font=('', 12), image=self.fun5_img,
                               compound='top')
        self.fun_zone = LabelFrame()
        # 布局
        # self.title_label.grid(row=1, column=1, padx=5, pady=20, columnspan=3)
        self.fun1_but.grid(row=2, column=2, padx=5, pady=10)
        self.fun2_but.grid(row=3, column=2, padx=5, pady=10)
        self.fun3_but.grid(row=4, column=2, padx=5, pady=10)
        self.fun4_but.grid(row=5, column=2, padx=5, pady=10)
        self.fun5_but.grid(row=6, column=2, padx=5, pady=10)
        # 按键绑定
        self.fun1_but.bind('<Button-1>', self.fun1_but_ev)
        self.fun2_but.bind('<Button-1>', self.fun2_but_ev)
        self.fun3_but.bind('<Button-1>', self.fun3_but_ev)
        self.fun4_but.bind('<Button-1>', self.fun4_but_ev)
        self.fun5_but.bind('<Button-1>', self.fun5_but_ev)

    def fun1_but_ev(self, event):  # 要加event参数才能被调用
        Face(master=self.master)

    def fun2_but_ev(self, event):
        FaceCompare(master=self.master)

    def fun3_but_ev(self, event):
        Face(master=self.master)

    def fun4_but_ev(self, event):
        Face(master=self.master)

    def fun5_but_ev(self, event):
        Face(master=self.master)


class Face(Frame):
    """功能1界面"""

    def __init__(self, master=None):
        super().__init__(master)
        self.master = master
        # 功能1窗口
        # self.fun1_win = Toplevel(master=self.master)
        # self.fun1_win.title('人脸识别与属性分析')
        # self.grid()
        self.fun1_win = LabelFrame(master=self.master, text='人脸识别与属性分析')
        self.fun1_win.grid(row=2, column=3, rowspan=5, padx=5, pady=5, sticky='n' + 's' + 'w' + 'e')
        # 识别结果部分
        self.result_frame = LabelFrame(master=self.fun1_win, text='识别结果', width=280)
        self.face_result_frame = Frame(master=self.result_frame, width=280)
        # 图片展示部分
        self.img_frame = LabelFrame(master=self.fun1_win, text='')
        self.up_img = PhotoImage(file='src/img/upload.png')
        self.img_label = Label(self.img_frame, width=680, height=400, image=self.up_img)
        # 上传图片以及参数部分
        self.upload_img_frame = LabelFrame(master=self.fun1_win, text='上传图片')
        self.file_entry = Entry(self.upload_img_frame, font=('', 17))
        self.folder_img = PhotoImage(file='src/img/folder.png')
        self.folder_but = Button(self.upload_img_frame, image=self.folder_img)
        self.ok_but = Button(self.upload_img_frame, text='确  定', )
        self.params_label = Label(self.upload_img_frame, text='识别参数：')
        # self.live = IntVar()
        # self.live_check = Checkbutton(master=self.up_frame, text='图片活体检测', variable=self.live, )
        self.params = {'age': ['年龄'], 'beauty': ['颜值'], 'expression': ['表情'], 'face_shape': ['脸型'], 'gender': ['性别'],
                       'glasses': ['眼镜'], 'emotion': ['情绪'], 'mask': ['口罩']}
        i = 1
        for param in self.params:
            i = i + 1
            # print(type(param))
            self.params[param].append(BooleanVar())
            # print(self.params[param])
            self.params_check = Checkbutton(master=self.upload_img_frame, text=self.params[param][0], font=('', 12),
                                            variable=self.params[param][1])
            self.params_check.grid(row=5, column=i)

        # 布局
        self.img_frame.grid(row=1, column=2, padx=5)
        self.upload_img_frame.grid(row=2, column=2, padx=5, sticky='w' + 'e')
        self.result_frame.grid(row=1, column=3, padx=5, rowspan=2, columnspan=3, sticky='n' + 's' + 'w' + 'e')
        self.result_frame.grid_propagate(flag=False)  # 阻止父组件自动调节尺寸以容纳所有子组件，默认值是True，该方法仅适用于父组件
        self.face_result_frame.grid(row=2, column=2, sticky='w' + 'e')
        self.img_label.grid(row=2, column=2)
        self.file_entry.grid(row=3, column=2, columnspan=7, padx=0, sticky='w' + 'e')
        self.folder_but.grid(row=3, column=9, sticky='w')
        self.ok_but.grid(row=3, column=10, sticky='e')
        self.params_label.grid(row=4, column=2)

        # 按键绑定
        self.ok_but.bind('<Button-1>', self.face_recognition)
        self.folder_but.bind('<Button-1>', self.open_file)

    def face_recognition(self, event):
        """上传图片请求识别，返回识别结果，不要开代理！！！"""
        self.face_field = ''
        for p in self.params:
            if self.params[p][1].get():
                self.face_field = self.face_field + p + ','
                print(self.face_field)
        print(self.file_path)
        # 之后将文件路径参数改成从entry控件获取
        self.result_json = fc.base64_recognition(self.file_path, self.face_field)
        print(self.result_json)
        self.show_result()

    def show_result(self):
        i = 1
        self.face_result_frame.destroy()
        self.face_result_frame = Frame(master=self.result_frame, width=280)
        # 选择查看识别结果
        # self.face_result_label = Label(master=self.face_result_frame,
        #                                text='识别到' + str(self.result_json['result']['face_num']) + '张人脸，查看第', font=('', 12))
        # self.face_result_but = ttk.Combobox(master=self.face_result_frame, )

        self.face_result_frame.grid(row=2, column=2, sticky='w' + 'e')
        # self.face_result_label.grid(row=1, column=2, columnspan=2, sticky='w')

        origin_result = ['none', 'smile', '', 'square', 'triangle', 'oval', 'heart', 'round', 'male', 'female',
                         'common', 'sun', 'angry', 'disgust', 'fear', 'happy', 'sad', 'surprise', 'neutral', 'pouty',
                         'grimace']

        for r_p in self.params:
            i = i + 1
            self.result_label = Label(master=self.face_result_frame, text=self.params[r_p][0] + '：', font=('', 12))
            self.result_label.grid(row=i, column=2, columnspan=3, sticky='w')
            if self.params[r_p][1].get():
                if r_p in ('age', 'beauty'):
                    self.result_label['text'] = self.params[r_p][0] + ':' + \
                                                str(self.result_json['result']['face_list'][0][r_p])
                else:
                    self.result_label['text'] = self.params[r_p][0] + ':' + str(
                        self.result_json['result']['face_list'][0][r_p]['type']).replace('none', '无').replace('smile',
                                                                                                              '微笑').replace(
                        'laugh', '大笑').replace('square', '方形').replace('triangle', '三角形').replace('oval', '椭圆').replace(
                        'heart', '心形').replace('round', '圆形').replace('female', '女性').replace('male', '男性').replace(
                        'common', '普通眼镜').replace('sun', '墨镜').replace('angry', '愤怒').replace('disgust', '厌恶').replace(
                        'fear', '恐惧').replace('happy', '高兴').replace('sad', '伤心').replace('surprise', '惊讶').replace(
                        'neutral', '无').replace('pouty', '撅嘴').replace('grimace', '鬼脸').replace('0', '无').replace('1',
                                                                                                                  '有')

    def open_file(self, event):
        """打开选择的文件并显示"""
        self.file_path = fc.open_file()
        print(self.file_path)
        self.file_entry.delete(0, END)
        self.file_entry.insert(END, self.file_path)
        self.show_img = fc.modify_img(self.file_path, 680, 400)
        self.img_label['image'] = self.show_img


class FaceCompare(Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.master = master
        # 功能2窗口
        self.fun2_win = LabelFrame(master=self.master, text='人脸对比')
        # 图片1部分
        self.img1_frame = LabelFrame(master=self.fun2_win, text='图片1')
        self.up_img1 = PhotoImage(file='src/img/upload.png')
        self.img1_label = Label(master=self.img1_frame, image=self.up_img1, width=485, height=400)
        # 图片2部分
        self.img2_frame = LabelFrame(master=self.fun2_win, text='图片2')
        self.img2_label = Label(master=self.img2_frame, image=self.up_img1, width=485, height=400)
        # 图片1上传
        self.upload_img1_frame = LabelFrame(master=self.fun2_win, text='上传图片1')
        self.file1_entry = Entry(self.upload_img1_frame, font=('', 17))
        self.folder_img = PhotoImage(file='src/img/folder.png')
        self.folder_but = Button(self.upload_img1_frame, image=self.folder_img)
        self.ok_but = Button(self.upload_img1_frame, text='确  定', )
        self.params_label = Label(self.upload_img1_frame, text='图片类型：')
        self.params = [('生活照', 1), ('身份证芯片照', 2), ('带水印证件照', 3), ('证件照片', 4)]
        self.v = IntVar()
        i = 1
        for param, num in self.params:
            i = i + 1
            self.params_radiobut = Radiobutton(master=self.upload_img1_frame, text=param, value=num, variable=self.v,
                                               font=('', 12))
            self.params_radiobut.grid(row=5, column=i, sticky='w')
        # 图片2上传
        self.upload_img2_frame = LabelFrame(master=self.fun2_win, text='上传图片2')

        # 布局
        self.fun2_win.grid(row=2, column=3, rowspan=5, padx=5, pady=5, sticky='n' + 's' + 'w' + 'e')
        self.fun2_win.propagate(flag=False)

        self.img1_frame.grid(row=2, column=2, padx=3)
        self.img1_label.grid(row=1, column=1)

        self.img2_label.grid(row=1, column=2)
        self.img2_frame.grid(row=2, column=3, padx=3)

        self.upload_img1_frame.grid(row=3, column=2, sticky='w' + 'e')
        self.file1_entry.grid(row=3, column=2, columnspan=3, padx=0, sticky='w' + 'e')
        self.folder_but.grid(row=3, column=5)
        self.ok_but.grid(row=3, column=6, sticky='e')
        self.params_label.grid(row=4, column=2, sticky='w')

        self.upload_img2_frame.grid(row=3, column=3)


if __name__ == '__main__':
    root = Tk()
    root.title('人脸识别系统V0.1')
    root.geometry('1170x792')
    Home(master=root)
    root.mainloop()
