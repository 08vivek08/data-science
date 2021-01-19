from cv2 import cv2 as cv 
import matplotlib.pyplot as plt

img=cv.imread('Photos/cat.jpg')
cv.imshow('Cat',img)

# BGR to GRAYSCALE
gray=cv.cvtColor(img,cv.COLOR_BGR2GRAY)
cv.imshow('Gray',gray)

# BGR to GRAYSCALE
gray_bgr=cv.cvtColor(gray,cv.COLOR_GRAY2BGR)
cv.imshow('Gray to BGR',gray_bgr)


# BGR to HSV
hsv=cv.cvtColor(img,cv.COLOR_BGR2HSV)
cv.imshow('HSV',hsv)

# HSV to BGR
hsv_bgr=cv.cvtColor(hsv,cv.COLOR_HSV2BGR)
cv.imshow('HSV to BGR',hsv_bgr)

# BGR to L*a*b
lab=cv.cvtColor(img,cv.COLOR_BGR2LAB)
cv.imshow('LAB',lab)

# LAB to BGR
lab_bgr=cv.cvtColor(lab,cv.COLOR_LAB2BGR)
cv.imshow('LAB to BGR',lab_bgr)

# BGR to RGB
rgb=cv.cvtColor(img,cv.COLOR_BGR2RGB)
cv.imshow('RGB',rgb)

# OpenCv read images by inverting color and because pyplot has no idea that it was a BGR image so it did't converted it to RGB
plt.imshow(img)
plt.title('bgr from cv2')
plt.show()

plt.imshow(rgb)
plt.title('rgb from cv2')
plt.show()

cv.waitKey(0)