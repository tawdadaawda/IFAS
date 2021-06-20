import cv2
import tkinter as tk
from PIL import Image, ImageTk
import tkinter.ttk as ttk
import time
from components.setImage import SetImage

# define valiable
width = 540
height = 800
filename = ""


class SsFrame(ttk.LabelFrame):
    def __init__(self, master=None, text=None):
        super(SsFrame, self).__init__(master, text=text)
        # self.start_b = ttk.Button(self, text="start", command=master.start_cap)
        # self.stop_b = ttk.Button(self, text="stop", command=master.stop_cap)

        # self.start_b.grid(row=0, column=0)
        # self.stop_b.grid(row=0, column=1)


class App(tk.Tk):
    def __init__(self):
        super(App, self).__init__()
        # root configuration
        self.title("VideoCapture")
        self.resizable(width=False, height=False)
        self.capture_flag = False

        # valiables configuration
        self.capture = cv2.VideoCapture(0)
        self.after_id = self.after(10, self.update_cap)

        # canvas configuration
        self.canvas = tk.Canvas(self, width=width, height=height)
        self.canvas.create_rectangle(0, 0, width, height, fill="black")
        self.canvas.pack()

        # ss_frame configuration
        self.ss_frame = SsFrame(self, text="start_stop_buttons")
        self.ss_frame.pack()

        self.btn_snapshot = tk.Button(text='Snapshot', command=self.snapshot)
        self.btn_snapshot.pack()
        self.btn_snapshot.place(x=width/2 - 10, y=height/2)

        # アイコンズ
        # クリックイベント

        # メインフレームのウィンドウにたいする位置を指定
        x = self.winfo_x()
        y = self.winfo_y()
        self.geometry("+%d+%d" % (x, y))

    def setImage(frame):
        iconSize = 50
        colorButtonSize = 30
        bubblesW = 540 - 20*2
        bubblesH = 150

        # トップレベル生成
        topLevelWindow = SetImage.createToplevel(
            frame=frame,
            width=width,
            height=height,
            x=frame.winfo_x(),
            y=frame.winfo_y()
        )

        # ホームボタンクリック処理
        SetImage.setImage(callbackName="homeClicked",
                          frame=topLevelWindow,
                          imagePath=r"../images/home.png",
                          width=iconSize,
                          height=iconSize,
                          x=width - iconSize - 20,
                          y=20
                          )

        # ハンガーボタンクリック処理
        SetImage.setImage(callbackName="hangerClicked",
                          frame=topLevelWindow,
                          imagePath=r"../images/hanger.png",
                          width=iconSize,
                          height=iconSize,
                          x=width - 50 - 20,
                          y=1*(iconSize + 10) + 20
                          )

        # カートボタンクリック処理
        SetImage.setImage(callbackName="shopClicked",
                          frame=topLevelWindow,
                          imagePath=r"../images/cart.png",
                          width=iconSize,
                          height=iconSize,
                          x=width - iconSize - 20,
                          y=2*(iconSize + 10) + 20
                          )

        # カラーボタンクリック処理
        SetImage.setImage(callbackName="colorClicked",
                          frame=topLevelWindow,
                          imagePath=r"../images/colors1.png",
                          width=colorButtonSize,
                          height=colorButtonSize,
                          x=20,
                          y=20)

        # バブルボタンクリック処理
        SetImage.setImage(callbackName="bubblesClicked",
                          frame=topLevelWindow,
                          imagePath=r"../images/bubbles1.png",
                          width=bubblesW,
                          height=bubblesH,
                          x=width/2 - bubblesW/2,
                          y=height - bubblesH - 20
                          )

    # def start_cap(self):
    # if not self.capture_flag:
    #     self.capture_flag = True
    #     self.capture = cv2.VideoCapture(0)
    #     self.after_id = self.after(10, self.update_cap)

    def update_cap(self):
        ret, frame = self.capture.read()
        if ret:
            if self.capture_flag == False:
                frame = cv2.resize(frame, (1400, 800))
                self.tk_frame = ImageTk.PhotoImage(
                    Image.fromarray(
                        cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
                    )
                )
                self.canvas.create_image(-1400/2 + 300,
                                         0, image=self.tk_frame, anchor='nw')
            else:
                myImage = ImageTk.PhotoImage(Image.open(filename))
                self.photo = myImage

        else:
            self.canvas.create_text(width/2, height/2, text="None")

        self.after_id = self.after(10, self.update_cap)

    def snapshot(self):
        # Get a frame from the video source
        _, frame = self.capture.read()
        frame1 = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

        cv2.imwrite("frame-" + time.strftime("%Y-%d-%m-%H-%M-%S") + ".jpg",
                    cv2.cvtColor(frame1, cv2.COLOR_BGR2RGB))
        global filename
        filename = "frame-" + time.strftime("%Y-%d-%m-%H-%M-%S") + ".jpg"
        self.capture_flag = True
        print("caputure now\n" + str(filename))

    def start(self):
        self.setImage()
        self.mainloop()


if __name__ == "__main__":

    app = App()
    app.start()
