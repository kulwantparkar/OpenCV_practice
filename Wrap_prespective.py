import cv2
import numpy as np

img = cv2.imread("resources/amanda-jones-P787-xixGio-unsplash.jpg")
img = cv2.resize(img, (700, 500))
cv2.imshow("image", img)
points = []
def mouse_click(event, x, y, flag, param):
    if event == cv2.EVENT_LBUTTONDOWN:
        points.append([x, y])
        print([x, y])
        if len(points)==4:
            w = 400
            h = 500
            pt1 = np.float32(points)
            pt2 = np.float32([[0, 0], [w, 0], [0, h], [w, h]])
            matrix = cv2.getPerspectiveTransform(pt1, pt2)
            img_output = cv2.warpPerspective(img, matrix, (w, h))
            cv2.imshow("new_image", img_output)


cv2.setMouseCallback("image", mouse_click)
print(img.shape)
cv2.waitKey(0)
cv2.destroyAllWindows()
