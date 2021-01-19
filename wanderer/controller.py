from wanderer.maze import Maze
from wanderer.hero import Hero
from wanderer.enemies import Enemies

class Controller():

    def __init__(self, canvas):
        self.canvas = canvas
        self.maze = Maze(canvas, self, 1)
        self.hero = Hero(canvas, self)
        self.enemies = Enemies(canvas, self)
        pass

    def next_level(self):
        self.canvas.delete("all")
        self.maze = Maze(self.canvas, self, self.maze.level + 1)
        self.enemies = Enemies(self.canvas, self)
        self.hero.position_row = 1
        self.hero.position_col = 1
        self.hero.draw_hero_2(1,1)
        self.hero.has_key = False
        self.hero.heal()
