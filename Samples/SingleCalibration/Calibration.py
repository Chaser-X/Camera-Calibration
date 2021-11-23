import cv2
import glob
import numpy as np
import matplotlib.pyplot as mp

# termination criteria
criteria = (cv2.TERM_CRITERIA_EPS + cv2.TERM_CRITERIA_MAX_ITER, 30, 0.001)
# prepare object points, like (0,0,0), (1,0,0), (2,0,0) ....,(6,5,0)
objp = np.zeros((9*6,3), np.float32)
objp[:,:2] = np.mgrid[0:9,0:6].T.reshape(-1,2)
objpoints = [] #chessboard conner 3d points
imgpoints = [] #conners image point
imgPaths = glob.glob('.\\CalImage\\*.jpg')
for frame in imgPaths:
    img = cv2.imread(frame)
    imggray = cv2.cvtColor(img, cv2.COLOR_RGB2GRAY)
    # Find the chess board corners
    ret, corners = cv2.findChessboardCorners(imggray, (9,6), None)
    # If found, add object points, image points (after refining them)
    if ret == True:
        objpoints.append(objp)
        corners2 = cv2.cornerSubPix(imggray,corners, (11,11), (-1,-1), criteria)
        imgpoints.append(corners)
        # Draw and display the corners
        cv2.drawChessboardCorners(img, (9,6), corners2, ret)
        cv2.imshow('img', img)
        cv2.waitKey()
shape  = imggray.shape[::-1]
ret,cameraMatrix,dist,rvecs,tvecs = cv2.calibrateCamera(objpoints, imgpoints, shape ,None,None)

#optimal cameramatrix 
imgT = cv2.imread('.\\CalImage\\cal1.jpg')
h,  w = imgT.shape[:2]
newcameramtx, roi = cv2.getOptimalNewCameraMatrix(cameraMatrix, dist, (w,h), 1, (w,h),True)
# undistort
dst = cv2.undistort(imgT, cameraMatrix, dist, None, cameraMatrix)
# crop the image
x, y, w, h = roi
dst = dst[y:y+h, x:x+w]
cv2.imshow('img', dst)
cv2.waitKey()

#EMS-ERROR
mean_error = 0
for i in range(len(objpoints)):
    imgpoints2, _ = cv2.projectPoints(objpoints[i], rvecs[i], tvecs[i], cameraMatrix, dist)
    error = cv2.norm(imgpoints[i], imgpoints2, cv2.NORM_L2)/len(imgpoints2)
    mean_error += error
print( "total error: {}".format(mean_error/len(objpoints)) )

cv2.destroyAllWindows()