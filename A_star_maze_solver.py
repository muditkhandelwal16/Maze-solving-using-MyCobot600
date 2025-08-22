import csv
import heapq
import numpy as np
from scipy.ndimage import binary_dilation

from maze_detection import maze_detection
from img_crop import*
from startStop import startStop
from capture_maze import capture_img

capture_img()

input_image='input_maze/maze1.png' #path of the original image
# rotate_angle = rotate_maze(input_image)
# print(rotate_angle)
cropped_img='maze_image/cropped_maze.png'
crop_img(input_image)
crop_fit(cropped_img)

maze_detection(cropped_img)



def heuristic(a, b):
    """Calculate Manhattan distance heuristic."""
    return abs(a[0] - b[0]) + abs(a[1] - b[1])

def is_valid_move(maze, x, y):
    """Check if the move is within bounds and not a wall."""
    return 0 <= x < len(maze) and 0 <= y < len(maze[0]) and maze[x][y] == 0

def expand_walls(maze, distance=3):
    """Expand the walls by a given distance using dilation."""
    maze_np = np.array(maze)
    struct = np.ones((distance * 2 + 1, distance * 2 + 1))  # Create a kernel for expansion
    expanded_maze = binary_dilation(maze_np, structure=struct).astype(int)
    return expanded_maze

def a_star(maze, start, goal):
    """A* algorithm to solve a maze."""
    open_list = []
    heapq.heappush(open_list, (0, start))
    g_cost = {start: 0}
    came_from = {start: None}
    
    while open_list:
        _, current = heapq.heappop(open_list)
        
        if current == goal:
            path = []
            while current:
                path.append(current)
                current = came_from[current]
            return path[::-1]
        
        x, y = current
        neighbors = [(x-1, y), (x+1, y), (x, y-1), (x, y+1)]
        
        for neighbor in neighbors:
            nx, ny = neighbor
            if is_valid_move(maze, nx, ny):
                new_cost = g_cost[current] + 1
                if neighbor not in g_cost or new_cost < g_cost[neighbor]:
                    g_cost[neighbor] = new_cost
                    f_cost = new_cost + heuristic(neighbor, goal)
                    heapq.heappush(open_list, (f_cost, neighbor))
                    came_from[neighbor] = current
    
    return None


binary_maze=[]
with open('binary_img.csv', mode ='r')as file:
    csvFile = csv.reader(file)
    for lines in csvFile:
        l=list(map(int,lines))
        binary_maze.append(l)

coordinates=startStop(binary_maze)
start = (coordinates[0][0], coordinates[0][1])
goal = (coordinates[1][0],coordinates[1][1])

# Expand walls and find path
expanded_maze = expand_walls(binary_maze, distance=3) # expand the walls to leave thin path

path = a_star(expanded_maze, start, goal) # calculate the path


for row in expanded_maze:
    with open('robot_path.csv', mode='w', newline='') as file:
        writer = csv.writer(file)
        writer.writerows(list(path))
with open('robot_path.csv', mode='w', newline='') as file:
    writer = csv.writer(file)
    writer.writerows(path)