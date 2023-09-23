import cv2
import numpy as np


def empty(a):
    pass


cv2.namedWindow("Trackbar")
cv2.resizeWindow("Trackbar", 500, 250)

cv2.createTrackbar("hue min", "Trackbar", 170, 179, empty)
cv2.createTrackbar("hue max", "Trackbar", 179, 179, empty)
cv2.createTrackbar("sat min", "Trackbar", 20, 255, empty)
cv2.createTrackbar("sat max", "Trackbar", 130, 255, empty)
cv2.createTrackbar("val min", "Trackbar", 178, 255, empty)
cv2.createTrackbar("val max", "Trackbar", 255, 255, empty)

while True:
    img = cv2.imread("resources/kidpid-1024x724.jpg")
    img = cv2.resize(img, (600, 400))
    img_hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)

    hue_lower = cv2.getTrackbarPos("hue min", 'Trackbar')
    hue_upper = cv2.getTrackbarPos('hue max', 'Trackbar')
    saturation_lower = cv2.getTrackbarPos('sat min', 'Trackbar')
    saturation_upper = cv2.getTrackbarPos('sat max', 'Trackbar')
    value_lower = cv2.getTrackbarPos('val min', 'Trackbar')
    value_upper = cv2.getTrackbarPos('val max', 'Trackbar')
    print(hue_lower, hue_upper, saturation_lower, saturation_upper, value_lower, value_upper)

    lower = np.array([hue_lower, saturation_lower, value_lower])
    high = np.array([hue_upper, saturation_upper, value_upper])
    mask = cv2.inRange(img_hsv, lower, high)
    result = cv2.bitwise_and(img, img, mask=mask)

    cv2.imshow("colours", img)
    cv2.imshow("hsv_img", img_hsv)
    cv2.imshow("Mask", mask)
    cv2.imshow("Result", result)
    cv2.waitKey(1)


img = cv2.destroyAllWincdows()