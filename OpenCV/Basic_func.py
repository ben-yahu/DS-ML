import cv2 as cv

img=cv.imread('Files\\Images\\Cat\\pexels-evg-kowalievska-1170986.jpg')

def resize(frame,scale=0.5):
    height=int(frame.shape[0]*scale)
    width=int(frame.shape[1]*scale)
    dimensions=(width,height)

    return cv.resize(frame,dimensions,interpolation=cv.INTER_AREA) 

res_img=resize(img,0.2)

#How to grayscale an image
grey=cv.cvtColor(res_img,cv.COLOR_BGR2GRAY)
cv.imshow('Grey',grey)

#Blur
blur=cv.GaussianBlur(res_img,(5,5),cv.BORDER_DEFAULT)
cv.imshow('Blur',blur)

#Edge Cascade
casc=cv.Canny(res_img,125,175)
cv.imshow('Canny',casc)

#Dilated
dila=cv.dilate(casc,(7,7),iterations=3)
cv.imshow('Dilated',dila)

#Eroding
erod=cv.erode(dila,(7,7),iterations=3)
cv.imshow('Erode',erod)

#Cropped
crop=res_img[100:,100:]
cv.imshow('Cropped',crop)

cv.waitKey(0)