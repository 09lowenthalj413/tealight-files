from tealight.robot import (move, 
                            turn, 
                            look, 
                            touch, 
                            smell, 
                            left_side, 
                            right_side)
from random import *

while True:
  move()
  
  chance = randint(0, 25 - smell())
  print(chance)
  if chance != 0:
    t = randint(-1, 2)
    #print(t)
    turn(t)
  else:
    print("THis actually happens!?")