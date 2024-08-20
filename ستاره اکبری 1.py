import cv2
import numpy as np
img = cv2.imread('IMG_9744.JPG')
new_width = img.shape[1] // 2
new_height = img.shape[0] // 2
new_img = np.zeros((new_height, new_width, 3), dtype=np.uint8)
for i in range(new_height):
    for j in range(new_width):
        new_img[i, j] = img[i*2, j*2]
cv2.imshow('Resized Image', new_img)
cv2.waitKey(0)
cv2.destroyAllWindows()