import random
from wanderer.skeleton import Skeleton
from wanderer.boss import Boss


class Enemies():

    def __init__(self, canvas, controller):
        self.canvas = canvas
        self.controller = controller
        self.enemies = []

        self.enemies.append(Boss(self.canvas, self.controller))

        #random.randint(2, 5)
        for i in range(random.randint(2, 5)):
            if i == 0:
                self.enemies.append(Skeleton(self.canvas, self.controller, True))
            else:
                self.enemies.append(Skeleton(self.canvas, self.controller, False))

        for i in self.enemies:
            i.draw(self.canvas, self.controller.maze)


    def get_enemy_at(self, row, col):

        for i in self.enemies:
            if i.position_row == row and i.position_col == col:
                return i

        return False

    def get_boss(self):
        return self.enemies[0]




