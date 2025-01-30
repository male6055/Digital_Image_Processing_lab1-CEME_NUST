import numpy
import cv2

r=int(input("Enter R",))
c=int(input("Enter C",))
a = numpy.ones((r,c,3),dtype=numpy.uint8)*255
cv2.imshow('win',a)
cv2.waitKey()

a[0:50,0:50,:]=[0,0,255]

a[0:50,c-50:c,:]=[0,255,0]

a[r-50:r,c-50:c,:]=[255,255,0]
a[0:50,c:c-50,:]=[255,255,0]

cv2.imshow('win',a)
cv2.waitKey()

