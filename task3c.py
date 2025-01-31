import cv2
import numpy

def grid_image(image_size, box_size, line_thickness):

    grid_image = numpy.ones((image_size[0], image_size[1]), dtype=numpy.uint8) * 255

    for y in range(0, image_size[0], box_size):
        grid_image[y:y + line_thickness, :] = 0

    for x in range(0, image_size[1], box_size):
        grid_image[:, x:x + line_thickness] = 0
    return grid_image

image_size = (400, 400)
box_size = 100
line_thickness = 25

grid_image = grid_image(image_size, box_size, line_thickness)

cv2.imshow("Grid Image", grid_image)
cv2.waitKey()

