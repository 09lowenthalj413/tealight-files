from tealight.robot import (move, 
                            turn, 
                            look, 
                            touch, 
                            smell, 
                            left_side, 
                            right_side)
from random import *

#last = smell()
#while True:
#  move()
#  if last < smell()

while True:
  if look() == "fruit":
    move()
  else:
    turn(randint(-1, 2))