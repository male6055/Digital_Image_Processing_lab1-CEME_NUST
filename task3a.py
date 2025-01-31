import cv2
import numpy

def striped_image(image_width, image_height, line_width, gap_width):

    striped_image = numpy.ones((image_height, image_width), dtype=numpy.uint8) * 255

    current_line = 0
    while current_line < image_width:
        striped_image[:, current_line:current_line + line_width] = 0
        current_line += line_width + gap_width
    return striped_image

image_width = 400  # Width
image_height = 300  # Height
line_width = 20  # Width of black stripes
gap_width = 20  # Width of white gaps

striped_image = striped_image(image_width, image_height, line_width, gap_width)

cv2.imshow("Striped Image", striped_image)
cv2.waitKey()

