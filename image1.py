#image
import cv2
import numpy as np

cap=cv2.imread('green.jpg')
while(1):
            hsv=cv2.cvtColor(cap,cv2.COLOR_BGR2HSV)
            lower_blue=np.array([0,100,0])
            upper_blue=np.array([173,255,47])
            mask=cv2.inRange(hsv,lower_blue,upper_blue)
            res=cv2.bitwise_and(cap,cap,mask=mask)
            cv2.imshow('FRAME',cap)
            cv2.imshow('MASK',mask)
            cv2.imshow('RESULT',res)
            k=cv2.waitKey(5)& 0xFF
            if (k==27):
                        break;
cv2.destroyAllWindows()

