import cv2 
import numpy as np 
import glob 

# Define the dimensions of the checkerboard 
CHECKERBOARD = (6, 8) 

# Criteria for termination 
criteria = (cv2.TERM_CRITERIA_EPS + cv2.TERM_CRITERIA_MAX_ITER, 30, 0.001) 

# Vectors for 3D points and 2D image points 
threedpoints = [] 
twodpoints = [] 

# 3D points real world coordinates 
objectp3d = np.zeros((1, CHECKERBOARD[0] * CHECKERBOARD[1], 3), np.float32) 
objectp3d[0, :, :2] = np.mgrid[0:CHECKERBOARD[0], 0:CHECKERBOARD[1]].T.reshape(-1, 2) 

# Extract paths of individual images 
images = glob.glob('calib_img*.jpg') 

if len(images) == 0:
    print("No images found.")
    exit()

for filename in images: 
    image = cv2.imread(filename) 
    grayColor = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY) 

    # Find the chess board corners 
    ret, corners = cv2.findChessboardCorners( 
        grayColor, CHECKERBOARD, 
        cv2.CALIB_CB_ADAPTIVE_THRESH + 
        cv2.CALIB_CB_FAST_CHECK + 
        cv2.CALIB_CB_NORMALIZE_IMAGE) 

    if ret: 
        threedpoints.append(objectp3d) 
        corners2 = cv2.cornerSubPix(grayColor, corners, (11, 11), (-1, -1), criteria) 
        twodpoints.append(corners2) 
        image = cv2.drawChessboardCorners(image, CHECKERBOARD, corners2, ret) 
        cv2.imshow('img', image) 
        cv2.waitKey(500) 

cv2.destroyAllWindows() 

if len(threedpoints) > 0 and len(twodpoints) > 0:
    h, w = grayColor.shape[:2] 
    ret, matrix, distortion, r_vecs, t_vecs = cv2.calibrateCamera(threedpoints, twodpoints, (w, h), None, None) 

    # Displaying the output 
    print("Camera Matrix:") 
    print(matrix) 

    print("\nDistortion Coefficients:") 
    print(distortion) 

    print("\nRotation Vectors:") 
    print(r_vecs) 

    print("\nTranslation Vectors:") 
    print(t_vecs) 
else:
    print("Calibration failed: No valid chessboard corners detected.")
