
import tkinter as tk
from tkinter import ttk
import cv2
import PIL.Image, PIL.ImageTk
from PIL import ImageTk, Image
from tkinter import font
import time
from cv.realsense import Realsense
from inference.inference import inferenceEngine

filename = ""
isStop = 0
class Application(tk.Frame):
    def __init__(self,master, video_source=0):
        super().__init__(master)
        self.model = r"C:\Program\IFAS\IFAS\IR\face-detection-retail-0005"
        self.inferenceEngine = inferenceEngine(self.model)

        self.master.geometry("700x700")
        self.master.title("Tkinter with Video Streaming and Capture")

        # ---------------------------------------------------------
        # Font
        # ---------------------------------------------------------
        self.font_frame = font.Font( family="Meiryo UI", size=15, weight="normal" )
        self.font_btn_big = font.Font( family="Meiryo UI", size=20, weight="bold" )
        self.font_btn_small = font.Font( family="Meiryo UI", size=15, weight="bold" )

        self.font_lbl_bigger = font.Font( family="Meiryo UI", size=45, weight="bold" )
        self.font_lbl_big = font.Font( family="Meiryo UI", size=30, weight="bold" )
        self.font_lbl_middle = font.Font( family="Meiryo UI", size=15, weight="bold" )
        self.font_lbl_small = font.Font( family="Meiryo UI", size=12, weight="normal" )

        # ---------------------------------------------------------
        # Open the video source
        # ---------------------------------------------------------

        self.realsense = Realsense()
        self.realsense.configurePipeline()
        self.realsense.startStream()
        self.width = 640
        self.height = 480

        # ---------------------------------------------------------
        # Widget
        # ---------------------------------------------------------

        self.create_widgets()

        # ---------------------------------------------------------
        # Canvas Update
        # ---------------------------------------------------------

        self.delay = 15 #[mili seconds]
        self.update()


    def create_widgets(self):
        #Frame_Camera
        global filename
        self.frame_cam = tk.LabelFrame(self.master, text = filename, font=self.font_frame)
        self.frame_cam.place(x = 10, y = 10)
        self.frame_cam.configure(width = self.width+100, height = self.height+50)
        self.frame_cam.grid_propagate(0)


        #Canvas
        self.canvas1 = tk.Canvas(self.frame_cam)
        self.canvas1.configure( width= self.width, height=self.height)
        self.canvas1.grid(column= 0, row=0,padx = 10, pady=10)

        # Frame_Button
        self.frame_btn = tk.LabelFrame( self.master, text='Control', font=self.font_frame )
        self.frame_btn.place( x=10, y=550 )
        self.frame_btn.configure( width=self.width + 30, height=120 )
        self.frame_btn.grid_propagate( 0 )

        #Snapshot Button
        self.btn_snapshot = tk.Button( self.frame_btn, text='Snapshot', font=self.font_btn_big)
        self.btn_snapshot.configure(width = 15, height = 1, command=self.press_snapshot_button)
        self.btn_snapshot.grid(column=0, row=0, padx=30, pady= 10)

        # Close
        self.btn_close = tk.Button( self.frame_btn, text='Close', font=self.font_btn_big )
        self.btn_close.configure( width=15, height=1, command=self.press_close_button )
        self.btn_close.grid( column=1, row=0, padx=20, pady=10 )

    def update(self):
        #Get a frame from the video source
        color_img, bg_removed_img = self.realsense.getFrame()

        frame = cv2.cvtColor(color_img, cv2.COLOR_BGR2RGB)
        global isStop
        if isStop == 0:
            
            self.photo = PIL.ImageTk.PhotoImage(image = PIL.Image.fromarray(frame))
        else:
            myImage = ImageTk.PhotoImage(Image.open(filename))
            self.photo = myImage
    

        #self.photo -> Canvas
        self.canvas1.create_image(0,0, image= self.photo, anchor = tk.NW)

        self.master.after(self.delay, self.update)

    def press_snapshot_button(self):
        # Get a frame from the video source
        color_img, bg_removed_img = self.realsense.getFrame()
        frame1 = cv2.cvtColor(bg_removed_img, cv2.COLOR_BGR2RGB)

        output = self.inferenceEngine.infer(frame1)

        for detection in output:
            confidence = float(detection[2])

            xmin = int(detection[3] * frame1.shape[1])
            ymin = int(detection[4] * frame1.shape[0])
            xmax = int(detection[5] * frame1.shape[1])
            ymax = int(detection[6] * frame1.shape[0])
        
            if confidence > 0.5:
                cv2.rectangle(frame1, (xmin, ymin), (xmax, ymax), color=(240, 180, 0), thickness=3)


        cv2.imwrite( "frame-" + time.strftime( "%Y-%d-%m-%H-%M-%S" ) + ".jpg",
                     cv2.cvtColor( frame1, cv2.COLOR_BGR2RGB ) )
        global filename
        global isStop
        filename =  "frame-" + time.strftime( "%Y-%d-%m-%H-%M-%S" ) + ".jpg"
        isStop = 1

    def press_close_button(self):
        self.master.destroy()
        self.vcap.release()





def main():
    root = tk.Tk()
    app = Application(master=root)#Inherit
    app.mainloop()

if __name__ == "__main__":
    main()
