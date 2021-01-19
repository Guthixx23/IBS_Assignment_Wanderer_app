import random


class Character():

    def __init__(self):
        self.hp = 0
        self.dp = 0
        self.sp = 0
        self.current_hp = 0
        self.level = 0
        self.position_row = 0
        self.position_col = 0

    def roll_d6(self):
        return random.randint(1, 6)

    def find_empty_cell(self, maze):

        done = False
        i = 0
        j = 0

        while not done:
            i = random.randint(1, 10)
            j = random.randint(1, 10)

            if i == 1 and j == 1:
                continue

            if maze.layout[i][j] == 0:
                done = True
                maze.layout[i][j] = 2

        return [j, i]

    def draw(self, canvas, maze):
        i, j = self.find_empty_cell(maze)
        canvas.create_image((i - 1) * 72 + 36, (j - 1) * 72 + 36,
                            image=self.image)
        self.position_col = i
        self.position_row = j

    def display_stats(self):
        """
        var1.set("Hero (Level " + str(ctr.maze.level) + ") HP: " + str(ctr.hero.current_hp) + "/" + str(
                ctr.hero.hp) + " | DP: " + str(ctr.hero.dp) + " | SP: " + str(ctr.hero.sp) + "\t" + "Enemy HP: " + str(
                i.hp) + " | DP: " + str(i.dp) + " | SP: " + str(i.sp))

        """
        return self.name + " (Level " + str(self.level) + ") HP: " + str(self.current_hp) + "/" + str(
            self.hp) + " | DP: " + str(self.dp) + " | SP: " + str(self.dp)

    def calculate_level(self):
        i = random.randint(0,9)
        chance1 = [0,1,2,3,4]
        chance2 = [5,6,7,8]

        if i in chance1:
            return self.controller.maze.level
        elif i in chance2:
            return self.controller.maze.level + 1
        else:
            return self.controller.maze.level + 2

    def strike(self, defender):
        strike_value = 2 * self.roll_d6() + self.sp
        if strike_value > defender.dp:
            defender.current_hp -= (strike_value - defender.dp)


