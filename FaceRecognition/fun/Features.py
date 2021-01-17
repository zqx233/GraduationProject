from FaceRecognition.fun import AppWidgets


def create_window(master, title):
    w = AppWidgets.AllWindows(master, title).top_windows()
    img_label1 = AppWidgets.ImgLabel(AppWidgets.AllWindows.master, None, None)
    img_label1.label(image='./src/img/face.png')
    img_label1.location(0, 0, 5, 5, 1, 'n')
