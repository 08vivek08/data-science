from cv2 import cv2 as cv

img=cv.imread('Photos/cat.jpg')
cv.imshow('Cat',img)

gray=cv.cvtColor(img,cv.COLOR_BGR2GRAY)
cv.imshow('Gray',gray)

# Simple Threshoding
threshold,thresh=cv.threshold(gray,100,255,cv.THRESH_BINARY)
cv.imshow('SIMPLE THRESHOLDED',thresh)

threshold,thresh_inv=cv.threshold(gray,100,255,cv.THRESH_BINARY_INV)
cv.imshow('SIMPLE THRESHOLDED INVERSE',thresh_inv)


# Adaptive Thresholding
adaptive_thresh=cv.adaptiveThreshold(gray,255,cv.ADAPTIVE_THRESH_MEAN_C,cv.THRESH_BINARY,5,2)
cv.imshow('Adapltive Thresholding',adaptive_thresh)


adaptive_thresh_inv=cv.adaptiveThreshold(gray,255,cv.ADAPTIVE_THRESH_GAUSSIAN_C,cv.THRESH_BINARY_INV,11,3)
cv.imshow('Adapltive Thresholding INVERSE',adaptive_thresh_inv)

cv.imwrite('Photos/cat2.jpg',adaptive_thresh_inv)






cv.waitKey(0)