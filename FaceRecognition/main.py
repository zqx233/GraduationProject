from tkinter import *


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
        self.fun1_but = Button(self.master, width=150, height=150, text='人脸识别与属性分析', font=('', 12), image=self.fun1_img,
                               compound='top')
        self.fun2_but = Button(self.master, width=150, height=150, text='人脸对比', font=('', 12), image=self.fun2_img,
                               compound='top')
        self.fun3_but = Button(self.master, width=150, height=150, text='人脸搜索', font=('', 12), image=self.fun3_img,
                               compound='top')
        self.fun4_but = Button(self.master, width=150, height=150, text='图片活体检测', font=('', 12), image=self.fun4_img,
                               compound='top')
        self.fun5_but = Button(self.master, width=150, height=150, text='关于', font=('', 12), image=self.fun5_img,
                               compound='top')
        # 布局
        self.title_label.grid(row=1, column=1, padx=5, pady=20, columnspan=3)
        self.fun1_but.grid(row=2, column=0, padx=10, pady=25)
        self.fun2_but.grid(row=2, column=1, padx=10, pady=25)
        self.fun3_but.grid(row=2, column=2, padx=10, pady=25)
        self.fun4_but.grid(row=2, column=3, padx=10, pady=25)
        self.fun5_but.grid(row=2, column=4, padx=10, pady=25)
        # 按键绑定
        self.fun1_but.bind('<Button-1>', self.fun1_but_ev)
        self.fun2_but.bind('<Button-1>', self.fun2_but_ev)
        self.fun3_but.bind('<Button-1>', self.fun3_but_ev)
        self.fun4_but.bind('<Button-1>', self.fun4_but_ev)
        self.fun5_but.bind('<Button-1>', self.fun5_but_ev)

    def fun1_but_ev(self, event):
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
        self.fun1_win = Toplevel(master=self.master)
        self.fun1_win.title('人脸识别与属性分析')
        self.grid()
        # 识别结果
        self.result_frame = LabelFrame(master=self.fun1_win, text='识别结果', width=50, height=50)
        # 图片展示
        self.img_frame = LabelFrame(master=self.fun1_win, text='图片')
        self.up_img = PhotoImage(file='src/img/upload.png')
        self.img_label = Label(self.img_frame, width=500, height=500, image=self.up_img)
        # 上传图片以及参数
        self.up_frame = LabelFrame(master=self.fun1_win, text='上传图片')
        self.file_entry = Entry(self.up_frame, )
        self.upload_but = Button(self.up_frame, text='确  定', )
        self.live = IntVar()
        self.live_check = Checkbutton(master=self.up_frame, text='图片活体检测', variable=self.live, )
        self.params = ['年龄', '性别', '口罩']
        self.v = []
        i = 1
        for param in self.params:
            i=i+1
            self.v.append(IntVar())
            self.params_check = Checkbutton(master=self.up_frame, text=param, variable=self.v[-1])
            self.params_check.grid(row=4, column=i)
        # 布局
        self.img_frame.grid(row=1, column=2, padx=5)
        self.up_frame.grid(row=2, column=2, padx=5, sticky='w' + 'e')
        self.result_frame.grid(row=1, column=3, padx=5)
        self.img_label.grid(row=2, column=2)
        self.file_entry.grid(row=3, column=2, padx=5, sticky='w' + 'e')
        self.upload_but.grid(row=3, column=3, sticky='e')


if __name__ == '__main__':
    root = Tk()
    root.title('人脸识别系统V0.1')
    root.geometry('1500x600')
    Home(master=root)
    root.mainloop()
