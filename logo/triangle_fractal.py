from tealight.logo import move, turn

def tri(scale):
  for i in range(3):
    move(scale)
    turn(120)
    

def trifrac(level, scale):
  if level == 0:
    return
  
  s = level * scale
  tri(s)
  for i in range(3):
    move(s)
    turn(120)
    trifrac(level-1, scale)

turn(-90)
trifrac(2, 100)