#loading video from video cam
import cv2
import numpy as np
cap=cv2.VideoCapture(0)
fourcc=cv2.VideoWriter_fourcc(*'XVID')
out=cv2.VideoWriter('Output.avi',fourcc, 20.0,(640,480))
out1=cv2.VideoWriter('Output1.avi',fourcc, 20.0,(640,480))
while True:
            ret,frame=cap.read()
            gray=cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
            cv2.imshow('Original',frame)
            cv2.imshow('Gray',gray)
            out.write(frame)
            out1.write(gray)
            if cv2.waitKey(1)& 0xFF==ord('q'):
                                                break

cap.release()
out.release()
out1.release()
cv2.destroyAllWindows()
