from cv2 import cv2 as cv
def rescaleFrame(frame,scale=0.75):
    ###### images,videos,live-videos
    width=int(frame.shape[1]*scale)
    height=int(frame.shape[0]*scale)

    dimensions=(width,height)

    return cv.resize(frame,dimensions,interpolation=cv.INTER_AREA)

def changeRes(width,height):
    ###### live-videos
    capture.set(3,width)
    capture.set(4,height)


###### reading image
img =cv.imread('Photos/cat.jpg')
resized_img=rescaleFrame(img)
cv.imshow('Image',img)
cv.imshow('Resized Image',resized_img)
cv.waitKey(0)


##### reading video
capture=cv.VideoCapture('Videos/dog.mp4')

while True:
    isTrue, frame=capture.read()

    frame_resized=rescaleFrame(frame,scale=.2)

    cv.imshow('Video',frame)
    cv.imshow('Video Resized',frame_resized)

    if(cv.waitKey(20) & 0xFF==ord('d')):
        break

capture.release()
cv.destroyAllWindows()