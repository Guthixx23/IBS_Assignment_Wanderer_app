from wanderer.character import Character
from tkinter import *


class Boss(Character):

    def __init__(self, canvas, controller):
        Character.__init__(self)
        self.canvas = canvas
        self.controller = controller
        self.image = PhotoImage(file="images/boss.gif")
        self.name = "Boss"
        self.level = self.calculate_level()
        self.has_key = False

        self.hp = 2 * self.level * self.roll_d6() + self.roll_d6()
        self.current_hp = self.hp
        self.dp = self.level / 2 * self.roll_d6() + self.roll_d6() / 2
        self.sp = self.level * self.roll_d6() + self.level
