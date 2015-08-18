from tealight.robot import (move, 
                            turn, 
                            look, 
                            touch, 
                            smell, 
                            left_side, 
                            right_side)
from random import *

last = smell()
print(last)
while True:
  move()
  if last > smell():
    turn(randint(-2, 2))
  last = smell()

# map seen 'no fruit' sight lines