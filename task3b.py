import cv2
import numpy

def border_box(image_size, box_size):

    image = numpy.zeros((image_size[0], image_size[1]), dtype=numpy.uint8)

    start_y = (image_size[0] - box_size[0])//2
    start_x = (image_size[1] - box_size[1])//2
    end_y = start_y + box_size[0]
    end_x = start_x + box_size[1]

    image[start_y:end_y, start_x:end_x] = 255
    return image

image_size = (400, 400)
box_size = (100, 100)

box_image = border_box(image_size, box_size)

cv2.imshow("Image", box_image)
cv2.waitKey()

