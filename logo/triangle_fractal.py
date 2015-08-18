from tealight.logo import move, turn

def tri(scale):
  for i in range(3):
    move(scale)
    turn(120)
    

def trifrac(level, scale):
  if level == 0:
    return
  
  tri(scale)
  for i in range(3):
    move(scale)
    turn(120)
    trifrac(level - 1, scale/2)

move(-250)
turn(-90)
move(-250)
trifrac(4, 500)