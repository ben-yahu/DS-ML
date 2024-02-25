import cv2 as cv

img=cv.imread("Files\\Images\\Cat\\pexels-krysten-merriman-20787.jpg")
# cv.imshow('Img',img)

def rescaleFrame(frame,scale=0.75):
    height=int(frame.shape[0]*scale)
    width=int(frame.shape[1]*scale)
    dimensions=(width,height)

    return cv.resize(frame,dimensions,interpolation=cv.INTER_AREA)

def changeRes(width,height):
    capture.set(3,width)
    capture.set(4,height)
    

resized_image=rescaleFrame(img,scale=0.2)
cv.imshow('Image_Resized',resized_image)

capture=cv.VideoCapture('Files\\Videos\\dog_resting_on_grass_field (1080p).mp4')

while True:
    isTrue,frame=capture.read()
    frame_resized=rescaleFrame(frame,scale=0.2)
    cv.imshow('Video Resized',frame_resized)

    if cv.waitKey(20) & 0xFF==ord('e'):
        break

capture.release()
cv.destroyAllWindows()

cv.waitKey(0)

