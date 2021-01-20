# IBS_guthixx23_wanderer

### Introduction
The Wanderer is a single player role playing game where the goal is to fight
off the evil skeletons and the boss in each level of a maze. Get stronger by
defeating as many foes as you can because even more fearsome opponents are
waiting for you on higher levels!

### Development environment and dependencies

The application was developed in python 3.9. Alongside the basic python 
libraries Tkinter was used for the visuals and Random was used for random
number generation. 

To run the game make sure you have python version 3.X and tkinter available.
Tu run the game open the command line in the package and use the following 
command:

```
python main.py
```

### How to use

Navigate your hero with "WASD" or the arrows alternatively. If you encounter
a monster (step on the same cell with a monster) you have to fight it. 
Strike by pressing the space bar, and observe your stats at the bottom of 
the screen. If you found the key and killed the boss, you are automatically
transferred to the next level.


### Features and edge cases
Monsters are moving randomly but only on every second move of the hero. If 
they happen to outrun you in a corner wait a turn and catch them!

*If the hero would step on a cell which the monster is moving away from 
the fight is not started. The same phenomenon can happen when the hero and 
the monster are moving towards each other, resulting in a switch of cells*

### Tips and tricks

Try to kill as many skeletons as possible to level up, before you go to
the next level, to maximize the potential healing.

### Extras

Every time the hero enters a new level in the maze a random map is generated. Then 
the validity of the map is checked. If a map is valid (all the floor tiles are 
connected, there are no unreachable parts) then the hero progresses on the said level.
Otherwise the default map is displayed. The reason behind not having random maps every
time the hero advances in teh maze is that the algorithm checking the validity 
tremendously slows down the rendering. To avoid that, bot the number of wall blocks
and the occurence of a random map were limited.

Random events are also implemented in the game. With a 1 in 8 chance monsters are 
paralyzed on the given level making them unable to move.

