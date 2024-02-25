import cv2 as cv
scale=0.1
import numpy as np

img=cv.imread('Files\\Images\\Dog\\pexels-chevanon-photography-1108099.jpg')
resized=cv.resize(img,(int(img.shape[1]*scale),int(img.shape[0]*scale)),interpolation=cv.INTER_AREA)
cv.imshow('Img',resized)

blank=np.zeros(resized.shape,'uint8')
cv.imshow('Blank',blank)

grey=cv.cvtColor(resized,cv.COLOR_BGR2GRAY)
cv.imshow('Grey',grey)

blur=cv.blur(grey,(3,3),cv.BORDER_DEFAULT)
cv.imshow('Blur',blur)

canny=cv.Canny(blur,125,175)
cv.imshow('Canny',canny)

ret,thresh=cv.threshold(grey,125,255,cv.THRESH_BINARY)
cv.imshow('Thresh',thresh)

contours,heirarchies=cv.findContours(canny,cv.RETR_LIST,cv.CHAIN_APPROX_SIMPLE)
print(f'{len(contours)} contour(s) found!')

drawn=cv.drawContours(blank,contours,-1,(0,0,255),1)
cv.imshow('Contours',drawn)

cv.waitKey(0)