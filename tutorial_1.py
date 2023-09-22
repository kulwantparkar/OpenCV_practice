import cv2
import numpy as np

kernel = np.ones((5, 5))
img = cv2.imread("resources/20230824.jpg")
img = cv2.resize(img, (400, 400))

#for coloring the image:
imgColor = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

#for blur
img_blur = cv2.GaussianBlur(imgColor, (3, 3), 0)

#for edges
img_corner = cv2.Canny(img_blur, 150, 150)

#for edges thickness
img_thick_corner = cv2.dilate(img_corner, kernel, iterations=1)

#for edeges thiness
img_thin_corner = cv2.erode(img_thick_corner, kernel, iterations=1)


img = cv2.imshow("Land", img_thin_corner)
img = cv2.waitKey(0)
img = cv2.destroyAllWindows()

