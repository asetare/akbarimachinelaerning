import cv2
img = cv2.imread('IMG_9744.JPG',cv2.IMREAD_COLOR)
gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
cv2.namedWindow('Myimg',cv2.WINDOW_NORMAL)
cv2.imshow('Myimg',img)
while True:
     k=cv2.waitKey(0)
     if k==27:
         print("finish")
         cv2.destroyAllWindows()
         break
     elif k==ord('g'):
         cv2.imshow('Myimg',gray)
         cv2.imwrite('output_gray.jpg',gray)
         cv2.waitKey(0)
         break
cv2.destroyAllWindows()