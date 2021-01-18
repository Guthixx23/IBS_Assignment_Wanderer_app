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
            self.enemies.append(Skeleton(self.canvas, self.controller))

        for i in self.enemies:
            i.draw(self.canvas, self.controller.maze)

        """
        print("-----------------")
        for i in controller.maze.layout:
            print(i)
        """