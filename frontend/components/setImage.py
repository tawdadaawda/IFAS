import tkinter as tk
from PIL import Image, ImageTk


def homeClicked(event):
    print("home click")


def hangerClicked(event):
    print("hanger click")


def shopClicked(event):
    print("shop click")


def colorClicked(event):
    print("color click")


def bubblesClicked(event):
    print("bubbles click")


class SetImage(object):
    def __init__(self):
        None

    def setImage(callbackName,  frame, imagePath, width, height, x, y, bg="white"):

        # 画像のリサイズ
        #basewidth = width
        image = Image.open(imagePath)
        #wpercent = (basewidth/float(image.size[0]))
        #hsize = int((float(image.size[1])*float(wpercent)))
        image = image.resize((width, height), Image.ANTIALIAS)

        frame.homeImage = ImageTk.PhotoImage(image)
        frame.home = tk.Canvas(
            frame, width=width, height=height, background=bg)
        frame.home.create_image(0, 0, image=frame.homeImage)
        frame.home.bind("<1>", eval(callbackName))
        frame.home.pack()
        frame.home.place(x=x, y=y)

    def createToplevel(frame, width, height, x, y, bg="white"):

        relative_y = 100  # メインフレームとのy軸のずれ
        frame.sub_win = tk.Toplevel(
            frame, width=width, height=height, bg=bg)

        # メインフレームとの相対位置を指定
        frame.sub_win.geometry("+%d+%d" % (x, y + relative_y))

        # toplevelオブジェクト（sub-win）の属性設定。透明色＝白に指定すると、背景色＝白＝透明色となり、ウィンドウが透明化する。
        frame.sub_win.wm_attributes("-transparentcolor", bg)

        # 常に最前に表示する設定
        frame.sub_win.wm_attributes("-topmost", True)
        frame.sub_win.overrideredirect(True)
        return frame.sub_win
