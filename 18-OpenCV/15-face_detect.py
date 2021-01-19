from cv2 import cv2 as cv

img=cv.imread('Photos/group.jpg')
cv.imshow('Person',img)

gray=cv.cvtColor(img,cv.COLOR_BGR2GRAY)
cv.imshow('Gray',gray)

haar_cascade=cv.CascadeClassifier('haar_face.xml')

faces_rect=haar_cascade.detectMultiScale(gray,scaleFactor=1.1,minNeighbors=6)

print(f'Number of faces found={len(faces_rect)}')

for(x,y,w,h) in faces_rect:
    cv.rectangle(img,(x-5,y-5),(x+w+5,y+h+5),(0,255,0),thickness=2)

cv.imshow('Detected faces',img)

cv.waitKey(0)