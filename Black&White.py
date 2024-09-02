import cv2
import numpy as np
#import ret

img=cv2.imread("DSCN0753.jpg",0)
ret,thresh1=cv2.threshold(img,127,255,cv2.THRESH_BINARY)
ret,thresh2=cv2.threshold(img,127,255,cv2.THRESH_BINARY_INV)
ret,thresh3=cv2.threshold(img,127,255,cv2.THRESH_TRUNC)
ret,thresh4=cv2.threshold(img,127,255,cv2.THRESH_TOZERO)
ret,thresh5=cv2.threshold(img,127,255,cv2.THRESH_TOZERO_INV)

cv2.imwrite("DSCN075.jpg",thresh1)
cv2.imwrite("DSCN075.jpg",thresh2)
cv2.imwrite("DSCN075.jpg",thresh3)
cv2.imwrite("DSCN073.jpg",thresh4)
cv2.imwrite("DSCN053.jpg",thresh5)

