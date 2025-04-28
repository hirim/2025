from picamera2 import Picamera2,Preview
import cv2
import numpy as np

picam2 = Picamera2()
picam2.configure(picam2.create_preview_configuration(main={'format' : 'RGB888','size': (640,480)}))
picam2.start()

while True:
    frame = picam2.capture_array()
    hsv = cv2.cvtColor(frame,cv2.COLOR_RGB2HSV)

    lower_red1 = np.array([0,100,100])
    upper_red1 = np.array([10,255,255])
    mask1 = cv2.inRange(hsv,lower_red1,upper_red1)

    lower_red2 = np.array([170,100,100])
    upper_red2 = np.array([180,255,255])
    mask2 = cv2.inRange(hsv,lower_red2,upper_red2)

    mask = cv2.bitwise_or(mask1,mask2)

    red_only = cv2.bitwise_and(frame,frame,mask=mask)

    cv2.imshow('Original',frame)
    cv2.imshow('Mask',mask)
    cv2.imshow('Result',red_only)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

picam2.stop()
cv2.destroyAllWindows()

