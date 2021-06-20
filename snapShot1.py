import cv2
import tkinter as tk
from PIL import Image, ImageTk
import tkinter.ttk as ttk
import time

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

        self.btn_snapshot = tk.Button(text='Snapshot', command = self.snapshot)
        self.btn_snapshot.pack()
        self.btn_snapshot.place(x= width/2 - 10, y= height/2)

        # アイコンズ
        # クリックイベント
        def homeClicked(event):
            print("home click")
        def hangerClicked(event):
            print("hanger click")
        def shopClicked(event):
            print("shopClicked")

        iconSize = 50
        
        self.homeImage = ImageTk.PhotoImage(Image.open("images/home.png"))
        self.home = tk.Canvas(self,width=iconSize, height=iconSize)
        self.home.create_image(0,0, image=self.homeImage)
        self.home.bind("<1>", homeClicked)
        self.home.pack()
        self.home.place(x= width - iconSize - 20, y= 20)

        self.hangerImage = ImageTk.PhotoImage(Image.open("images/hanger.png"))
        self.hanger = tk.Canvas(self,width=iconSize, height=iconSize)
        self.hanger.create_image(0,0, image=self.hangerImage)
        self.hanger.bind("<1>", hangerClicked)
        self.hanger.pack()
        self.hanger.place(x= width - iconSize - 20, y= 1*(iconSize + 10) + 20)

        self.shopImage = ImageTk.PhotoImage(Image.open("images/cart.png"))
        self.shopping = tk.Canvas(self,width=iconSize, height=iconSize)
        self.shopping.create_image(0,0, image=self.shopImage)
        self.shopping.bind("<1>", shopClicked)
        self.shopping.pack()
        self.shopping.place(x= width - iconSize - 20, y=  2*(iconSize + 10) + 20)

        def colorBtnClicked(event):
            print("colorBtn click")

        # colors
        # 初めはカラーボタンひとつ
        self.colorBtnImage = ImageTk.PhotoImage(Image.open("images/colors1.png"))
        self.colorBtn = tk.Canvas(self,width=30, height=30)
        self.colorBtn.create_image(0,0, image=self.colorBtnImage)
        self.colorBtn.bind("<1>", colorBtnClicked)
        self.colorBtn.pack()
        self.colorBtn.place(x=20, y= 20)

        # アイテムをならべるフレームの作成と配置
        bubblesW = 540 - 20*2
        bubblesH = 150
        self.bubblesImage = ImageTk.PhotoImage(Image.open("images/bubbles1.png"))
        self.bubbles = tk.Canvas(self,width=bubblesW, height=bubblesH)
        self.bubbles.create_image(0,0, image=self.bubblesImage)
        self.bubbles.pack()
        self.bubbles.place(x= width/2 - bubblesW/2, y= height - bubblesH - 20)


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
                self.canvas.create_image(-1400/2 + 300, 0, image=self.tk_frame, anchor='nw')
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

        cv2.imwrite( "frame-" + time.strftime( "%Y-%d-%m-%H-%M-%S" ) + ".jpg",
                     cv2.cvtColor( frame1, cv2.COLOR_BGR2RGB ) )
        global filename
        filename =  "frame-" + time.strftime( "%Y-%d-%m-%H-%M-%S" ) + ".jpg"
        self.capture_flag = True
        print("caputure now\n" +str(filename))

    def start(self):
        self.mainloop()


if __name__ == "__main__":

    app = App()
    app.start()
