import tkinter as tk


# class AllWidgets():
#     def __init__(self, master,row, column):
#         self.master = master
#         self.row = row
#         self.column = column
#
#
# class Button(AllWidgets):
#     def __init__(self, text, commmand, master, row, column):
#         AllWidgets.__init__(self, master, row, column)
#         self.text = text
#         self.command = commmand
#         self.create()
#
#     def create(self):
#         self.b = tk.Button(master=self.master, text=self.text, command=self.command)
#         self.b.grid(row=self.row, column=self.column)


class Windows:
    def __init__(self, master, height, width, title):
        self.master = master
        self.height = height
        self.width = width
        self.title = title

    def root_window(self):
        self.r = tk.Tk()
        self.r.title(self.title)
        # self.r.mainloop()

    def toplevel_windows(self):
        self.t = tk.Toplevel(master=self.master, height=self.height, width=self.width)
        self.t.title(self.title)
        # self.t.mainloop()


class Widgets:
    def __init__(self, master, height, width, padx, pady):
        self.master = master
        self.height = height
        self.width = width
        self.padx = padx
        self.pady = pady
        # self.row = row
        # self.column = column


class Frames(Widgets):
    def __init__(self, master, height, width, padx, pady, text):
        Widgets.__init__(self, master, height, width, padx, pady)
        self.text = text
        self.f = tk.Frame

    def frames(self):
        self.f = tk.Frame(master=self.master, padx=self.padx, pady=self.pady)
    def postion(self, row, column):
        self.f.grid(row=row, column=column)

class Buttons(Widgets):
    def __init__(self, master, height, width, padx, pady, text, command):
        Widgets.__init__(self, master, height, width, padx, pady)
        self.text = text
        self.command = command

    def buttons(self):
        # self.b = tk.Button
        b = tk.Button(master=self.master, text=self.text, command=self.command)
    def postion(self, row, column):
        self.postion(row, column)