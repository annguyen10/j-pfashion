import numpy as np
import cv2 as cv
import matplotlib.pyplot as plt
# Load file hinh
img = cv.imread('vuong-quoc-anh.jpg',cv.IMREAD_COLOR)

# show file hinh
cv.imshow('image',img)
cv.waitKey(0)
cv.destroyAllWindows()
