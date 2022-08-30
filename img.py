import sys
import cv2
img = cv2.imread("monk.jpg", cv2.IMREAD_ANYCOLOR)
 
while True:
    cv2.imshow("Monke", img)
    cv2.waitKey(0)
    sys.exit()
 
cv2.destroyAllWindows()
