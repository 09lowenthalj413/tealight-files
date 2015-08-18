from tealight.robot import (move, 
                            turn, 
                            look, 
                            touch, 
                            smell, 
                            left_side, 
                            right_side)
from random import *

# This is a fairly useless algorithm!

while True:
  move()
  #turn(-1 to 2)
  if randint(0, 24 - smell()) != 0:
    turn(randint(-1, 2))