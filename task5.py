import numpy
import cv2

r=int(input("Enter R: ",))
c=int(input("Enter C: ",))
r_col=r//8
c_col=c//8
a = numpy.ones((r,c,3),dtype=numpy.uint8)*255

a[0:r_col,0:c_col,:]=[0,0,0] #black
a[0:r_col,c-c_col:c,:]=[255,0,0] #blue
a[r-r_col:r,c-c_col:c,:]=[0,255,0] #green
a[r-r_col:r,0:c_col,:]=[0,0,255] #red

cv2.imshow('win',a)
cv2.waitKey()

