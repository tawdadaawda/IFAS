from screens.fittingScreen import fittingScreen
from screens.topScreen import topScreen
from screens.choose2Screen import choose2Screen
from screens.chooseScreen import chooseScreen
from screens.completeScreen import completeScreen
from screens.fitting2Screen import fitting2Screen
from screens.propertyScreen import propertyScreen
from screens.purchaseScreen import purchaseScreen
from screens.shutterScreen import shutterScreen
from screens.similarOrSameScreen import similarOrSameScreen

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


def change_app(window):
    window.tkraise()


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

        #self.btn_snapshot = tk.Button(text='Snapshot', command=self.snapshot)
        # self.btn_snapshot.pack()
        #self.btn_snapshot.place(x=width/2 - 10, y=height/2)

        self.btn_snapshot = tk.Button(text='Snapshot', command=self.test)
        self.btn_snapshot.pack()
        self.btn_snapshot.place(x=width/2 - 10, y=height/2)

        # アイコンズ
        # クリックイベント

        # メインフレームのウィンドウにたいする位置を指定
        x = self.winfo_x()
        y = self.winfo_y()
        self.geometry("+%d+%d" % (x, y))

        # ページ遷移用フラグ
        self.screenTransitionFlag = None

    def screenTransition(self, flag):
        self.screenTransitionFlag = flag
        print(self.screenTransitionFlag)

        # if self.screenTransitionFlag == "homeClicked":
        #   self.createFittingScreen()

    # トップ画面生成
    def createTopScreen(self):
        topScreen.createScreen(self, width, height)

    def createChooseScreen(self):
        chooseScreen.createScreen(self, width, height)

    def createChoose2Screen(self):
        choose2Screen.createScreen(self, width, height)

    def createShutterScreen(self):
        shutterScreen.createScreen(self, width, height)

    def createFittingScreen(self):
        fittingScreen.createScreen(self, width, height)

    def createSimilarOrSameScreen(self):
        similarOrSameScreen.createScreen(self, width, height)

    def createPropertyScreen(self):
        propertyScreen.createScreen(self, width, height)

    def createFitting2Screen(self):
        fitting2Screen.createScreen(self, width, height)

    def createPurchaseScreen(self):
        purchaseScreen.createScreen(self, width, height)

    def createCompleteScreen(self):
        completeScreen.createScreen(self, width, height)

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

    def test(self):
        if self.screenTransitionFlag != "homeClicked":
            self.screenTransition("homeClicked")

        if self.screenTransitionFlag == "homeClicked":
            self.screenTransition("snapShot")

    def start(self):
        self.createFittingScreen()
        self.mainloop()


if __name__ == "__main__":

    app = App()
    app.start()
