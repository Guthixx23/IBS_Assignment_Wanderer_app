import random


class Character():

    def __init__(self):
        self.hp = 0
        self.dp = 0
        self.sp = 0
        self.position_row = 0
        self.position_col = 0

    def roll_d6(self):
        return random.randint(1, 6)


    def find_empty_cell(self, maze):

        done = False
        i = 0
        j = 0

        while not done:
            i = random.randint(1,10)
            j = random.randint(1,10)

            if i == 1 and j == 1:
                continue

            if maze.layout[i][j] == 0:
                done = True
                maze.layout[i][j] = 2

        return [j,i]

    def draw(self, canvas, maze):
        i,j = self.find_empty_cell(maze)
        canvas.create_image((i-1) * 72 + 36, (j-1)  * 72 + 36,
                                 image=self.image)
        self.position_col = i
        self.position_row = j