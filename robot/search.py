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
  for i in range(4):
    if look():
      move()
      break