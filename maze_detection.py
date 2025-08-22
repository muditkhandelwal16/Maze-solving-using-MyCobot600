import cv2
import numpy as np
import os
import csv

# img_path='maze_image/cropped_maze.png'
def maze_detection(img_path):
    # Load and preprocess the maze image
    image = cv2.imread(img_path)  # Replace with your image
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    _, thresh = cv2.threshold(gray, 128, 255, cv2.THRESH_BINARY_INV)

    # Get image dimensions
    height, width = thresh.shape
    cell_count= 34
    cell_height = height // cell_count
    cell_width = width // cell_count

    maze_grid = np.zeros((cell_count, cell_count), dtype=int)

    for i in range(cell_count):
        for j in range(cell_count):
            # Extract the cell
            cell = thresh[i * cell_height:(i + 1) * cell_height, j * cell_width:(j + 1) * cell_width]
            
            # Calculate the percentage of white pixels (walls)
            wall_percentage = np.sum(cell == 255) / (cell_height * cell_width)
            
            # Set threshold to classify as wall (1) or open space (0)
            if wall_percentage > 0.5:  # Adjust this threshold as needed
                maze_grid[i, j] = 1
            else:
                maze_grid[i, j] = 0
        with open('binary_img.csv', mode='w', newline='') as file:
            writer = csv.writer(file)
            writer.writerows(maze_grid)
