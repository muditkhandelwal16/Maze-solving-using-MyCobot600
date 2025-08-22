import cv2
import numpy as np

# Load the image
def crop_fit(img_path):
    image = cv2.imread(img_path, cv2.IMREAD_GRAYSCALE)

    # Invert the image so the walls become black (value 0) and background white (value 255)
    _, binary = cv2.threshold(image, 150, 255, cv2.THRESH_BINARY)

    # Find rows and columns containing black pixels (wall pixels)
    horizontal_projection = np.any(binary == 0, axis=1)
    vertical_projection = np.any(binary == 0, axis=0)

    # Get the indices where black pixels are found
    top_index = np.argmax(horizontal_projection)
    bottom_index = binary.shape[0] - np.argmax(horizontal_projection[::-1]) - 1
    left_index = np.argmax(vertical_projection)
    right_index = binary.shape[1] - np.argmax(vertical_projection[::-1]) - 1

    # Crop the maze using these indices
    cropped_maze = image[top_index:bottom_index + 1, left_index:right_index + 1]

    cv2.imwrite('maze_image/cropped_maze.png', cropped_maze)


def crop_maze(image_path):
    # Load the image
    image = cv2.imread(image_path)
    
    # Convert the image to grayscale
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    
    # Use adaptive thresholding to handle varying lighting
    thresh = cv2.adaptiveThreshold(gray, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY_INV, 11, 2)
    
    # Perform morphological operations to clean up noise
    kernel = np.ones((5, 5), np.uint8)
    cleaned = cv2.morphologyEx(thresh, cv2.MORPH_CLOSE, kernel)
    
    # Find the largest contour (assumed to be the maze)
    contours, _ = cv2.findContours(cleaned, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    largest_contour = max(contours, key=cv2.contourArea)
    
    # Approximate the contour to a polygon
    epsilon = 0.02 * cv2.arcLength(largest_contour, True)
    approx = cv2.approxPolyDP(largest_contour, epsilon, True)
    
    # Create a mask for the maze
    mask = np.zeros_like(gray)
    cv2.drawContours(mask, [approx], -1, 255, thickness=cv2.FILLED)
    
    # Bitwise AND the mask with the original image
    maze_only = cv2.bitwise_and(image, image, mask=mask)
    
    # Find the bounding box of the maze
    x, y, w, h = cv2.boundingRect(approx)
    print(x,y,w,h)
    # Crop to this bounding box
    cropped_maze = maze_only[y+10:y+h-40, x+20:x+w-20]
    
    # Save the cropped maze
    cv2.imwrite('maze_image/rotated_image.png', cropped_maze)


def crop_img(img_path):
    image = cv2.imread(img_path)

    mx=325
    my=325
    height, width = image.shape[:2]
    print(height,width)

    # Define crop coordinates (make sure they're within bounds)
    # x_start=(width-mx)//2+20
    # x_end=(width+mx)//2-10
    # y_start=(height-my)//2
    # y_end=(height+my)//2-20
    x_start=178
    x_end=489
    y_start=85
    y_end=395

    # Ensure coordinates are valid
    if 0 <= x_start < x_end <= width and 0 <= y_start < y_end <= height:
        # Crop the image using slicing
        cropped_image = image[y_start:y_end, x_start:x_end]


        # Save the cropped image
        cv2.imwrite('maze_image/cropped_maze.png', cropped_image)
    else:
        print(f"Invalid crop coordinates! Image size: {width}x{height}, "
            f"Coordinates: x_start={x_start}, y_start={y_start}, x_end={x_end}, y_end={y_end}")
