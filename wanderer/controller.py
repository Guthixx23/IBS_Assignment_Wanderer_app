from wanderer.maze import Maze
from wanderer.hero import Hero
from wanderer.enemies import Enemies

class Controller():

    def __init__(self, canvas):
        self.canvas = canvas
        self.maze = Maze(canvas, self)
        self.hero = Hero(canvas, self)
        self.enemies = Enemies(canvas, self)
        pass