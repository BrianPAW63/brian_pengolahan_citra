import cv2 as cv

image = cv.imread('zoro.png')
cv.imshow('Image RGB',image)

grey_image = cv.cvtColor(image,cv.COLOR_RGB2GRAY)
cv.imshow('Image Grayscale', grey_image)

_,binary_image = cv.threshold(grey_image,127, 255, cv.THRESH_BINARY)
cv.imshow('Image Binary', binary_image)

cv.waitKey(0)
cv.destroyAllWindows()