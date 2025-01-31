import numpy
import cv2

image = cv2.imread("task4image.png",0)
cv2.imshow("Original_image",image)
cv2.waitKey()

resized = cv2.resize(image,(512,512))
cv2.imshow("Resized_Image",resized)
cv2.waitKey()

h, w = image.shape[:2]
scale_factor = int(input("Enter down sampling factor: "))

new_h = h//scale_factor
new_w = w//scale_factor

down_sampled = numpy.zeros((new_h,new_w),dtype=numpy.uint8)
for i in range(new_h):
    for j in range(new_w):
        down_sampled[i][j] = image[i * scale_factor][j * scale_factor]

cv2.imshow("Down sampled_Image",down_sampled)
cv2.waitKey()