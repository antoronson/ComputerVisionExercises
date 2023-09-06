import cv2 as cv
import numpy as np

class processImage:


    def getPanorama(imageList):
        resizedImage = []

        for iDx in range(len(imageList)):
            resizedImage.append(cv.imread(imageList[iDx]))
            resizedImage[iDx] = cv.resize(resizedImage[iDx], (0,0), fx=0.4, fy=0.4)

            imageStitcher = cv.Stitcher.create()

        (nError, output) = imageStitcher.stitch(resizedImage)

        if nError != cv.STITCHER_OK:
            print("Stitching is not successful")
        else:
            print("Your Panorama is ready")

        cv.imshow("final result", output)

        cv.waitKey(0)



imageList = ['1.jpg', '2.jpg']
Panorama = processImage()

processImage.getPanorama(imageList)

