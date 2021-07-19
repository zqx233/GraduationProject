from time import sleep
from tkinter import *
import tkinter.messagebox
from tkinter import ttk
import functions as fc


class Home(Frame):
    """主界面的功能按钮"""

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
        self.fun4_img = PhotoImage(file='src/img/database.png')
        self.fun5_img = PhotoImage(file='src/img/about.png')
        # 按钮组件
        self.fun1_but = Button(self.master, width=140, height=130, text='人脸识别与属性分析', font=('', 12), image=self.fun1_img,
                               compound='top')
        self.fun2_but = Button(self.master, width=140, height=130, text='人脸对比', font=('', 12), image=self.fun2_img,
                               compound='top')
        self.fun3_but = Button(self.master, width=140, height=130, text='人脸搜索', font=('', 12), image=self.fun3_img,
                               compound='top')
        self.fun4_but = Button(self.master, width=140, height=130, text='人脸库管理', font=('', 12), image=self.fun4_img,
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

    def fun1_but_ev(self, event):  # 要加event参数才能被调用，之后的按钮用command调用，不知道为什么用bind会点下去弹不起来
        Face(master=self.master)

    def fun2_but_ev(self, event):
        FaceCompare(master=self.master)

    def fun3_but_ev(self, event):
        FaceSearch(master=self.master)

    def fun4_but_ev(self, event):
        FaceDatabase(master=self.master)

    def fun5_but_ev(self, event):
        About(master=self.master)


class Face(Frame):
    """人脸识别与属性分析界面"""

    def __init__(self, master=None):
        super().__init__(master)
        self.master = master
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
        self.folder_but = Button(self.upload_img_frame, image=self.folder_img,
                                 command=self.open_file)  # command的参数的函数加了()就会自动调用
        self.ok_but = Button(self.upload_img_frame, text='确  定', command=self.face_recognition)
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

    def face_recognition(self):
        """上传图片请求识别，返回识别结果，不要开代理！！！"""
        self.face_field = ''
        for p in self.params:
            if self.params[p][1].get():
                self.face_field = self.face_field + p + ','
                print(self.face_field)
        print(self.file_path)
        # TODO: 之后将文件路径参数改成从entry控件获取
        # TODO: 完善一下其他情况的显示
        self.result_json = fc.base64_recognition(self.file_path, self.face_field)
        print(self.result_json)
        # self.select_result()
        self.show_result()

    def show_result(self):
        i = 1
        self.face_result_frame.destroy()
        self.face_result_frame = Frame(master=self.result_frame, width=280)
        # TODO: 选择查看识别结果
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

    # def show_result(self, num):
    #     """识别结果展示"""
    #     i = 1
    #
    #     # self.face_result_frame = Frame(master=self.result_frame, width=280)
    #
    #     for r_p in self.params:
    #         i = i + 1
    #         self.show_result_frame = Frame(master=self.face_result_frame)
    #         self.result_label = Label(master=self.show_result_frame, text=self.params[r_p][0] + '：', font=('', 12))
    #         self.show_result_frame.grid(row=3, column=2, sticky='w' + 'e')
    #         self.result_label.grid(row=i, column=2, columnspan=3, sticky='w')
    #         if self.params[r_p][1].get():
    #             if r_p in ('age', 'beauty'):
    #                 self.result_label['text'] = self.params[r_p][0] + ':' + \
    #                                             str(self.result_json['result']['face_list'][int(num)][r_p])
    #             else:
    #                 self.result_label['text'] = self.params[r_p][0] + ':' + str(
    #                     self.result_json['result']['face_list'][int(num)][r_p]['type']).replace('none', '无').replace(
    #                     'smile',
    #                     '微笑').replace(
    #                     'laugh', '大笑').replace('square', '方形').replace('triangle', '三角形').replace('oval', '椭圆').replace(
    #                     'heart', '心形').replace('round', '圆形').replace('female', '女性').replace('male', '男性').replace(
    #                     'common', '普通眼镜').replace('sun', '墨镜').replace('angry', '愤怒').replace('disgust', '厌恶').replace(
    #                     'fear', '恐惧').replace('happy', '高兴').replace('sad', '伤心').replace('surprise', '惊讶').replace(
    #                     'neutral', '无').replace('pouty', '撅嘴').replace('grimace', '鬼脸').replace('0', '无').replace('1',
    #                                                                                                               '有')

    # def select_result(self):
    #     # TODO: 选择查看识别结果
    #     self.show_result(0)
    #     self.select_result_frame = Frame(master=self.face_result_frame)
    #     self.face_result_label = Label(master=self.select_result_frame,
    #                                    text='识别到' + str(self.result_json['result']['face_num']) + '张人脸，查看第',
    #                                    font=('', 12))
    #     self.face_result_combobox = ttk.Combobox(master=self.select_result_frame, width=2)
    #     result_num = []  # 识别到的人脸数量的下拉列表
    #     for i in range(int(self.result_json['result']['face_num'])):
    #         result_num.append(i + 1)
    #     self.face_result_combobox['value'] = result_num
    #     self.face_result_combobox.current(0)
    #     self.face_result_label2 = Label(master=self.select_result_frame, text='张人脸', font=('', 12))
    #     self.select_result_frame.grid(row=1, column=2, sticky='w' + 'e')
    #     # self.face_result_frame.grid(row=2, column=2, sticky='w' + 'e')
    #     self.face_result_label.grid(row=1, column=2, columnspan=2, sticky='w')
    #     self.face_result_combobox.grid(row=1, column=4, sticky='w')
    #     self.face_result_label2.grid(row=1, column=5, sticky='w')
    #
    #     self.face_result_combobox.bind('<Button-1>', self.show_select_result)

    # def show_select_result(self, event):
    #     self.show_result_frame.destroy()
    #     self.show_result(int(self.face_result_combobox.get()) - 1)

    def open_file(self):
        """打开选择的文件并显示"""
        self.file_path = fc.open_file()
        print(self.file_path)
        self.file_entry.delete(0, END)
        self.file_entry.insert(END, self.file_path)
        self.show_img = fc.modify_img(self.file_path, 680, 400)
        self.img_label['image'] = self.show_img


class FaceCompare(Frame):
    """人脸对比界面"""

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
        self.folder_but = Button(self.upload_img1_frame, image=self.folder_img, command=self.open_file1)
        self.ok_but = Button(self.upload_img1_frame, text='确  定', command=self.compare)
        self.params_label = Label(self.upload_img1_frame, text='图片类型：')
        self.params = [('生活照', 'LIVE'), ('身份证芯片照', 'IDCARD'), ('带水印证件照', 'WATERMARK'), ('证件照片', 'CERT')]
        self.v = StringVar()
        i = 1
        for param, string in self.params:
            i = i + 1
            self.v.set('LIVE')  # 字符串变量默认值是''，会导致第一次运行时全选，设置为0后为全不选状态
            self.params_radiobut = Radiobutton(master=self.upload_img1_frame, text=param, value=string, variable=self.v,
                                               font=('', 12))
            self.params_radiobut.grid(row=5, column=i, sticky='w')
        # 图片2上传
        self.upload_img2_frame = LabelFrame(master=self.fun2_win, text='上传图片2')
        self.file2_entry = Entry(self.upload_img2_frame, font=('', 17))
        self.folder2_but = Button(self.upload_img2_frame, image=self.folder_img, command=self.open_file2)
        self.ok2_but = Button(self.upload_img2_frame, text='确  定', command=self.compare)
        self.params2_label = Label(self.upload_img2_frame, text='图片类型：')
        self.v2 = StringVar()
        j = 1
        for param, string in self.params:
            j = j + 1
            self.v2.set('LIVE')
            self.params2_radiobut = Radiobutton(master=self.upload_img2_frame, text=param, value=string,
                                                variable=self.v2,
                                                font=('', 12))
            self.params2_radiobut.grid(row=5, column=j, sticky='w')
        # 显示结果
        self.result_frame = LabelFrame(master=self.fun2_win, text='对比结果', height=230)
        self.show_result_label = Label(master=self.result_frame, text='', font=('', 20))

        # 布局
        self.fun2_win.grid(row=2, column=3, rowspan=5, padx=5, pady=5, sticky='n' + 's' + 'w' + 'e')

        self.img1_frame.grid(row=2, column=2, padx=3)
        self.img1_label.grid(row=1, column=1)

        self.img2_frame.grid(row=2, column=3, padx=3)
        self.img2_label.grid(row=1, column=2)

        self.upload_img1_frame.grid(row=3, column=2, padx=3, sticky='w' + 'e')
        self.file1_entry.grid(row=3, column=2, columnspan=3, padx=0, sticky='w' + 'e')
        self.folder_but.grid(row=3, column=5, sticky='w')
        self.ok_but.grid(row=3, column=6, sticky='e')
        self.params_label.grid(row=4, column=2, sticky='w')

        self.upload_img2_frame.grid(row=3, column=3, padx=3, sticky='w' + 'e')
        self.file2_entry.grid(row=3, column=2, columnspan=3, padx=0, sticky='w' + 'e')
        self.folder2_but.grid(row=3, column=5, sticky='w')
        self.ok2_but.grid(row=3, column=6, sticky='e')
        self.params2_label.grid(row=4, column=2)

        self.result_frame.grid(row=4, column=2, columnspan=2, padx=3, sticky='n' + 's' + 'w' + 'e')
        self.result_frame.grid_propagate(flag=False)
        self.show_result_label.grid(row=2, column=2, sticky='n')

        # 按键绑定
        # self.folder_but.bind('<Button-1>', self.open_file1)
        # self.folder2_but.bind('<Button-1>', self.open_file2)

    def open_file1(self):
        self.file1_path = fc.open_file()
        self.file1_entry.delete(0, END)
        self.file1_entry.insert(END, self.file1_path)
        self.show_img1 = fc.modify_img(self.file1_path, 485, 400)
        self.img1_label['image'] = self.show_img1

    def open_file2(self):
        self.file2_path = fc.open_file()
        self.file2_entry.delete(0, END)
        self.file2_entry.insert(END, self.file2_path)
        self.show_img2 = fc.modify_img(self.file2_path, 485, 400)
        self.img2_label['image'] = self.show_img2

    def compare(self):
        if self.file1_entry.get() == '' or self.file2_entry.get() == '':
            pass
        else:
            self.show_result_label['text'] = '相似度为' + str(
                fc.compare_request(self.file1_entry.get(), self.file2_entry.get(), self.v.get(), self.v2.get())) + '%'


class FaceSearch(Frame):
    """人脸搜索界面"""

    def __init__(self, master=None):
        super().__init__(master)
        self.master = master
        # 搜索窗口
        self.fun3_win = LabelFrame(master=self.master, text='人脸搜索')
        self.fun3_win.grid(row=2, column=3, rowspan=5, padx=5, pady=5, sticky='n' + 's' + 'w' + 'e')
        # 被搜索图片展示部分
        self.img_frame = LabelFrame(master=self.fun3_win, text='被查人脸')
        self.up_img = PhotoImage(file='src/img/upload.png')
        self.img_label = Label(master=self.img_frame, width=485, height=400, image=self.up_img)
        # 上传图片以及参数部分
        self.upload_img_frame = LabelFrame(master=self.fun3_win, text='上传图片')
        self.file_entry = Entry(self.upload_img_frame, font=('', 17))
        self.folder_img = PhotoImage(file='src/img/folder.png')
        self.folder_but = Button(self.upload_img_frame, image=self.folder_img, command=self.open_file)
        self.ok_but = Button(self.upload_img_frame, text='确  定', command=self.show_result)
        self.search_label = Label(master=self.upload_img_frame, text='搜索范围：')
        self.search_combobox = ttk.Combobox(master=self.upload_img_frame)

        # 结果展示部分
        self.result_frame = LabelFrame(master=self.fun3_win, text='查找结果', width=490, height=532)

        self.fun3_win.grid(row=2, column=3, rowspan=5, padx=5, pady=5, sticky='n' + 's' + 'w' + 'e')
        self.img_frame.grid(row=2, column=2, padx=3)
        self.img_label.grid(row=1, column=1)
        self.upload_img_frame.grid(row=3, column=2, sticky='w' + 'e')
        self.file_entry.grid(row=2, column=2, columnspan=3, sticky='w' + 'e')
        self.folder_but.grid(row=2, column=5, sticky='w')
        self.ok_but.grid(row=2, column=6, padx=15)
        self.search_label.grid(row=3, column=2, sticky='w')
        self.search_combobox.grid(row=4, column=2, pady=5, sticky='w')
        self.result_frame.grid(row=2, column=3, rowspan=2)
        self.result_frame.grid_propagate(flag=False)

        self.search_combobox.bind('<Button-1>', self.show_group)

    def open_file(self):
        """打开选择的文件并显示"""
        self.file_path = fc.open_file()
        print(self.file_path)
        self.file_entry.delete(0, END)
        self.file_entry.insert(END, self.file_path)
        self.show_img = fc.modify_img(self.file_path, 680, 400)
        self.img_label['image'] = self.show_img

    def show_group(self, event):
        self.search_combobox['value'] = fc.get_group()

    def show_result(self):
        self.result_img = []
        self.result_user_list = fc.face_search(self.file_entry.get(), self.search_combobox.get())
        print(self.result_user_list)
        for i in range(4):
            self.result_img_path = 'FaceDatabase/' + self.search_combobox.get() + '/' + str(
                self.result_user_list[i]['user_id']) + '/' + str(
                fc.get_user_face_list(self.search_combobox.get(), self.result_user_list[i]['user_id'])[0][
                    'face_token']) + '.jpg'
            self.result_img.append(fc.modify_img(self.result_img_path, 220, 190))
            self.result_img_frame = Frame(master=self.result_frame)
            self.result_user_img_label = Label(master=self.result_img_frame, image=self.result_img[i],
                                               text='用户名：' + str(
                                                   self.result_user_list[i]['user_id']) + '\n' + '相似度：' + str(
                                                   self.result_user_list[i]['score']) + '%', compound='top', width=220,
                                               height=250)
            self.result_img_frame.grid(row=i // 2, column=i % 2, padx=2, pady=2)
            self.result_user_img_label.grid(row=2, column=1)
            sleep(0.5)


class FaceDatabase(Frame):
    """人脸库管理界面"""

    def __init__(self, master=None):
        super().__init__(master)
        self.master = master
        # 人脸库窗口
        self.fun4_win = LabelFrame(master=self.master, text='人脸库管理', width=1000)
        # 选择用户部分
        self.select_frame = Frame(master=self.fun4_win)
        self.select_group_label = Label(master=self.select_frame, text='用户组：')
        self.select_group_combobox = ttk.Combobox(master=self.select_frame)
        self.select_user_label = Label(master=self.select_frame, text='用户：')
        self.select_user_combobox = ttk.Combobox(master=self.select_frame)
        self.select_ok_button = Button(master=self.select_frame, text='查 询', command=self.show_user_img)
        # 用户、组增删
        self.add_face_button = Button(master=self.select_frame, text='添加人脸', command=self.new_user_win)
        self.new_group_but = Button(master=self.select_frame, text='新建组', command=self.new_group_win)
        self.delete_group_but = Button(master=self.select_frame, text='删除当前组', foreground='red',
                                       command=lambda: fc.delete_group(self.select_group_combobox.get()))
        self.delete_user_but = Button(master=self.select_frame, text='删除当前用户', foreground='red',
                                      command=lambda: fc.delete_user(self.select_group_combobox.get(),
                                                                     self.select_user_combobox.get()))
        # 显示用户所有图片部分
        self.user_img_frame = Frame(master=self.fun4_win)
        self.user_load_img = PhotoImage(file='src/img/upload.png')
        # 布局
        self.fun4_win.grid(row=2, column=3, rowspan=5, padx=5, pady=5, sticky='n' + 's' + 'w' + 'e')
        self.fun4_win.grid_propagate(flag=False)
        self.select_frame.grid(row=2, column=2, pady=5, sticky='w' + 'e')
        self.select_group_label.grid(row=2, column=2)
        self.select_group_combobox.grid(row=2, column=3)
        self.select_user_label.grid(row=2, column=4)
        self.select_user_combobox.grid(row=2, column=5)
        self.select_ok_button.grid(row=2, column=6)
        self.user_img_frame.grid(row=3, column=2, columnspan=3, sticky='w')
        self.add_face_button.grid(row=2, column=7, padx=20)
        self.new_group_but.grid(row=2, column=8)
        self.delete_group_but.grid(row=2, column=9, padx=20)
        self.delete_user_but.grid(row=2, column=10)

        self.select_group_combobox.bind('<Button-1>', self.show_group)
        self.select_user_combobox.bind('<Button-1>', self.show_user)

    def show_group(self, event):
        """在用户组下拉菜单中显示所有用户组列表"""
        self.select_group_combobox['value'] = fc.get_group()

    def show_user(self, event):
        """在用户下拉菜单中显示已选用户组中的所有用户列表"""
        self.select_user_combobox['value'] = fc.get_user(self.select_group_combobox.get())

    def show_user_img(self):
        """显示所选用户所有照片"""
        self.user_img = []  # 用一个列表来保存一个用户所有的人脸，使得可以批量显示，否则只是显示最后一个，其他的图片会丢失
        self.user_img_list = fc.get_user_face_list(self.select_group_combobox.get(), self.select_user_combobox.get())
        for i in range(0, len(self.user_img_list)):
            self.user_img_path = 'FaceDatabase/' + self.select_group_combobox.get() + '/' + self.select_user_combobox.get() + '/' + \
                                 str(self.user_img_list[i]['face_token']) + '.jpg'
            self.user_img.append(fc.modify_img(self.user_img_path, 195, 170))
            self.user_img_label = Label(master=self.user_img_frame, image=self.user_img[i], width=195, height=170)
            self.user_img_label.grid(row=i // 5, column=i % 5, padx=2, pady=2, sticky='w')

    def new_group_win(self):
        """打开新建组窗口"""
        self.new_group_win = Toplevel(master=self.master, height=245, width=425)
        self.new_group_win.title('新建组')
        self.new_group_win.geometry('555x190')
        self.new_group_label = Label(master=self.new_group_win, text='由数字、字母和下划线组成，最多48个字符：')
        self.new_group_entry = Entry(master=self.new_group_win, font=('', 15), width=48)
        self.new_group_ok_but = Button(master=self.new_group_win, text='确 定',
                                       command=lambda: fc.new_group(self.new_group_entry.get()))
        self.new_group_label.grid(row=1, column=2, padx=88, pady=20)
        self.new_group_entry.grid(row=2, column=2, padx=30)
        self.new_group_ok_but.grid(row=3, column=2, pady=25)

    def new_user_win(self):
        """打开添加人脸窗口"""
        self.new_user_win = Toplevel(master=self.master, height=245, width=425)
        self.new_user_win.title('添加人脸')
        self.new_user_win.geometry('760x465')
        self.note_label = Label(master=self.new_user_win, text='由数字、字母和下划线组成，最多128个字符')
        self.new_user_group_label = Label(master=self.new_user_win, text='用户组：')
        self.new_user_group_combobox = ttk.Combobox(master=self.new_user_win)
        self.new_user_label = Label(master=self.new_user_win, text='用户：')
        self.new_user_entry = Entry(master=self.new_user_win, font=('', 15), width=24)
        self.new_user_ok_but = Button(master=self.new_user_win, text='确  定',
                                      command=lambda: fc.new_user(self.new_user_img_path,
                                                                  self.new_user_group_combobox.get(),
                                                                  self.new_user_entry.get()))
        self.new_user_frame = LabelFrame(master=self.new_user_win)
        self.up_img = PhotoImage(file='src/img/upload.png')
        self.new_user_img_label = Label(master=self.new_user_frame,
                                        text='点此添加图片\n请上传用户正面、无遮挡照片\n仅支持PNG、JPG、JPEG、BMP格式，大小5M以内\n若图片中包含多张人脸，则只注册图片中可检测到的最大脸\n若用户名已存在，则将追加到该用户下，每个用户最多可添加20张人脸照片',
                                        font=('', 15), image=self.up_img, compound='top', width=710, height=320)

        self.new_user_group_label.grid(row=2, column=0, pady=10)
        self.new_user_group_combobox.grid(row=2, column=1, pady=10)
        self.new_user_label.grid(row=2, column=2, pady=10)
        self.new_user_entry.grid(row=2, column=3, pady=10)
        self.note_label.grid(row=2, column=4, padx=5, pady=10)
        self.new_user_frame.grid(row=3, column=0, columnspan=5, padx=0, pady=10)
        self.new_user_img_label.grid(row=2, column=2)
        self.new_user_ok_but.grid(row=4, column=4, sticky='e')

        self.new_user_group_combobox.bind('<Button-1>', self.select_group)
        self.new_user_img_label.bind('<Button-1>', self.add_img)

    def add_img(self, event):
        """新建用户界面添加图片"""
        self.new_user_img_path = fc.open_file(parent=self.new_user_win)
        self.show_new_user_img = fc.modify_img(self.new_user_img_path, 710, 320)
        self.new_user_img_label['image'] = self.show_new_user_img
        self.new_user_img_label['text'] = ''

    def select_group(self, event):
        """新建用户界面中显示所有组"""
        self.new_user_group_combobox['value'] = fc.get_group()


class About(Frame):
    """关于界面"""

    def __init__(self, master=None):
        super().__init__(master)
        self.master = master
        # 关于界面窗口
        self.fun5_win = LabelFrame(master=self.master, text='关于', width=1000, height=780)
        self.title_label = Label(master=self.fun5_win, text='人脸识别系统', font=('', 20))
        self.version_label = Label(master=self.fun5_win, text='V1.0\n作者：赵其昕')
        self.introduce_label = Label(master=self.fun5_win,
                                     text='基于Python开发，由百度AI支持的一款人脸识别系统，具有人脸识别与属性分析、人脸对比、人脸搜索、人脸库管理功能')
        self.github_label = Label(master=self.fun5_win, text='Github项目地址：')
        self.github_link_label = Label(master=self.fun5_win, text='https://github.com/zqx233/GraduationProject')

        self.fun5_win.grid(row=2, column=3, rowspan=5, padx=5, pady=5, sticky='n' + 's' + 'w' + 'e')
        self.fun5_win.grid_propagate(flag=False)
        self.title_label.grid(row=2, column=2, columnspan=2)
        self.version_label.grid(row=3, column=2, columnspan=2)
        self.introduce_label.grid(row=4, column=2, columnspan=2)
        self.github_label.grid(row=5, column=2)
        self.github_link_label.grid(row=5, column=3)


if __name__ == '__main__':
    root = Tk()
    root.title('人脸识别系统V0.1')
    root.geometry('1170x792')
    Home(master=root)
    root.mainloop()
