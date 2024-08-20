import cv2
img = cv2.imread('IMG_9744.JPG')
cv2.namedWindow('Img',cv2.WINDOW_NORMAL)
cv2.imshow('Img',img)
k = cv2.waitKey(5000)
if k == 27:
    cv2.destroyAllWindows()
else:
    gray_img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    cv2.imshow('Img', gray_img)
    cv2.waitKey(2000)
    cv2.imwrite('output_gray.jpg', gray_img)
    print('No key')
cv2.destroyAllWindows()