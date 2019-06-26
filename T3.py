#Drawing and Writing on Images using cv2
import cv2
import numpy as np
img=cv2.imread('green.jpg')
cv2.line(img,(0,0),(200,300),(255,255,255),10)
cv2.imshow('Result after drawing a line',img)
cv2.waitKey(0)
cv2.destroyAllWindows()
