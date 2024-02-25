import cv2 as cv
import numpy as np
scale=0.1

#Translation
def translate(frame,x,y):
    transMat=np.float32([[1,0,x],[0,1,y]])
    dimensions=(frame.shape[1],frame.shape[0])
    return cv.warpAffine(frame,transMat,dimensions)

img=cv.imread('Files\\Images\\Cat\\pexels-danielle-daniel-479009.jpg')
resized=cv.resize(img,(int(img.shape[1]*scale),int(img.shape[0]*scale)))

''' 
-x >>> Left
-y >>> Up
x >>> Right
y >>> Down
'''
translated=translate(resized,100,100)
cv.imshow('Translated',translated)

#Rotation
def rotate(frame,angle,rot=None):
    width,height=(frame.shape[1],frame.shape[0])
    if rot is None:
        rot=(width//2,height//2)
    rotMat=cv.getRotationMatrix2D(rot,angle,1.0)
    dimensions=(width,height)    

    return cv.warpAffine(frame,rotMat,dimensions)

rotate_img=rotate(resized,45)
cv.imshow('Rotated',rotate_img)

#Flipping
flip=cv.flip(resized,1)
cv.imshow('Flipping',flip)

cv.waitKey(0)