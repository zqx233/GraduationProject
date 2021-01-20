import base64
from tkinter import *
import tkinter.filedialog
import tkinter.messagebox

import requests
from PIL import Image
from PIL import ImageTk


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
        Face(master=self.master)

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
        self.fun1_win.grid(row=2, column=3, rowspan=5, padx=5, pady=5, sticky='n' + 's')
        # 识别结果部分
        self.result_frame = LabelFrame(master=self.fun1_win, text='识别结果', width=285, height=510)
        self.face_result_frame = Frame(master=self.result_frame)
        # 图片展示部分
        self.img_frame = LabelFrame(master=self.fun1_win, text='')
        self.up_img = PhotoImage(file='src/img/upload.png')
        self.img_label = Label(self.img_frame, width=680, height=400, image=self.up_img)
        # 上传图片以及参数部分
        self.up_frame = LabelFrame(master=self.fun1_win, text='上传图片')
        self.file_entry = Entry(self.up_frame, font=('', 17))
        self.ok_but = Button(self.up_frame, text='确  定', )
        self.folder_img = PhotoImage(file='src/img/folder.png')
        self.folder_but = Button(self.up_frame, image=self.folder_img)
        self.params_label = Label(self.up_frame, text='识别参数：')
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
            self.params_check = Checkbutton(master=self.up_frame, text=self.params[param][0], font=('', 12),
                                            variable=self.params[param][1])
            self.params_check.grid(row=5, column=i)

        # 布局
        self.img_frame.grid(row=1, column=2, padx=5)
        self.up_frame.grid(row=2, column=2, padx=5, sticky='w' + 'e')
        self.result_frame.grid(row=1, column=3, padx=5, rowspan=2, sticky='n' + 's')
        self.face_result_frame.grid(row=2, column=2, sticky='w' + 'e')
        self.img_label.grid(row=2, column=2)
        self.file_entry.grid(row=3, column=2, columnspan=7, padx=0, sticky='w' + 'e')
        self.ok_but.grid(row=3, column=10, sticky='e')
        self.folder_but.grid(row=3, column=9, sticky='w')
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
            # print(self.params[p][0])
            # print(self.params[p][1].get())
        print(self.file_path)
        with open(self.file_path, 'rb') as f:
            img_base64 = base64.b64encode(f.read())
            b64 = img_base64.decode()
        request_url = "https://aip.baidubce.com/rest/2.0/face/v3/detect"
        params = "{\"image\":\"" + b64 + "\",\"image_type\":\"BASE64\",\"face_field\":\"" + self.face_field + "\",\"max_face_num\":\"30\"} "
        # access_token只有一个月有效期，最后记得完善一下
        access_token = '24.037e02027b589adb179b494a9c83aff7.2592000.1613726893.282335-23545866'
        request_url = request_url + "?access_token=" + access_token
        headers = {'content-type': 'application/json'}
        response = requests.post(request_url, data=params, headers=headers)
        if response:
            self.result_json = response.json()
            print(self.result_json)
            self.show_result()

    def show_result(self):
        i = 1
        self.face_result_frame.destroy()
        self.face_result_frame = Frame(master=self.result_frame)
        self.face_result_frame.grid(row=2, column=2, sticky='w' + 'e')
        for r_p in self.params:
            i = i + 1
            self.result_label = Label(master=self.face_result_frame, text=self.params[r_p][0] + '：', font=('', 12))
            self.result_label.grid(row=i, column=2)
            if self.params[r_p][1].get():
                if r_p in ('age', 'beauty'):
                    self.result_label['text'] = self.params[r_p][0] + ':' + \
                                                str(self.result_json['result']['face_list'][0][r_p])
                else:
                    self.result_label['text'] = self.params[r_p][0] + ':' + str(
                        self.result_json['result']['face_list'][0][r_p]['type'])

    def open_file(self, event):
        """打开选择的文件并显示"""
        self.file_path = tkinter.filedialog.askopenfilename(
            filetypes=[('JPG', '.jpg'), ('JPEG', '.jpeg'), ('PNG', '.png'), ('BMP', '.bmp')])
        self.file_entry.delete(0, END)
        self.file_entry.insert(END, self.file_path)
        self.up_img = Image.open(self.file_path)  # PhotoImage打开会报错，使用PIL库的ImageTK
        # 按比例将图片缩放到Frame大小，也可以用self.up_img.width或.height获取宽高数值
        if (self.up_img.size[0] / self.up_img.size[1]) > (680 / 400):
            rate = 680 / self.up_img.size[0]
        else:
            rate = 400 / self.up_img.size[1]
        rate = round(rate, 1)
        # pillow中调整图片大小的方法，第二个参数是图片质量Image.NEAREST ：低质量Image.BILINEAR：双线性Image.BICUBIC ：三次样条插值Image.ANTIALIAS：高质量
        self.out_img = self.up_img.resize((int(self.up_img.size[0] * rate), int(self.up_img.size[1] * rate)),
                                          Image.ANTIALIAS)
        self.show_img = ImageTk.PhotoImage(self.out_img)
        self.img_label['image'] = self.show_img


if __name__ == '__main__':
    root = Tk()
    root.title('人脸识别系统V0.1')
    root.geometry('1170x792')
    Home(master=root)
    root.mainloop()
