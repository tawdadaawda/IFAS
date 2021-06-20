from components.setImage import SetImage


class fittingScreen(object):
    def __init__(self):

        None

    def createScreen(frame, width, height):
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
                          y=20,
                          mainFrameInfo=frame
                          )

        # ハンガーボタンクリック処理
        SetImage.setImage(callbackName="hangerClicked",
                          frame=topLevelWindow,
                          imagePath=r"../images/hanger.png",
                          width=iconSize,
                          height=iconSize,
                          x=width - 50 - 20,
                          y=1*(iconSize + 10) + 20,
                          mainFrameInfo=frame
                          )

        # カートボタンクリック処理
        SetImage.setImage(callbackName="shopClicked",
                          frame=topLevelWindow,
                          imagePath=r"../images/cart.png",
                          width=iconSize,
                          height=iconSize,
                          x=width - iconSize - 20,
                          y=2*(iconSize + 10) + 20,
                          mainFrameInfo=frame
                          )

        # カラーボタンクリック処理
        SetImage.setImage(callbackName="colorClicked",
                          frame=topLevelWindow,
                          imagePath=r"../images/colors1.png",
                          width=colorButtonSize,
                          height=colorButtonSize,
                          x=20,
                          y=20,
                          mainFrameInfo=frame
                          )

        # バブルボタンクリック処理
        SetImage.setImage(callbackName="bubblesClicked",
                          frame=topLevelWindow,
                          imagePath=r"../images/bubbles1.png",
                          width=bubblesW,
                          height=bubblesH,
                          x=width/2 - bubblesW/2,
                          y=height - bubblesH - 20,
                          mainFrameInfo=frame
                          )
