import tkinter as tk


class AllWidgets:
    def __init__(self, master):
        self.master = master


class AllButtons(AllWidgets):
    def __init__(self, master, text, command):
        super().__init__(master)
        self.text = text
        self.command = command

    def main_buttons(self, width, height, image):
        self.img = tk.PhotoImage(file=image)  # 要将图片作为类属性，否则会被python垃圾回收机制回收，导致图片不显示
        self.m_b = tk.Button(master=self.master, text=self.text, width=width, font=('', 12), image=self.img,
                             compound='top',
                             height=height,
                             command=self.command)

    def location(self, x, y):
        self.m_b.grid(row=x, column=y, padx=10, pady=25)


class AllWindows(AllWidgets):
    def __init__(self, master, title):
        self.master = master
        self.title = title

    def top_windows(self):
        tw1 = tk.Toplevel(master=self.master).title(self.title)
        return tw1


class AllLabels(AllWidgets):
    def __init__(self, master, text, font):
        super().__init__(master)
        self.text = text
        self.font = font

    def label(self):
        self.m_l = tk.Label(master=self.master, text=self.text, font=self.font)

    def location(self, x, y, padx, pady, columnspan, sticky):
        self.m_l.grid(row=x, column=y, padx=padx, pady=pady, columnspan=columnspan, sticky=sticky)


class ImgLabel(AllLabels):
    def label(self, image=None):  # 改变父类方法参数并重写方法内容，要为参数添加默认值
        self.img = tk.PhotoImage(file=image)
        self.i_l = tk.Label(master=self.master, image=self.img)

    def upload_img(self, image):
        self.img = tk.PhotoImage(file=image)
        self.i_l['image'] = self.img

    def location(self, x, y, padx, pady, columnspan, sticky):
        self.i_l.grid(row=x, column=y, padx=padx, pady=pady, columnspan=columnspan, sticky=sticky)


class AllFrames(AllWidgets):
    def __init__(self, master, ):
        super().__init__(master)
