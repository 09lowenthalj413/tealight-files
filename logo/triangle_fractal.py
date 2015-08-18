from tealight.logo import move, turn, color

def tri(scale):
  for i in range(3):
    move(scale)
    turn(120)
    

def trifrac(level, scale):
  if level == 0:
    return
  
  tri(scale)
  for i in range(3):
    trifrac(level - 1, scale/2)
    move(scale)
    turn(120)

color("white")
move(-250)
turn(-90)
move(-250)

color("blue")
trifrac(10, 500)