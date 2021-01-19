from cv2 import cv2 as cv 
import numpy as np 

img=cv.imread('Photos/cat.jpg')
cv.imshow('Cat',img)

# To draw contours
blank1=np.zeros(img.shape,dtype='uint8')
# cv.imshow('Blank1',blank1)
blank2=np.zeros(img.shape,dtype='uint8')
# cv.imshow('Blank2',blank2)


gray=cv.cvtColor(img,cv.COLOR_BGR2GRAY)
cv.imshow('Gray',gray)

canny=cv.Canny(gray,125,125)
cv.imshow('Canny Edges',canny)

contours,hierarchies=cv.findContours(canny,cv.RETR_LIST,cv.CHAIN_APPROX_NONE)
print(f'{len(contours)} contour(s) found in canny!')
cv.drawContours(blank1,contours,-1,(255,255,255),1)
cv.imshow('Contours drawn for canny',blank1)


ret,thresh=cv.threshold(gray,125,255,cv.THRESH_BINARY)
cv.imshow('Thresh',thresh)

contours,hierarchies=cv.findContours(thresh,cv.RETR_LIST,cv.CHAIN_APPROX_NONE)
print(f'{len(contours)} contour(s) found in thresh!')
cv.drawContours(blank2,contours,-1,(255,255,255),1)
cv.imshow('Contours drawn for thresh',blank2)

cv.waitKey(0)