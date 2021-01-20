from tkinter import *
import random


# maze class
class Maze():

    def __init__(self, canvas, controller, level):
        self.controller = controller
        self.canvas = canvas
        self.level = level
        self.wall = PhotoImage(file="images/wall.gif")
        self.floor = PhotoImage(file="images/floor.gif")
        self.hero = PhotoImage(file="images/hero-down.gif")
        self.layout = []
        self.tracker_grid = []
        self.validity_count = 0

        self.init_tracker_grid()
        self.init_layout()
        self.set_map()
        self.draw_maze()

    # function to draw maze
    def draw_maze(self):

        for i in range(1, 11):
            for j in range(1, 11):
                self.draw_cell(i, j)

    # function to represent layout in list format
    def init_layout(self):
        for i in range(0, 12):
            temp = []
            for j in range(0, 12):
                if i == 0 or i == 11 or j == 0 or j == 11:
                    temp.append(1)
                else:
                    temp.append(0)
            self.layout.append(temp)

    # setting map either to default or random
    def set_map(self):
        number_of_walls = random.randint(10, 17)
        self.random_map(number_of_walls)

        if not self.validate_map(1, 1, number_of_walls):
            self.layout = []
            self.init_layout()
            self.default_map()

    # initializer function to default map
    def default_map(self):
        self.layout[1][4] = 1
        self.layout[2][4] = 1
        self.layout[2][6] = 1
        self.layout[2][8] = 1
        self.layout[2][9] = 1
        self.layout[3][2] = 1
        self.layout[3][3] = 1
        self.layout[3][4] = 1
        self.layout[3][6] = 1
        self.layout[3][8] = 1
        self.layout[3][9] = 1
        self.layout[4][6] = 1
        self.layout[5][1] = 1
        self.layout[5][2] = 1
        self.layout[5][3] = 1
        self.layout[5][4] = 1
        self.layout[5][6] = 1
        self.layout[5][7] = 1
        self.layout[5][8] = 1
        self.layout[5][9] = 1
        self.layout[6][2] = 1
        self.layout[6][4] = 1
        self.layout[7][2] = 1
        self.layout[7][4] = 1
        self.layout[7][6] = 1
        self.layout[7][7] = 1
        self.layout[7][9] = 1
        self.layout[8][6] = 1
        self.layout[8][7] = 1
        self.layout[8][9] = 1
        self.layout[9][2] = 1
        self.layout[9][3] = 1
        self.layout[9][4] = 1
        self.layout[9][9] = 1
        self.layout[10][4] = 1
        self.layout[10][6] = 1
        self.layout[10][7] = 1

    # function to redraw a single cell to its original form
    def draw_cell(self, col, row):
        if self.layout[col][row] == 1:
            self.canvas.create_image((row - 1) * self.wall.width() + self.wall.width() / 2,
                                     (col - 1) * self.wall.width() + self.wall.width() / 2, image=self.wall)
        else:
            self.canvas.create_image((row - 1) * self.floor.width() + self.floor.width() / 2,
                                     (col - 1) * self.floor.width() + self.floor.width() / 2, image=self.floor)

    # randomly placing wall blocks in the maze
    def random_map(self, number_of_walls):
        for i in range(number_of_walls):
            k = random.randint(1, 10)
            l = random.randint(1, 10)

            if k == 1 and l == 1:
                continue

            elif self.layout[k][l] != 1:
                self.layout[k][l] = 1

    # initializing the tracker grid used in validity check
    def init_tracker_grid(self):
        self.tracker_grid.append([1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1])
        for i in range(10):
            self.tracker_grid.append([1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1])
        self.tracker_grid.append([1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1])

    # flood fill algorythm to check whether all floor tiles are connected in the maze.
    def validate_map(self, row, col, number_of_walls):

        self.tracker_grid[row][col] = 1

        if self.layout[row][col] == 0:
            self.validity_count += 1

        if self.layout[row + 1][col] == 0 and self.tracker_grid[row + 1][col] == 0:
            self.validate_map(row + 1, col, number_of_walls)
        if self.layout[row - 1][col] == 0 and self.tracker_grid[row - 1][col] == 0:
            self.validate_map(row - 1, col, number_of_walls)
        if self.layout[row][col + 1] == 0 and self.tracker_grid[row][col + 1] == 0:
            self.validate_map(row, col + 1, number_of_walls)
        if self.layout[row][col - 1] == 0 and self.tracker_grid[row][col - 1] == 0:
            self.validate_map(row, col - 1, number_of_walls)

        if self.validity_count + number_of_walls == 100:
            return True
        else:
            return False
