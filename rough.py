import cv2

# Load the image
# image = cv2.imread('maze_image/rotated_image.png')
image = cv2.imread('input_maze/maze2.jpg')
# cv2.imshow('Image', image)

# Get image dimensions
mx=752
my=752
height, width = image.shape[:2]
print(height,width)

# Define crop coordinates (make sure they're within bounds)
# x_start, y_start = 160, 70
# x_end, y_end = 470, 390
x_start=(width-mx)//2+20
x_end=(width+mx)//2-20
y_start=(height-my)//2
y_end=(height+my)//2-50
# x_start, y_start = 584, 164
# x_end, y_end = 1336, 916
print(type(x_start))

# Ensure coordinates are valid
if 0 <= x_start < x_end <= width and 0 <= y_start < y_end <= height:
    # Crop the image using slicing
    cropped_image = image[y_start:y_end, x_start:x_end]

    # Display the cropped image
    cv2.imshow('Cropped Image', cropped_image)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

    # Save the cropped image
    cv2.imwrite('maze_image/rotated_image.png', cropped_image)
else:
    print(f"Invalid crop coordinates! Image size: {width}x{height}, "
          f"Coordinates: x_start={x_start}, y_start={y_start}, x_end={x_end}, y_end={y_end}")

# import cv2
# import numpy as np
# import matplotlib.pyplot as plt

# # Load the image
# image = cv2.imread('maze_image/rotated_image.png')

# # Convert to grayscale
# gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

# # Threshold the image to create a binary mask (white maze on black background)
# _, binary = cv2.threshold(gray, 200, 255, cv2.THRESH_BINARY)

# # Invert the binary image to make the white board as foreground
# binary = cv2.bitwise_not(binary)

# # Find contours of the white maze board
# contours, _ = cv2.findContours(binary, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

# # Filter by area to eliminate small contours (screws, markers, etc.)
# contours = [c for c in contours if cv2.contourArea(c) > 10000]

# # Assume the largest contour is the maze board
# maze_contour = max(contours, key=cv2.contourArea)

# # Approximate the contour to get a rectangle
# epsilon = 0.02 * cv2.arcLength(maze_contour, True)
# approx = cv2.approxPolyDP(maze_contour, epsilon, True)

# # Warp perspective if the contour is a quadrilateral
# if len(approx) == 4:
#     # Get points for perspective transformation
#     pts = approx.reshape(4, 2)

#     # Determine top-left, top-right, bottom-left, bottom-right
#     rect = np.zeros((4, 2), dtype="float32")
#     s = pts.sum(axis=1)
#     rect[0] = pts[np.argmin(s)]  # top-left
#     rect[2] = pts[np.argmax(s)]  # bottom-right

#     diff = np.diff(pts, axis=1)
#     rect[1] = pts[np.argmin(diff)]  # top-right
#     rect[3] = pts[np.argmax(diff)]  # bottom-left

#     # Define the destination points for warping
#     (tl, tr, br, bl) = rect
#     width = max(int(np.linalg.norm(br - bl)), int(np.linalg.norm(tr - tl)))
#     height = max(int(np.linalg.norm(tr - br)), int(np.linalg.norm(tl - bl)))

#     dst = np.array([
#         [0, 0],
#         [width - 1, 0],
#         [width - 1, height - 1],
#         [0, height - 1]
#     ], dtype="float32")

#     # Get the perspective transform matrix and warp the image
#     M = cv2.getPerspectiveTransform(rect, dst)
#     warped = cv2.warpPerspective(image, M, (width, height))

#     # Save or display the result
#     cv2.imwrite('maze_image/cropped_maze.png', warped)
#     plt.imshow(cv2.cvtColor(warped, cv2.COLOR_BGR2RGB))
#     plt.axis('off')
#     plt.show()

# else:
#     print("Maze board contour is not a quadrilateral.")
