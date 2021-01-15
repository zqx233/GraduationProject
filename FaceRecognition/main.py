import tkinter as tk

from aip import AipOcr
from GUI import Widgets


def main():
    root = Widgets.Windows(None, None, None, '人脸识别系统V0.1').root_window()
    f1 = Widgets.Frames(root, 100, 300, 5, 5, None)
    f1.frames()
    f1.postion(0, 0)
    b1 = Widgets.Buttons(f1, 5, 10, 5, 5, 'ok', lambda: print('ok'))
    b1.buttons()
    b1.postion(0, 0)

    # face_detection = Widgets.Windows(root, 500, 500, '人脸检测').toplevel_windows()
    tk.mainloop()


if __name__ == '__main__':
    main()
