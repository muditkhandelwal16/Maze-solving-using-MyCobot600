import cv2
import numpy as np

# Step 1: Load the image
def rotate_maze(image_path):
    image = cv2.imread(image_path)
    # Step 2: Convert the image to grayscale

    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

    # Step 3: Apply Gaussian Blur to reduce noise and smooth the image
    blurred = cv2.GaussianBlur(gray, (5, 5), 0)

    # Step 4: Apply adaptive thresholding to handle noise and variable lighting
    binary_image = cv2.adaptiveThreshold(blurred, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY_INV, 11, 2)
    
    # Step 5: Detect edges using Canny edge detection
    edges = cv2.Canny(binary_image, 50, 150, apertureSize=3)

    # Step 6: Use Hough Line Transform to detect lines and estimate the maze's orientation
    lines = cv2.HoughLines(edges, 1, np.pi / 180, 150)
    # Step 7: Calculate the average angle of detected lines to determine rotation
    angles = []
    if lines is not None:
        for rho, theta in lines[:, 0]:
            angle = np.rad2deg(theta)  # Convert radians to degrees
            if angle < 90:  # Only consider angles less than 90 degrees
                angles.append(angle)

    # Step 8: Compute the median of all detected angles as the rotation angle
    rotation_angle = np.median(angles) if len(angles) > 0 else 0
    rotation_angle=rotation_angle
    # Step 9: Rotate the image to correct the tilt
    (h, w) = image.shape[:2]
    center = (w // 2, h // 2)
    rotation_matrix = cv2.getRotationMatrix2D(center, rotation_angle, 1.0)
    rotated_image = cv2.warpAffine(image, rotation_matrix, (w, h), flags=cv2.INTER_LINEAR, borderMode=cv2.BORDER_CONSTANT, borderValue=(255, 255, 255))
    cv2.imwrite('maze_image/cropped_maze.png', rotated_image)
    return rotation_angle
rotate_maze('input_maze/maze1.png')
# rotate_maze('maze_image/rotated_image.png')
# rotate_maze('input_maze/maze1.jpg')

# import cv2
# import numpy as np

# def rotate_and_crop(image_path, output_path):
#     # Read the image
#     image = cv2.imread(image_path, cv2.IMREAD_GRAYSCALE)
    
#     # Threshold the image to binary (assuming black maze walls on a white background)
#     _, thresh = cv2.threshold(image, 127, 255, cv2.THRESH_BINARY_INV)
    
#     # Find contours of the maze
#     contours, _ = cv2.findContours(thresh, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    
#     # Get the largest contour assuming it's the maze
#     largest_contour = max(contours, key=cv2.contourArea)
    
#     # Find the minimum bounding rectangle with angle
#     rect = cv2.minAreaRect(largest_contour)
#     angle = rect[-1]
    
#     # Correct the angle
#     if angle < -45:
#         angle += 90
    
#     # Get the center of the image
#     center = (image.shape[1] // 2, image.shape[0] // 2)
    
#     # Get the rotation matrix
#     rotation_matrix = cv2.getRotationMatrix2D(center, angle, 1.0)
    
#     # Rotate the image
#     rotated = cv2.warpAffine(image, rotation_matrix, (image.shape[1], image.shape[0]), flags=cv2.INTER_LINEAR)
    
#     # Crop to keep the same size without padding
#     x, y, w, h = cv2.boundingRect(cv2.findNonZero(rotated))
#     cropped = rotated[y:y + h, x:x + w]
    
#     # Resize back to the original size to ensure the maze stays the same size
#     resized = cv2.resize(cropped, (image.shape[1], image.shape[0]))
    
#     # Save and display the corrected maze
#     cv2.imwrite(output_path, resized)
#     print(f"Maze image saved to {output_path}")

# # Paths
# input_path = 'input_maze/maze1.png'

# rotate_and_crop(input_path, 'maze_image/cropped_maze.png')
