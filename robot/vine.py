from tealight.robot import (move, 
                            turn,
                            touch)

def tree():
  count = 0
  while touch() == "fruit":
    move()
    count += 1
   
  turn(-1)
  if touch() == "fruit":
    tree()
    
  turn(2)
  if touch() == "fruit":
    tree()
    
  turn(1)
  for i in range(count):
    move()
    
  turn(2)
  
tree()
    
  
    
  
   
  