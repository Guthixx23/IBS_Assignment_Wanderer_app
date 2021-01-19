from tkinter import *
from wanderer.maze import Maze
from wanderer.hero import Hero
from wanderer.controller import Controller
from tkinter.font import Font
import random

# Create the tk environment as usual
root = Tk()
canvas = Canvas(root, width=715, height=720)

"""
img = PhotoImage(file="images/floor.gif")
canvas.create_image(40, 40, image=img)
"""

ctr = Controller(canvas)

var1 = StringVar()
# maze = Maze(canvas)
# hero = Hero(canvas)

def on_key_press(e):

    if not ctr.hero.is_fighting:
        current_pos = ctr.hero.get_hero_position()

        if e.keycode == 87:
            # up
            ctr.maze.draw_cell(ctr.hero.position_row, ctr.hero.position_col)
            ctr.hero.draw_hero_2(ctr.hero.position_row-1, ctr.hero.position_col)
            print("up [" + str(current_pos[0]) + "  " + str(current_pos[1]) + " ]")

        elif e.keycode == 83:
            # down
            ctr.maze.draw_cell(ctr.hero.position_row, ctr.hero.position_col)
            ctr.hero.draw_hero_2(ctr.hero.position_row+1, ctr.hero.position_col )
            print("down [" + str(current_pos[0]) + "  " + str(current_pos[1]) + " ]")
        elif e.keycode == 68:
            # right
            ctr.maze.draw_cell(ctr.hero.position_row, ctr.hero.position_col)
            ctr.hero.draw_hero_2(ctr.hero.position_row, ctr.hero.position_col+1 )
            print("right [" + str(current_pos[0]) + "  " + str(current_pos[1]) + " ]")
        elif e.keycode == 65:
            # left
            ctr.maze.draw_cell(ctr.hero.position_row, ctr.hero.position_col)
            ctr.hero.draw_hero_2(ctr.hero.position_row, ctr.hero.position_col-1)
            print("left [" + str(current_pos[0]) + "  " + str(current_pos[1]) + " ]")
    else:
        if e.keycode == 32:
            print("strike!")
            enemy = enemy = ctr.enemies.get_enemy_at(ctr.hero.position_row,ctr.hero.position_col)
            ctr.hero.strike(enemy)
            boss = ctr.enemies.get_boss()

            if enemy.current_hp <= 0:
                ctr.enemies.enemies.remove(enemy)
                ctr.hero.is_fighting = False
                ctr.hero.level_up()

                if enemy.has_key:
                    ctr.hero.has_key = True

                if ctr.hero.has_key and boss.current_hp <= 0:
                    ctr.next_level()
            else:
                enemy.strike(ctr.hero)
                if ctr.hero.current_hp <= 0:
                    quit()


    if ctr.enemies.get_enemy_at(ctr.hero.position_row,ctr.hero.position_col) != False:
        enemy = ctr.enemies.get_enemy_at(ctr.hero.position_row,ctr.hero.position_col)
        enemy_stat = enemy.display_stats()
        hero_stat = ctr.hero.display_stats()
        var1.set(hero_stat + "\t" + enemy_stat)
        ctr.hero.is_fighting = True
    else:
        hero_stat = ctr.hero.display_stats()
        var1.set(hero_stat)



    """
    for i in ctr.enemies.enemies:
        if i.position_row == ctr.hero.position_row and i.position_col == ctr.hero.position_col:
            var1.set("Hero (Level " + str(ctr.maze.level) + ") HP: " + str(ctr.hero.current_hp) + "/" + str(
                ctr.hero.hp) + " | DP: " + str(ctr.hero.dp) + " | SP: " + str(ctr.hero.sp) + "\t" + "Enemy HP: " + str(
                i.hp) + " | DP: " + str(i.dp) + " | SP: " + str(i.sp))
            break
        else:
            var1.set( " " + str(random.randint(1,10)) + "Hero (Level " + str(ctr.maze.level) + ") HP: " + str(ctr.hero.current_hp) + "/" + str(
                ctr.hero.hp) + " | DP: " + str(ctr.hero.dp) + " | SP: " + str(ctr.hero.sp))

    """
"""

# Creating a box that can draw itself in a certain position
box = Box()

# Create a function that can be called when a key pressing happens
def on_key_press(e):
    # When the keycode is 111 (up arrow) we move the position of our box higher
    if e.keycode == 111:
        box.testBoxY = box.testBoxY - 100
    elif e.keycode == 116:
        box.testBoxY = box.testBoxY + 100
    # and lower if the key that was pressed the down arrow
    # draw the box again in the new position
    box.draw(canvas)

"""

# Tell the canvas that we prepared a function that can deal with the key press events
canvas.bind("<KeyPress>", on_key_press)
"""
var1 = StringVar()
var1.set("Hero (Level " + str(ctr.maze.level) + ") HP: " + str(ctr.hero.current_hp) + "/" + str(
    ctr.hero.hp) + " | DP: " + str(ctr.hero.dp) + " | SP: " + str(ctr.hero.sp))
"""
my_font = Font(family="Times New Roman", size=12, weight="bold")
label_hero = Label(root, textvariable=var1, anchor=S, font=my_font)
var2 = StringVar()

canvas.pack()
label_hero.pack()

"""
for i in ctr.enemies.enemies:
    if i.position_row == ctr.hero.position_row and i.position_col == ctr.hero.position_col:
        var2.set("Szuper!!")
        label_enemy = Label(root, textvariable=var2, anchor=S, font=my_font)
        label_enemy.pack()
"""

# Select the canvas to be in focused so it actually recieves the key hittings
canvas.focus_set()

# Draw the box in the initial position
# box.draw(canvas)


root.mainloop()
