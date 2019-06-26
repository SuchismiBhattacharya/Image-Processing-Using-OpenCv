#live video
import cv2
import numpy as np

cap=cv2.VideoCapture(0)
while(1):
         _,frame=cap.read()
         hsv=cv2.cvtColor(frame,cv2.COLOR_BGR2HSV)
         lower_blue=np.array([0,100,0])
         upper_blue=np.array([173,255,47])
         mask=cv2.inRange(hsv,lower_blue,upper_blue)
         res=cv2.bitwise_and(frame,frame,mask=mask)
         cv2.imshow('FRAME',frame)
         cv2.imshow('MASK',mask)
         cv2.imshow('RESULT',res)
         k=cv2.waitKey(5)& 0xFF
         if (k==27):
                     break
                    
cv2.destroyAllWindows()
