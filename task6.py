import numpy
import cv2

image = cv2.imread("lab1.png",0)
cv2.imshow("Original_image",image)
cv2.waitKey()

h, w = image.shape[:2]
image_mirrored = numpy.zeros((h,w),dtype=numpy.uint8)

for i in range(h // 2):
    for j in range(w):
        image_mirrored[i][j] = image[i][j]
        if i==h//2:
            continue
        else:
            image_mirrored[h-i-2][j] = image[i][j]

cv2.imshow("Mirrored Image", image_mirrored)
cv2.waitKey(0)

