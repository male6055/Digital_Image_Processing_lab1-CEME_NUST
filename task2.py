import numpy
import cv2

r=500
c=500
a = numpy.ones((r,c),dtype=numpy.uint8)

cv2.imshow('win',a*255)
cv2.waitKey()

#padded_image= [c+10 for _ in range (r+10)]
r=510
c=510
a[0:5,0:5,0]

cv2.imshow('win',a)
cv2.waitKey()