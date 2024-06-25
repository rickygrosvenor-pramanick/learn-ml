import sys
import cv2 as cv
import numpy as np

def linear_filter(filename):
    window_name = 'filter2D Demo'
    image = cv.imread(filename)

    if image is None:
        print('Error opening image!')
        print('Usage: filter2D.py [image_name -- default lena.jpg] \n')
        return -1

    # Initialize ddepth argument for the filter
    ddepth = -1

    ind = 0

    while True:
        kernel_size = 3 + 2 * (ind % 5)
        kernel = np.ones((kernel_size, kernel_size), dtype=np.float32)
        kernel /= (kernel_size * kernel_size)

        # Apply filter
        dst = cv.filter2D(image, ddepth, kernel)
        cv.imshow(window_name, dst)

        c = cv.waitKey(500)
        if c == 27:
            break

        ind += 1

    return 0

linear_filter('lena.jpg')




