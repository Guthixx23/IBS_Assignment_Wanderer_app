from tkinter import *
from wanderer.character import Character
import random


class Hero(Character):

    def __init__(self, canvas, controller):
        Character.__init__(self)
        self.hp = 20 + 3 * self.roll_d6()
        self.dp = 2 * self.roll_d6()
        self.sp = 5 + self.roll_d6()
        self.current_hp = self.hp
        self.name = "Hero"
        self.is_fighting = False
        self.level = 1
        self.has_key = False

        self.controller = controller
        self.canvas = canvas

        self.image_down = PhotoImage(file="images/hero-down.gif")
        self.image_right = PhotoImage(file="images/hero-right.gif")
        self.image_left = PhotoImage(file="images/hero-left.gif")
        self.image_up = PhotoImage(file="images/hero-up.gif")
        self.position_row = 1
        self.position_col = 1
        self.draw_hero_2(self.position_row, self.position_col)

    def draw_hero_2(self, row, col):
        if self.position_row == row and self.position_col == col:
            self.canvas.create_image((self.position_col - 1) * 72 + 36, (self.position_row - 1) * 72 + 36,
                                     image=self.image_down)

        # down
        if row == self.position_row + 1:
            if self.controller.maze.layout[self.position_row + 1][self.position_col] != 1:
                self.canvas.create_image((self.position_col - 1) * 72 + 36, (self.position_row) * 72 + 36,
                                         image=self.image_down)
                self.position_row = row
            else:
                self.canvas.create_image((self.position_col - 1) * 72 + 36, (self.position_row - 1) * 72 + 36,
                                         image=self.image_down)

        # up
        if row == self.position_row - 1:
            if self.controller.maze.layout[self.position_row - 1][self.position_col] != 1:
                self.canvas.create_image((self.position_col - 1) * 72 + 36, (self.position_row - 2) * 72 + 36,
                                         image=self.image_up)
                self.position_row = row
            else:
                self.canvas.create_image((self.position_col - 1) * 72 + 36, (self.position_row - 1) * 72 + 36,
                                         image=self.image_up)

        # left
        if col == self.position_col - 1:
            if self.controller.maze.layout[self.position_row][self.position_col - 1] != 1:
                self.canvas.create_image((self.position_col - 2) * 72 + 36, (self.position_row - 1) * 72 + 36,
                                         image=self.image_left)
                self.position_col = col
            else:
                self.canvas.create_image((self.position_col - 1) * 72 + 36, (self.position_row - 1) * 72 + 36,
                                         image=self.image_left)

        # right
        if col == self.position_col + 1:
            if self.controller.maze.layout[self.position_row][self.position_col + 1] != 1:
                self.canvas.create_image((self.position_col) * 72 + 36, (self.position_row - 1) * 72 + 36,
                                         image=self.image_right)
                self.position_col = col
            else:
                self.canvas.create_image((self.position_col - 1) * 72 + 36, (self.position_row - 1) * 72 + 36,
                                         image=self.image_right)

    """

    def draw_hero(self, x_pos, y_pos):

        if x_pos == self.position_row and y_pos == self.position_col:
            self.canvas.create_image((self.position_row - 1) * 72 + 36, (self.position_col - 1) * 72 + 36,
                                     image=self.image_down)

        if x_pos == self.position_row + 1:
            if self.controller.maze.layout[self.position_col][self.position_row + 1] != 1:
                self.canvas.create_image(self.position_row * 72 + 36, (self.position_col - 1) * 72 + 36,
                                         image=self.image_right)
                self.position_row = x_pos
            else:
                self.canvas.create_image((self.position_row - 1) * 72 + 36, (self.position_col - 1) * 72 + 36,
                                         image=self.image_right)

        if x_pos == self.position_row - 1:
            if self.controller.maze.layout[self.position_col][self.position_row - 1] != 1:
                self.canvas.create_image((self.position_row - 2) * 72 + 36, (self.position_col - 1) * 72 + 36,
                                         image=self.image_left)
                self.position_row = x_pos
            else:
                self.canvas.create_image((self.position_row - 1) * 72 + 36, (self.position_col - 1) * 72 + 36,
                                         image=self.image_left)

        if y_pos == self.position_col + 1:
            if self.controller.maze.layout[self.position_col + 1][self.position_row] != 1:
                self.canvas.create_image((self.position_row - 1) * 72 + 36, self.position_col * 72 + 36,
                                         image=self.image_down)
                self.position_col = y_pos
            else:
                self.canvas.create_image((self.position_row - 1) * 72 + 36, (self.position_col - 1) * 72 + 36,
                                         image=self.image_down)

        if y_pos == self.position_col - 1:
            if self.controller.maze.layout[self.position_col - 1][self.position_row] != 1:
                self.canvas.create_image((self.position_row - 1) * 72 + 36, (self.position_col - 2) * 72 + 36,
                                         image=self.image_up)
                self.position_col = y_pos
            else:
                self.canvas.create_image((self.position_row - 1) * 72 + 36, (self.position_col - 1) * 72 + 36,
                                         image=self.image_up)

    """

    def get_hero_position(self):
        return [self.position_col, self.position_row]

    def level_up(self):
        self.level += 1
        self.hp += self.roll_d6()
        self.dp += self.roll_d6()
        self.sp += self.roll_d6()

    def heal(self):
        i = random.randint(0, 9)

        if i in [0, 1, 2, 3, 4]:
            if self.current_hp < 0.9 * self.hp:
                self.current_hp += 0.1 * self.hp
            else:
                self.current_hp = self.hp
        elif i in [5, 6, 7, 8]:
            if self.current_hp < (2 * self.hp / 3):
                self.current_hp += self.hp / 3
            else:
                self.current_hp = self.hp
        else:
            self.current_hp = self.hp
