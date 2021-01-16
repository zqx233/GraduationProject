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


class AllWidgets:
    def __init__(self, master):
        self.master = master



class AllButtons(AllWidgets):
    def __init__(self, master, text, command):
        super().__init__(master)
        self.text = text
        self.command = command

    def main_buttons(self, width, height):
        self.m_b = tk.Button(master=self.master, text=self.text, width=width, height=height, command=self.command)

    def postion(self, x, y):
        self.m_b.grid(row=x, column=y)


class AllWindows(AllWidgets):
    def __init__(self, master, title):
        self.master = master
        self.title = title

    def top_windows(self):
        tk.Toplevel(master=self.master).title(self.title)

class AllLables(AllWidgets):
