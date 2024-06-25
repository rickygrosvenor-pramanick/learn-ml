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
    lst = [0 for _ in range(0, 1206)] + [1]
    print(lst[-1])
    while True:
        kernel = np.array([[0 for _ in range(0, 1207)],
                           lst,
                           [0 for _ in range(0, 1207)]
                           ])
        # kernel /= (kernel_size * kernel_size)

        # Apply filter
        dst = cv.filter2D(image, ddepth, kernel)
        cv.imshow(window_name, dst)

        c = cv.waitKey(500)
        if c == 27:
            break

        ind += 1

    return 0

linear_filter('eye.jpg')
