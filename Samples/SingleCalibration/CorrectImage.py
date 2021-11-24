import cv2
import numpy as np

PATH = 'D:/GitRepos/WORK/self project/LearnPython/Samples/SingleCalibration'
criteria = (cv2.TERM_CRITERIA_EPS + cv2.TERM_CRITERIA_MAX_ITER, 30, 0.001)

img = cv2.imread(PATH + '/CalImage/cal1.jpg')

f = cv2.FileStorage(PATH  + '/CalImage/cameraInstric.xml',cv2.FILE_STORAGE_READ)
cameraMatrix = f.getNode('cameraMatrix').mat()
dist = f.getNode('distortion').mat()
f.release()
dstImage = cv2.undistort(img, cameraMatrix, dist)
gray = cv2.cvtColor(dstImage,cv2.COLOR_RGB2GRAY)

ret, corners = cv2.findChessboardCorners(gray, (9,6), None)
if ret:
    imgPoints = np.array([corners[0],
                 corners[8],
                 corners[45],
                 corners[53]],dtype = 'float32')

    cv2.imshow('dstImage', dstImage)
    dstpoints = np.array([[290,320],
                [290,160],
                [390,320],
                [390,160]],dtype = 'float32')
    preMatrix = cv2.getPerspectiveTransform(imgPoints, dstpoints)
    preImage = cv2.warpPerspective(dstImage, preMatrix, (680,480))
    cv2.imshow('prespectiveImage', preImage)
cv2.waitKey()
cv2.destroyAllWindows()