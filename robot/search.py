from tealight.robot import (move, 
                            turn, 
                            look, 
                            touch, 
                            smell, 
                            left_side, 
                            right_side)
from random import *

print(smell)

last = smell()
while True:
  move()
  if last > smell():
    turn(randint(-2, 2))

# map seen 'no fruit' sight lines