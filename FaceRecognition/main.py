import tkinter as tk

from aip import AipOcr
from fun import AppWidgets, Features

root = tk.Tk()
root.title('人脸识别系统V0.1')
# root.geometry('1250x550')
# root.resizable(width=False, height=False)


def main():
    main_label = AppWidgets.AllLabels(root, '人脸识别系统', ('', 18))
    main_label.label()
    main_label.location(1, 1, 5, 20, 3, 'n' + 's')

    fun_button1 = AppWidgets.AllButtons(root, '人脸识别与属性分析', lambda: Features.create_window(root, '人脸识别与属性分析'), )
    fun_button1.main_buttons(150, 150, 'src/img/face.png')
    fun_button1.location(2, 0)

    # fun_button2 = AppWidgets.AllButtons(root, '人脸对比', lambda: Features.create_window(root, '人脸对比'), )
    # fun_button2.main_buttons(150, 150, 'src/img/compare.png')
    # fun_button2.location(2, 1)
    #
    # fun_button3 = AppWidgets.AllButtons(root, '人脸搜索', lambda: Features.create_window(root, '人脸搜索'), )
    # fun_button3.main_buttons(150, 150, 'src/img/search.png')
    # fun_button3.location(2, 2)
    #
    # fun_button4 = AppWidgets.AllButtons(root, '图片活体检测', lambda: Features.create_window(root, '图片活体检测'), )
    # fun_button4.main_buttons(150, 150, 'src/img/detect.png')
    # fun_button4.location(2, 3)
    #
    # fun_button5 = AppWidgets.AllButtons(root, '关于', lambda: Features.create_window(root, '关于'), )
    # fun_button5.main_buttons(150, 150, 'src/img/about.png')
    # fun_button5.location(2, 4)


    root.mainloop()


if __name__ == '__main__':
    main()
