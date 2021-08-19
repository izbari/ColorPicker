# -*- coding: utf-8 -*-
"""
Created on Thu Jul 15 00:00:09 2021

@author: zafer
"""

import cv2
import numpy as rp

def nothing(x):
    pass

img= rp.zeros((512,512,3),rp.uint8)

cv2.namedWindow("image")


cv2.createTrackbar("R", "image", 0, 255, nothing)
cv2.createTrackbar("G", "image", 0, 255, nothing)
cv2.createTrackbar("B", "image", 0, 255, nothing)

while(1):
    cv2.imshow("image",img)
    if cv2.waitKey(1) & 0xFF == 27:
        break;
       
    r= cv2.getTrackbarPos("R","image")    
    g= cv2.getTrackbarPos("G","image")    
    b= cv2.getTrackbarPos("B","image")


    img[:] = [b,g,r]    
            
cv2.destroyAllWindows()
