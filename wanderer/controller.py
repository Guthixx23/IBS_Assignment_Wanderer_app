from wanderer.maze import Maze
from wanderer.hero import Hero
from wanderer.enemies import Enemies


# controller class that serves as the basis of interaction for all the other classes
class Controller():

    def __init__(self, canvas):
        self.canvas = canvas
        self.maze = Maze(canvas, self, 1)
        self.hero = Hero(canvas, self)
        self.enemies = Enemies(canvas, self)
        pass

    # reinstantiating maze to create a new level
    def next_level(self):
        self.canvas.delete("all")
        self.maze = Maze(self.canvas, self, self.maze.level + 1)
        self.enemies = Enemies(self.canvas, self)
        self.hero.position_row = 1
        self.hero.position_col = 1
        self.hero.move_character_to(1, 1)
        self.hero.has_key = False
        self.hero.heal()
