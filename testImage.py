import cv2
import numpy as np

img = cv2.imread("images/bubbles1.png", -1)
img[:, :, 3] = np.where(np.all(img == 255, axis=-1), 0,
                        255)  # 白色のみTrueを返し、Alphaを0にする
cv2.imwrite('out.png', img)
cv2.imshow("test", img)
cv2.waitKey(0)
cv2.destroyAllWindows()
