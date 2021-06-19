from numpy import real, true_divide
from inference import inferenceEngine
import cv2

inferenceEngine = inferenceEngine(r"C:\Program\IFAS\IFAS\IR\face-detection-retail-0005")
image = cv2.imread(r"C:\Program\IFAS\IFAS\IR\test.jpg")
output = inferenceEngine.infer(image)

for detection in output:
    confidence = float(detection[2])

    xmin = int(detection[3] * image.shape[1])
    ymin = int(detection[4] * image.shape[0])
    xmax = int(detection[5] * image.shape[1])
    ymax = int(detection[6] * image.shape[0])
 
    if confidence > 0.5:
        cv2.rectangle(image, (xmin, ymin), (xmax, ymax), color=(240, 180, 0), thickness=3)

cv2.imshow("test", image)
cv2.waitKey(0)
cv2.destroyAllWindows()