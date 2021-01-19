from cv2 import cv2 as cv
import matplotlib.pyplot as plt
import numpy as np  

img=cv.imread('Photos/cat.jpg')
cv.imshow('Cat',img)

gray=cv.cvtColor(img,cv.COLOR_BGR2GRAY)
cv.imshow('GRAY',gray)

blank=np.zeros(img.shape[:2],dtype='uint8')
cv.imshow('blank',blank)

mask=cv.circle(blank,(img.shape[1]//2,img.shape[0]//2-25),225,255,-1)
cv.imshow('Mask',mask)

masked=cv.bitwise_and(img,img,mask=mask)
cv.imshow('Masked Image',masked)

# # GRAYSCALE histogram
# gray_hist=cv.calcHist([gray],[0],mask,[256],[0,256])

# plt.figure()
# plt.title('Grayscale Histogram')
# plt.xlabel('Bins')
# plt.ylabel('No of pixels')
# plt.plot(gray_hist)
# plt.xlim([0,256])
# plt.show()



# Color Histogram
plt.figure()
plt.title('Color Histogram')
plt.xlabel('Bins')
plt.ylabel('No of pixels')
colors=('b','g','r')
for i,col in enumerate(colors):
    hist=cv.calcHist([img],[i],mask,[256],[0,256])
    plt.plot(hist,color=col)
    plt.xlim([0,256])

plt.show()


cv.waitKey(0)