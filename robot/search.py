from tealight.robot import (move, 
                            turn, 
                            look, 
                            touch, 
                            smell, 
                            left_side, 
                            right_side)
from random import *

last = int(smell())
while True:
  if touch() == "wall":
    turn(2)
  
  move()
  if last > int(smell()):
    turn(randint(-2, 2))
  last = int(smell())

# map seen 'no fruit' sight lines