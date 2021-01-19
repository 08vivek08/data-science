from cv2 import cv2 as cv
import numpy as np 

img=cv.imread('Photos/cat.jpg')
cv.imshow('image',img)

print('img.shape',img.shape)

blank=np.zeros((img.shape[:2]),dtype='uint8')
# cv.imshow('blank',blank)
print('blank.shape',blank.shape)

b,g,r=cv.split(img)

print('b.shape',b.shape)
print('g.shape',g.shape)
print('r.shape',r.shape)


blue=cv.merge([b,blank,blank])
green=cv.merge([blank,g,blank])
red=cv.merge([blank,blank,r])

print('blue.shape',blue.shape)
print('green.shape',green.shape)
print('red.shape',red.shape)


cv.imshow('blue',blue)
cv.imshow('green',green)
cv.imshow('red',red)

bgr=cv.merge([b,g,r])
cv.imshow('bgr',bgr)

cv.waitKey(0)
