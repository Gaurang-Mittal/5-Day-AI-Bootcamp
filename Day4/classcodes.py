import numpy as np
import matplotlib.pyplot as plt 
import cv2


img=cv2.imread("img.jpg")
print(img.shape)
# cv2.imshow("Image",img)
# cv2.waitKey(0)

img_resize=cv2.resize(img,(600,600))
cv2.imshow("Image",img_resize)
cv2.waitKey(0)


img_flip=cv2.flip(img_resize,0)
cv2.imshow("Image",img_flip)
cv2.waitKey(0)

img_crop=img_resize[100:400,100:400]
cv2.imshow("Image",img_crop)
cv2.waitKey(0)

cv2.destroyAllWindows()