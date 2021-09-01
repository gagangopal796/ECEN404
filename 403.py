from tkinter import *
from PIL import Image, ImageTk
from functools import partial
from time import sleep

# func for the window
def app_window(app, root, canvas1, start_color, end_color, cover_color, obstacle_color, path_color, 
start1, start2, start3, end, cover1, cover2, cover3, cover4, cover5, obstacle1,
obstacle2, obstacle3, obstacle4, obstacle5, obstacle6, obstacle7, obstacle8, 
obstacle9, obstacle10, obstacle11, obstacle12, obstacle13, obstacle14, obstacle15, obstacle16):

    root.geometry('1000x1000') # for the size of the GUI

    # create the icon [top left of the GUI]
    icon = PhotoImage(file = 'images/drone.png')
    root.iconphoto(False, icon)

    # place the starting squad color on the map image
    canvas1.create_image((start1), image=start_color, anchor=NW)
    canvas1.create_image((start2), image=start_color, anchor=NW)
    canvas1.create_image((start3), image=start_color, anchor=NW)

    # place the end node color on the map
    canvas1.create_image((end), image=end_color, anchor=NW)

    # position for the cover nodes 
    canvas1.create_image((cover1), image=cover_color, anchor=NW)
    canvas1.create_image((cover2), image=cover_color, anchor=NW)
    canvas1.create_image((cover3), image=cover_color, anchor=NW)
    canvas1.create_image((cover4), image=cover_color, anchor=NW)
    canvas1.create_image((cover5), image=cover_color, anchor=NW)

    # position for the obstacles nodes
    canvas1.create_image((obstacle1), image=obstacle_color, anchor=NW)
    canvas1.create_image((obstacle2), image=obstacle_color, anchor=NW)
    canvas1.create_image((obstacle3), image=obstacle_color, anchor=NW)
    canvas1.create_image((obstacle4), image=obstacle_color, anchor=NW)
    canvas1.create_image((obstacle5), image=obstacle_color, anchor=NW)
    canvas1.create_image((obstacle6), image=obstacle_color, anchor=NW)
    canvas1.create_image((obstacle7), image=obstacle_color, anchor=NW)
    canvas1.create_image((obstacle8), image=obstacle_color, anchor=NW)
    canvas1.create_image((obstacle9), image=obstacle_color, anchor=NW)
    canvas1.create_image((obstacle10), image=obstacle_color, anchor=NW)
    canvas1.create_image((obstacle11), image=obstacle_color, anchor=NW)
    canvas1.create_image((obstacle12), image=obstacle_color, anchor=NW)
    canvas1.create_image((obstacle13), image=obstacle_color, anchor=NW)
    canvas1.create_image((obstacle14), image=obstacle_color, anchor=NW)
    canvas1.create_image((obstacle15), image=obstacle_color, anchor=NW)
    canvas1.create_image((obstacle16), image=obstacle_color, anchor=NW)

class App:
    def __init__(self, root, canvas1, start_color, end_color, cover_color, obstacle_color, path_color, start1 = [], 
    start2 = [], start3 = [], end = [], cover1 = [], cover2 = [], cover3 = [], cover4 = [], cover5 = [], obstacle1 = [],
    obstacle2 = [], obstacle3 = [], obstacle4 = [], obstacle5 = [], obstacle6 = [], obstacle7 = [], obstacle8 = [], obstacle9 = [], 
    obstacle10 = [], obstacle11 = [], obstacle12 = [], obstacle13 = [], obstacle14 = [], obstacle15 = [], obstacle16 = []):
        
        root.wm_title("403 Project Demo")
        
        self.root = root
        self.canvas1 = canvas1
        self.start_color = start_color
        self.end_color = end_color
        self.cover_color = cover_color
        self.obstacle_color = obstacle_color
        self.path_color = path_color
        self.start1 = [100,100]         # keep all paths on a diagonal to the goal node
        self.start2 = [900, 100]        
        self.start3 = [100, 900]

        self.end = [500, 500]           # keep obstacle in the center for easy testing

        self.cover1 = [220, 220]        # for squad 1 testing
        self.cover2 = [770, 220]        # squad 2
        self.cover3 = [220, 770]        # squad 3
        self.cover4 = [700, 700]  
        self.cover5 = [800, 900]

        self.obstacle1 = [200, 200]     # make obstacles of 4 adjacent pixels for better visibility
        self.obstacle2 = [201, 200]
        self.obstacle3 = [200, 201]
        self.obstacle4 = [201, 201]

        self.obstacle5 = [200, 800]     # obstacle 2
        self.obstacle6 = [201, 800]
        self.obstacle7 = [200, 801]
        self.obstacle8 = [201, 801]

        self.obstacle9 = [800, 200]     # obstacle 3
        self.obstacle10 = [801, 200]
        self.obstacle11 = [800, 201]
        self.obstacle12 = [801, 201]

        self.obstacle13 = [800, 800]     # obstacle 4
        self.obstacle14 = [801, 800]
        self.obstacle15 = [800, 801]
        self.obstacle16 = [801, 801]

        # starting positions of everything will be hard-coded for now - will need to get from Gagan later
        start1 = [100,100]         # keep all paths on a diagonal to the goal node - this way we can easily implement cover node logic
        start2 = [900, 100]        
        start3 = [100, 900]

        end = [500, 500]           # keep obstacle in the center for easy testing
        
        cover1 = [220, 220]        # squad 1
        cover2 = [770, 220]        # squad 2
        cover3 = [220, 770]        # squad 3
        cover4 = [700, 700]        
        cover5 = [800, 900]

        obstacle1 = [200, 200]     # obstacle 1
        obstacle2 = [201, 200]
        obstacle3 = [200, 201]
        obstacle4 = [201, 201]

        obstacle5 = [200, 800]     # obstacle 2
        obstacle6 = [201, 800]
        obstacle7 = [200, 801]
        obstacle8 = [201, 801]

        obstacle9 = [800, 200]     # obstacle 3
        obstacle10 = [801, 200]
        obstacle11 = [800, 201]
        obstacle12 = [801, 201]

        obstacle13 = [800, 800]     # obstacle 4
        obstacle14 = [801, 800]
        obstacle15 = [800, 801]
        obstacle16 = [801, 801]

        # create the pop-up window
        root.update_idletasks()
        app_window(self, root, canvas1, start_color, end_color, cover_color, obstacle_color, path_color, 
        start1, start2, start3, end, cover1, cover2, cover3, cover4, cover5, obstacle1,
        obstacle2, obstacle3, obstacle4, obstacle5, obstacle6, obstacle7, obstacle8, 
        obstacle9, obstacle10, obstacle11, obstacle12, obstacle13, obstacle14, obstacle15, obstacle16)

    # heuristic function to find the minimum amount we need
    def heuristic(self, node1, node2):
        # implement distance formula
        return abs(node1[0] - node2[0]) + abs(node1[1]-node2[1])

    # function to find the neighbors - pass all five obstacles - will need to iterate over the 1000x1000 GUI
    def find_neighbors(self, current):
        # create an empty list for the neighbors
        neighbors = []

        right_neighbor = current[:] # create new list for the right neighbor
        right_neighbor[1] = current[1] + 1 

        # check the right neighbor for all five obstacles
        if 0 <= right_neighbor[1] < 1000 and right_neighbor != self.obstacle1 \
            and right_neighbor != self.obstacle2 and right_neighbor != self.obstacle3 \
            and right_neighbor != self.obstacle4 and right_neighbor != self.obstacle5 \
            and right_neighbor != self.obstacle6 and right_neighbor != self.obstacle7 \
            and right_neighbor != self.obstacle8 and right_neighbor != self.obstacle9 \
            and right_neighbor != self.obstacle10 and right_neighbor != self.obstacle11 \
            and right_neighbor != self.obstacle12 and right_neighbor != self.obstacle13 \
            and right_neighbor != self.obstacle14 and right_neighbor != self.obstacle15 \
            and right_neighbor != self.obstacle16:
            neighbors.append(right_neighbor)
        left_neighbor = current[:]
        left_neighbor[1] = current[1] - 1

        # check the left neighbor
        if 0 <= left_neighbor[1] < 1000 and left_neighbor != self.obstacle1 \
            and left_neighbor != self.obstacle2 and left_neighbor != self.obstacle3 \
            and left_neighbor != self.obstacle4 and left_neighbor != self.obstacle5 \
            and left_neighbor != self.obstacle6 and left_neighbor != self.obstacle7 \
            and left_neighbor != self.obstacle8 and left_neighbor != self.obstacle9 \
            and left_neighbor != self.obstacle10 and left_neighbor != self.obstacle11 \
            and left_neighbor != self.obstacle12 and left_neighbor != self.obstacle13 \
            and left_neighbor != self.obstacle14 and left_neighbor != self.obstacle15 \
            and left_neighbor != self.obstacle16:
            neighbors.append(left_neighbor)
        up_neighbor = current[:]
        up_neighbor[0] = current[0] + 1

        # check the neighbor above
        if 0 <= up_neighbor[0] < 1000 and up_neighbor != self.obstacle1 \
            and up_neighbor != self.obstacle2 and up_neighbor != self.obstacle3 \
            and up_neighbor != self.obstacle4 and up_neighbor != self.obstacle5 \
            and up_neighbor != self.obstacle6 and up_neighbor != self.obstacle7 \
            and up_neighbor != self.obstacle8 and up_neighbor != self.obstacle9 \
            and up_neighbor != self.obstacle10 and up_neighbor != self.obstacle11 \
            and up_neighbor != self.obstacle12 and up_neighbor != self.obstacle13 \
            and up_neighbor != self.obstacle14 and up_neighbor != self.obstacle15 \
            and up_neighbor != self.obstacle16:
            neighbors.append(up_neighbor)
        down_neighbor = current[:]
        down_neighbor[0] = current[0] - 1

        # check the neighbor below
        if 0 <= down_neighbor[0] < 1000 and down_neighbor != self.obstacle1 \
            and down_neighbor != self.obstacle2 and down_neighbor != self.obstacle3 \
            and down_neighbor != self.obstacle4 and down_neighbor != self.obstacle5 \
            and down_neighbor != self.obstacle6 and down_neighbor != self.obstacle7 \
            and down_neighbor != self.obstacle8 and down_neighbor != self.obstacle9 \
            and down_neighbor != self.obstacle10 and down_neighbor != self.obstacle11 \
            and down_neighbor != self.obstacle12 and down_neighbor != self.obstacle13 \
            and down_neighbor != self.obstacle14 and down_neighbor != self.obstacle15 \
            and down_neighbor != self.obstacle16:
            neighbors.append(down_neighbor)
        down_right_neighbor = current[:]
        down_right_neighbor[0] = current[0] + 1
        down_right_neighbor[1] = current[1] + 1

        # check the neighbor below and to the right
        if 0 <= down_right_neighbor[0] < 1000 and down_right_neighbor != self.obstacle1 \
            and down_right_neighbor != self.obstacle2 and down_right_neighbor != self.obstacle3 \
            and down_right_neighbor != self.obstacle4 and down_right_neighbor != self.obstacle5 \
            and down_right_neighbor != self.obstacle6 and down_right_neighbor != self.obstacle7 \
            and down_right_neighbor != self.obstacle8 and down_right_neighbor != self.obstacle9 \
            and down_right_neighbor != self.obstacle10 and down_right_neighbor != self.obstacle11 \
            and down_right_neighbor != self.obstacle12 and down_right_neighbor != self.obstacle13 \
            and down_right_neighbor != self.obstacle14 and down_right_neighbor != self.obstacle15 \
            and down_right_neighbor != self.obstacle16:
            neighbors.append(down_right_neighbor)
        up_right_neighbor = current[:]
        up_right_neighbor[0] = current[0] - 1
        up_right_neighbor[1] = current[1] + 1

        # check the neighbor above and to the right
        if 0 <= up_right_neighbor[0] < 1000 and up_right_neighbor != self.obstacle1 \
            and up_right_neighbor != self.obstacle2 and up_right_neighbor != self.obstacle3 \
            and up_right_neighbor != self.obstacle4 and up_right_neighbor != self.obstacle5 \
            and up_right_neighbor != self.obstacle6 and up_right_neighbor != self.obstacle7 \
            and up_right_neighbor != self.obstacle8 and up_right_neighbor != self.obstacle9 \
            and up_right_neighbor != self.obstacle10 and up_right_neighbor != self.obstacle11 \
            and up_right_neighbor != self.obstacle12 and up_right_neighbor != self.obstacle13 \
            and up_right_neighbor != self.obstacle14 and up_right_neighbor != self.obstacle15 \
            and up_right_neighbor != self.obstacle16:
            neighbors.append(up_right_neighbor)
        up_left_neighbor = current[:]
        up_left_neighbor[0] = current[0] - 1
        up_left_neighbor[1] = current[1] - 1

        # check the neighbor above and to the left
        if 0 <= up_left_neighbor[0] < 1000 and up_left_neighbor != self.obstacle1 \
            and up_left_neighbor != self.obstacle2 and up_left_neighbor != self.obstacle3 \
            and up_left_neighbor != self.obstacle4 and up_left_neighbor != self.obstacle5 \
            and up_left_neighbor != self.obstacle6 and up_left_neighbor != self.obstacle7 \
            and up_left_neighbor != self.obstacle8 and up_left_neighbor != self.obstacle9 \
            and up_left_neighbor != self.obstacle10 and up_left_neighbor != self.obstacle11 \
            and up_left_neighbor != self.obstacle12 and up_left_neighbor != self.obstacle13 \
            and up_left_neighbor != self.obstacle14 and up_left_neighbor != self.obstacle15 \
            and up_left_neighbor != self.obstacle16:
            neighbors.append(up_left_neighbor)
        down_left_neighbor = current[:]
        down_left_neighbor[0] = current[0] + 1
        down_left_neighbor[1] = current[1] - 1

        # check the neighbor below and to the left
        if 0 <= down_left_neighbor[0] < 1000 and down_left_neighbor != self.obstacle1 \
            and down_left_neighbor != self.obstacle2 and down_left_neighbor != self.obstacle3 \
            and down_left_neighbor != self.obstacle4 and down_left_neighbor != self.obstacle5 \
            and down_left_neighbor != self.obstacle6 and down_left_neighbor != self.obstacle7 \
            and down_left_neighbor != self.obstacle8 and down_left_neighbor != self.obstacle9 \
            and down_left_neighbor != self.obstacle10 and down_left_neighbor != self.obstacle11 \
            and down_left_neighbor != self.obstacle12 and down_left_neighbor != self.obstacle13 \
            and down_left_neighbor != self.obstacle14 and down_left_neighbor != self.obstacle15 \
            and down_left_neighbor != self.obstacle16:
            neighbors.append(down_left_neighbor)
        return neighbors

    # to sort the set
    def sort_open_set(self, open_set, f_score):
        # The index of the list is the same as the index in the open set
        # and the value of the index is the f_score of it
        index_to_fscore = []
        for node in open_set:
            f_score_of_node = f_score[node[0]][node[1]]
            index_to_fscore.append(f_score_of_node)

        sorted_copy = index_to_fscore.copy()
        sorted_copy.sort()
        sorted_open_set = []

        for value in sorted_copy:
            min_ = index_to_fscore.index(value)
            sorted_open_set.append(open_set[min_])
            # We mark that we have transfered this value to the sorted array
            index_to_fscore[min_] = float('inf')

        return sorted_open_set

    # implement the actual algorithm
    def a_star_algorithm(self, canvas1, start, end):
        # create an open set for the start nodes
        open_set = [start] 
        g_score = [] # cost so far to reach the node
        f_score = [] # total estimated cost of path through node  
        came_from = []

        # Initialiazation of f_score, g_score and came_from - make these lists full of infinitely large numbers 
        for i in range(1000):
            f_score.append([])
            g_score.append([])
            came_from.append([])
            for j in range(1000):
                infinity = float('inf')
                came_from[i].append([])
                g_score[i].append(infinity)  # set it to infinity
                f_score[i].append(infinity)  # set it to infinity

        # the starting cost (g_score) is 0, the f score is the expected cost [from the current node to the end - using the heuristic]
        g_score[start[0]][start[1]] = 0
        f_score[start[0]][start[1]] = self.heuristic(start, end)

        while len(open_set) > 0:
            self.root.update_idletasks() # Enter event loop until all idle tasks have been completed - this is used to display each path when it is completed - safer than update()
            sleep(0.02)

            # sort the open set
            open_set = self.sort_open_set(open_set, f_score)
            current = open_set[0]
            current_row = current[0]
            current_column = current[1]

            # once we have reached the end, construct the best path
            if current == end:
                return self.reconstruct_path(canvas1, came_from, current)

            # find the neighbors of the current node
            open_set.remove(current)
            neighbors = self.find_neighbors(current)

            for node in neighbors:
                node_row = node[0]
                node_column = node[1]
                # node is a list of [x,y], with the values inside being ints, so is cover. We can compare the values inside to see if going to that cover makes sense or not- cover is of 50 pts less

                # The weight of every edge is 1
                tentative_gScore = g_score[current_row][current_column] + 1

                # if the tentative g score (ie g score plus 1) is less than the current g score of the node
                # then we append the current nodes row and colum to the came_from list
                # then, update the g score to the new, lower score
                # and update the f score to be the g score plus the heuristic (h(n))
                if tentative_gScore < g_score[node_row][node_column]:
                    came_from[node_row][node_column].append(current_row)
                    came_from[node_row][node_column].append(current_column)
                    g_score[node_row][node_column] = tentative_gScore
                    f_score[node_row][node_column] = g_score[node_row][node_column] + self.heuristic(node, end) # changed end from self.end

                    if node not in open_set:
                        open_set.append(node[:])

    # find the paths needed - ADD COVER LOGIC HERE
    def find_path(self, event):
        # go to the shortest cover - NEED logic to compare if there are two paths that have cover
        
        # LOGIC FOR START 1 (FIRST SQUAD)
        # compare the distances for all five cover nodes from the starting node, then check if the lowest one satisfies the if statement, if so, go
        path1 = min(self.heuristic(self.start1, self.cover1), self.heuristic(self.start1, self.cover2), \
            self.heuristic(self.start1, self.cover3), self.heuristic(self.start1, self.cover4), self.heuristic(self.start1, self.cover5))
        
        if path1 == self.heuristic(self.start1, self.cover1) and self.cover1[0] < max(self.end[0], self.start1[0]) + 50 and \
            self.cover1[0] > min(self.end[0], self.start1[0]) - 50 and \
            self.cover1[1] < max(self.end[1], self.start1[1]) + 50 and \
            self.cover1[1] > min(self.end[1], self.start1[1]) - 50:
            self.a_star_algorithm(self.canvas1, self.start1, self.cover1) 
            self.a_star_algorithm(self.canvas1, self.cover1, self.end) 

        elif path1 == self.heuristic(self.start1, self.cover2) and self.cover2[0] < max(self.end[0], self.start1[0]) + 50 and \
            self.cover2[0] > min(self.end[0], self.start1[0]) - 50 and \
            self.cover2[1] < max(self.end[1], self.start1[1]) + 50 and \
            self.cover2[1] > min(self.end[1], self.start1[1]) - 50:
            self.a_star_algorithm(self.canvas1, self.start1, self.cover2) 
            self.a_star_algorithm(self.canvas1, self.cover2, self.end) 

        elif path1 == self.heuristic(self.start1, self.cover3) and self.cover3[0] < max(self.end[0], self.start1[0]) + 50 and \
            self.cover3[0] > min(self.end[0], self.start1[0]) - 50 and \
            self.cover3[1] < max(self.end[1], self.start1[1]) + 50 and \
            self.cover3[1] > min(self.end[1], self.start1[1]) - 50:
            self.a_star_algorithm(self.canvas1, self.start1, self.cover3) 
            self.a_star_algorithm(self.canvas1, self.cover3, self.end) 

        elif path1 == self.heuristic(self.start1, self.cover4) and self.cover4[0] < max(self.end[0], self.start1[0]) + 50 and \
            self.cover4[0] > min(self.end[0], self.start1[0]) - 50 and \
            self.cover4[1] < max(self.end[1], self.start1[1]) + 50 and \
            self.cover4[1] > min(self.end[1], self.start1[1]) - 50:
            self.a_star_algorithm(self.canvas1, self.start1, self.cover4) 
            self.a_star_algorithm(self.canvas1, self.cover4, self.end) 

        elif path1 == self.heuristic(self.start1, self.cover5) and self.cover5[0] < max(self.end[0], self.start1[0]) + 50 and \
            self.cover5[0] > min(self.end[0], self.start1[0]) - 50 and \
            self.cover5[1] < max(self.end[1], self.start1[1]) + 50 and \
            self.cover5[1] > min(self.end[1], self.start1[1]) - 50:
            self.a_star_algorithm(self.canvas1, self.start1, self.cover5) 
            self.a_star_algorithm(self.canvas1, self.cover5, self.end) 

        else: 
            self.a_star_algorithm(self.canvas1, self.start1, self.end) 

        #LOGIC FOR START 2
        path2 = min(self.heuristic(self.start2, self.cover1), self.heuristic(self.start2, self.cover2), \
            self.heuristic(self.start2, self.cover3), self.heuristic(self.start2, self.cover4), self.heuristic(self.start2, self.cover5))
        
        if path2 == self.heuristic(self.start2, self.cover1) and self.cover1[0] < max(self.end[0], self.start2[0]) + 50 and \
            self.cover1[0] > min(self.end[0], self.start2[0]) - 50 and \
            self.cover1[1] < max(self.end[1], self.start2[1]) + 50 and \
            self.cover1[1] > min(self.end[1], self.start2[1]) - 50:
            self.a_star_algorithm(self.canvas1, self.start2, self.cover1) 
            self.a_star_algorithm(self.canvas1, self.cover1, self.end) 

        elif path2 == self.heuristic(self.start2, self.cover2) and self.cover2[0] < max(self.end[0], self.start2[0]) + 50 and \
            self.cover2[0] > min(self.end[0], self.start2[0]) - 50 and \
            self.cover2[1] < max(self.end[1], self.start2[1]) + 50 and \
            self.cover2[1] > min(self.end[1], self.start2[1]) - 50:
            self.a_star_algorithm(self.canvas1, self.start2, self.cover2) 
            self.a_star_algorithm(self.canvas1, self.cover2, self.end) 

        elif path2 == self.heuristic(self.start2, self.cover3) and self.cover3[0] < max(self.end[0], self.start2[0]) + 50 and \
            self.cover3[0] > min(self.end[0], self.start2[0]) - 50 and \
            self.cover3[1] < max(self.end[1], self.start2[1]) + 50 and \
            self.cover3[1] > min(self.end[1], self.start2[1]) - 50:
            self.a_star_algorithm(self.canvas1, self.start2, self.cover3) 
            self.a_star_algorithm(self.canvas1, self.cover3, self.end) 

        elif path2 == self.heuristic(self.start2, self.cover4) and self.cover4[0] < max(self.end[0], self.start2[0]) + 50 and \
            self.cover4[0] > min(self.end[0], self.start2[0]) - 50 and \
            self.cover4[1] < max(self.end[1], self.start2[1]) + 50 and \
            self.cover4[1] > min(self.end[1], self.start2[1]) - 50:
            self.a_star_algorithm(self.canvas1, self.start2, self.cover4) 
            self.a_star_algorithm(self.canvas1, self.cover4, self.end) 

        elif path2 == self.heuristic(self.start2, self.cover5) and self.cover5[0] < max(self.end[0], self.start2[0]) + 50 and \
            self.cover5[0] > min(self.end[0], self.start2[0]) - 50 and \
            self.cover5[1] < max(self.end[1], self.start2[1]) + 50 and \
            self.cover5[1] > min(self.end[1], self.start2[1]) - 50:
            self.a_star_algorithm(self.canvas1, self.start2, self.cover5) 
            self.a_star_algorithm(self.canvas1, self.cover5, self.end) 

        else: 
            self.a_star_algorithm(self.canvas1, self.start2, self.end)

        # LOGIC FOR START 3
        path3 = min(self.heuristic(self.start3, self.cover1), self.heuristic(self.start3, self.cover2), \
            self.heuristic(self.start3, self.cover3), self.heuristic(self.start3, self.cover4), self.heuristic(self.start3, self.cover5))
        
        if path3 == self.heuristic(self.start3, self.cover1) and self.cover1[0] < max(self.end[0], self.start3[0]) + 50 and \
            self.cover1[0] > min(self.end[0], self.start3[0]) - 50 and \
            self.cover1[1] < max(self.end[1], self.start3[1]) + 50 and \
            self.cover1[1] > min(self.end[1], self.start3[1]) - 50:
            self.a_star_algorithm(self.canvas1, self.start3, self.cover1) 
            self.a_star_algorithm(self.canvas1, self.cover1, self.end) 

        elif path3 == self.heuristic(self.start3, self.cover2) and self.cover2[0] < max(self.end[0], self.start3[0]) + 50 and \
            self.cover2[0] > min(self.end[0], self.start3[0]) - 50 and \
            self.cover2[1] < max(self.end[1], self.start3[1]) + 50 and \
            self.cover2[1] > min(self.end[1], self.start3[1]) - 50:
            self.a_star_algorithm(self.canvas1, self.start3, self.cover2) 
            self.a_star_algorithm(self.canvas1, self.cover2, self.end) 

        elif path3 == self.heuristic(self.start3, self.cover3) and self.cover3[0] < max(self.end[0], self.start3[0]) + 50 and \
            self.cover3[0] > min(self.end[0], self.start3[0]) - 50 and \
            self.cover3[1] < max(self.end[1], self.start3[1]) + 50 and \
            self.cover3[1] > min(self.end[1], self.start3[1]) - 50:
            self.a_star_algorithm(self.canvas1, self.start3, self.cover3) 
            self.a_star_algorithm(self.canvas1, self.cover3, self.end) 

        elif path3 == self.heuristic(self.start3, self.cover4) and self.cover4[0] < max(self.end[0], self.start3[0]) + 50 and \
            self.cover4[0] > min(self.end[0], self.start3[0]) - 50 and \
            self.cover4[1] < max(self.end[1], self.start3[1]) + 50 and \
            self.cover4[1] > min(self.end[1], self.start3[1]) - 50:
            self.a_star_algorithm(self.canvas1, self.start3, self.cover4) 
            self.a_star_algorithm(self.canvas1, self.cover4, self.end) 

        elif path3 == self.heuristic(self.start3, self.cover5) and self.cover5[0] < max(self.end[0], self.start3[0]) + 50 and \
            self.cover5[0] > min(self.end[0], self.start3[0]) - 50 and \
            self.cover5[1] < max(self.end[1], self.start3[1]) + 50 and \
            self.cover5[1] > min(self.end[1], self.start3[1]) - 50:
            self.a_star_algorithm(self.canvas1, self.start3, self.cover5) 
            self.a_star_algorithm(self.canvas1, self.cover5, self.end) 

        else: 
            self.a_star_algorithm(self.canvas1, self.start3, self.end)
        
    # function to make the path
    def reconstruct_path(self, canvas1, came_from, current):
        total_path = []
        while current: # reconstruct the three paths
            canvas1.create_image((current), image=self.path_color, anchor=NW) # getting an out of range error in this line
            total_path.append(current[:])
            current = came_from[current[0]][current[1]]
        print("Path found!")

def main():

    # create the root
    root = Tk()

    # for the background image - needed to pass it globally
    bg = PhotoImage(file = 'images/veterans.png') # to add the background image
    canvas1 = Canvas(width = 1000, height = 1000)
    canvas1.pack(fill = 'both', expand = True)
    canvas1.create_image(0,0,image = bg, anchor = 'nw')

    # --- load the colors (as png images of 1x1 pixel)  --- #
    # load the color used for the starting squads [blue]
    start_color = PhotoImage(file = 'images/start.png')
    # load the color used for the end node [red]
    end_color = PhotoImage(file = 'images/end.png')
    # load the color used for the cover node [green]
    cover_color = PhotoImage(file = 'images/cover.png')
    # load the color used for the obstacle node [magenta]
    obstacle_color = PhotoImage(file = 'images/obstacle.png')
    # load the color used for the path node [turquois]
    path_color = PhotoImage(file = 'images/path3.png')

    # need to pass the images to the app class - create the GUI
    app = App(root, canvas1, start_color, end_color, cover_color, obstacle_color, path_color)

    # start the algorithm when 'enter' is pressed
    root.bind('<Return>', app.find_path)

    # start the main loop
    root.mainloop()

if __name__ == "__main__":
    main()