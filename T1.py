#loading Images and showing Images
import cv2
import numpy as np
import matplotlib.pyplot as plt
url=input('Enter the image you want to process:')
img=cv2.imread(url,-1)
cv2.imshow('My first image',img)
#showing image using matplotlib
plt.imshow(img,cmap='gray',interpolation='bicubic')
plt.show()
cv2.waitKey(0)
cv2.destroyAllWindows()

