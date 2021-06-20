from components.setImage import SetImage


class topScreen(object):
    def __init__(self):

        None

    def createScreen(frame, width, height):

        # トップレベル生成
        topLevelWindow = SetImage.createToplevel(
            frame=frame,
            width=width,
            height=height,
            x=frame.winfo_x(),
            y=frame.winfo_y(),
            bg="light green"
        )

        # ホームボタンクリック処理
        SetImage.setImage(callbackName="homeToChoosing",
                          frame=topLevelWindow,
                          imagePath=r"../images/home/p_HOME.png",
                          width=width,
                          height=height,
                          x=0,
                          y=0,
                          mainFrameInfo=frame
                          )
