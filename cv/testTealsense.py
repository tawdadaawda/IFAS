from numpy import real, true_divide
from realsense import Realsense
import realsense
import cv2

realsense = Realsense()
realsense.configurePipeline()
realsense.startStream()
while True:
    color_img, bg_removed_img = realsense.getFrame()
    cv2.imshow("image", color_img)

    key = cv2.waitKey(1)
    if key == ord('q'):
        cv2.destroyAllWindows()
        break
