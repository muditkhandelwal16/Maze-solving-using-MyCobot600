import numpy as np
import csv
def startStop(maze):
    orientation=0

    def find_opening_center(row):
        row=np.array(row)
        # Find indices of consecutive zeros in the row
        zero_indices = np.where(row == 0)
    
        if len(zero_indices) > 0:
            # Find the middle index of the consecutive zeros
            indices=zero_indices[0].tolist()
            start = indices[0]
            end = indices[-1]
            center = (start + end) // 2
            return center
        return None
    
    side1_list=[]
    side2_list=[]

    row=np.array(maze[0])
    zero_indices = np.where(row == 0)
    if len(zero_indices[0])>0:
        orientation=1

    for i in range(len(maze)):
        side1_list.append(maze[i][0])
        side2_list.append(maze[i][len(maze)-1])
    
    if orientation==1:
        # Start coordinates
        start_x = 0
        start_y = find_opening_center(maze[0])
        # End coordinates
        end_x = len(maze) - 1
        end_y = find_opening_center(maze[end_x])
        coordinates = [[start_x,start_y],[end_x, end_y]]
        return coordinates
    else:
        start_x=find_opening_center(side1_list)
        start_y=0

        end_x = find_opening_center(side2_list)
        end_y = len(side2_list) - 1
        coordinates = [[start_x,start_y],[end_x, end_y]]
        return coordinates

binary_maze=[]
with open('binary_img.csv', mode ='r')as file:
    csvFile = csv.reader(file)
    for lines in csvFile:
        l=list(map(int,lines))
        binary_maze.append(l)
