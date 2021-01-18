from wanderer.character import Character
from tkinter import *


class Boss(Character):

    def __init__(self, canvas, controller):
        Character.__init__(self)
        self.canvas = canvas
        self.controller = controller
        self.image = PhotoImage(file="images/boss.gif")

        self.hp = 2 * self.controller.maze.level * self.roll_d6() + self.roll_d6()
        self.dp = self.controller.maze.level / 2 * self.roll_d6() + self.roll_d6() / 2
        self.sp = self.controller.maze.level * self.roll_d6() + self.controller.maze.level
