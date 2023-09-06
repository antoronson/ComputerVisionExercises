import cv2 as cv


ipImage = cv.imread("1.jpg")

cv.imshow("Test Display", ipImage)

k = cv.waitKey(0)