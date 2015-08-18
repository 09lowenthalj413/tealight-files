from tealight.logo import move, turn

def tri(scale):
  for i in range(3):
    move(scale)
    turn(120)
    

def trifrac(scale):
  if scale == 1:
    return
  
  tri(scale)
  for i in range(3):
    move(scale)
    turn(120)
    trifrac(scale/2)

turn(-60)
trifrac(100)