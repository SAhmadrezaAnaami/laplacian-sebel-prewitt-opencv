# Created by Ahmadreza Anaami
import cv2
import numpy as np

img = cv2.imread("RES/1.jpg" , 0)
img = cv2.resize(img , (700,400))
blur = cv2.GaussianBlur(img,(3,3),0)

# laplacian

lap_1 = cv2.Laplacian(blur, cv2.CV_64F ) 
laplacian1 = lap_1/lap_1.max()


# sobel image  

sobelx = cv2.Sobel(blur,cv2.CV_64F,1,0,ksize=5)
sobely = cv2.Sobel(blur,cv2.CV_64F,0,1,ksize=5)
img_sobel = sobelx + sobely
# Prewitt image

kernelx = np.array([[1,1,1],[0,0,0],[-1,-1,-1]])
kernely = np.array([[-1,0,1],[-1,0,1],[-1,0,1]])
img_prewittx = cv2.filter2D(blur, -1, kernelx)
img_prewitty = cv2.filter2D(blur, -1, kernely)
img_prewitt = img_prewittx + img_prewitty


cv2.imshow("laplacian1" , laplacian1)
# cv2.imshow("sobelx" , sobelx)
# cv2.imshow("sobely" , sobely)
cv2.imshow("img_sobel" , img_sobel)
# cv2.imshow("img_prewittx" , img_prewittx)
# cv2.imshow("img_prewitty" , img_prewitty)
cv2.imshow("img_prewitt" , img_prewitt)
cv2.waitKey()
cv2.destroyAllWindows()
