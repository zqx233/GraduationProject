import tkinter as tk

from aip import AipOcr
from GUI import AppWidgets

root = tk.Tk()
root.title('人脸识别系统')


def main():


    fun_button1 = AppWidgets.AllButtons(root, '人脸识别与属性分析', lambda: ceate_window('人脸识别与属性分析'), )
    fun_button1.main_buttons(20, 10)
    fun_button1.postion(2, 0)

    fun_button2 = AppWidgets.AllButtons(root, '人脸对比', lambda: ceate_window('人脸对比'), )
    fun_button2.main_buttons(20, 10)
    fun_button2.postion(2, 1)

    fun_button3 = AppWidgets.AllButtons(root, '人脸搜索', lambda: ceate_window('人脸搜索'), )
    fun_button3.main_buttons(20, 10)
    fun_button3.postion(2, 2)

    fun_button4 = AppWidgets.AllButtons(root, 'ok', lambda: ceate_window('功能2'), )
    fun_button4.main_buttons(20, 10)
    fun_button4.postion(2, 3)

    fun_button5 = AppWidgets.AllButtons(root, 'ok', lambda: ceate_window('关于'), )
    fun_button5.main_buttons(20, 10)
    fun_button5.postion(2, 4)

    root.mainloop()


def ceate_window(title):
    w1 = AppWidgets.AllWindows(root, title)
    w1.top_windows()


if __name__ == '__main__':
    main()
