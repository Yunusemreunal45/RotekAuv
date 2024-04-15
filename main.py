import cv2 
import numpy as np

camera = cv2.VideoCapture(2)

while camera.isOpened():
    _, frame = camera.read()
    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
    lower = np.array[110,50,50]
    upper = np.array[130,255,255]
    
    mask = cv2.inRange(hsv,lower,upper)
    
    cv2.imshow("frame",frame)
    cv2.imshow("hsv",hsv)
    if cv2.waitKey(1)==ord("q"):
       break
   
cv2.destroyAllWindows()   