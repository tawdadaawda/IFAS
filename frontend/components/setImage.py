import tkinter as tk
from PIL import Image, ImageTk


def homeClicked(event, frame, mainFrameInfo):
    print(event.widget)
    print("home click")
    frame.destroy()
    mainFrameInfo.screenTransition("homeClicked")


def homeToChoosing(event, frame, mainFrameInfo):
    print(event.widget)
    print("homeToChoosing click")
    frame.destroy()
    mainFrameInfo.screenTransition("homeToChoosing_Clicked")


def hangerClicked(event, message):
    print(event.widget)
    print("hanger click" + message)


def shopClicked(event, message):
    print(event.widget)
    print("shop click" + message)


def colorClicked(event, message):
    print(event.widget)
    print("event click" + message)


def bubblesClicked(event, message):
    print(event.widget)
    print("bubble click" + message)


image_list = []


class SetImage(object):
    def __init__(self):

        None

    def setImage(callbackName,  frame, imagePath, width, height, x, y, mainFrameInfo, bg="white"):
        global image_list
        # 画像のリサイズ
        # basewidth = width
        image = Image.open(imagePath)
        # wpercent = (basewidth/float(image.size[0]))
        # hsize = int((float(image.size[1])*float(wpercent)))
        image = image.resize((width, height), Image.ANTIALIAS)

        call = eval(callbackName)

        homeImage = ImageTk.PhotoImage(image)
        image_list.append(homeImage)
        frame.home = tk.Canvas(
            frame, width=width, height=height, background=bg, highlightthickness=0)
        frame.home.create_image(width/2, height/2, image=homeImage)
        frame.home.bind("<1>", lambda event, frame=frame, mainFrameInfo=mainFrameInfo:
                        call(event, frame, mainFrameInfo))
        # frame.home.pack()
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
