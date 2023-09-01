import cv2
import numpy

image_paths = ['1.jpg', '2.jpg']
img = []

for idx in range(len(image_paths)):
    img.append(cv2.imread(image_paths[idx]))
    img[idx]=cv2.resize(img[idx], (0,0), fx=0.4, fy=0.4)


stitchy = cv2.Stitcher.create()

(dummy, output) = stitchy.stitch(img)

if dummy != cv2.STITCHER_OK:
    print("Stitching is not successful")
else:
    print("Your Panorama is ready")

cv2.imshow("final result", output)

cv2.waitKey(0)


