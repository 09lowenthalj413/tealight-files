from tealight.logo import move, turn

def tri(scale):
  for i in range(3):
    move(scale)
    turn(120)
    

def trifrac(scale):
  if scale == 1:
    return
  
  tri(scale*4)
  for i in range(3):
    move(scale*4)
    turn(120)
    trifrac(scale*4/2)

turn(-90)
trifrac(100)