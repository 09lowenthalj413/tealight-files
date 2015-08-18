from tealight.logo import move, turn, color

def tri(scale):
  for i in range(3):
    move(scale)
    turn(120)
    
    
def gradientmove(distance,
                 r1, g1, b1, a1, 
                 r2, g2, b2, a2,
                 step=10):
  for i in range(0, distance, step):
    j = distance - i
    col = ("rgba("
          + str((r1*j + r2*i)/distance) + ","
          + str((g1*j + g2*i)/distance) + ","
          + str((b1*j + b2*i)/distance) + ","
          + str((a1*j + a2*i)/distance) + ")")
    
    color(col)
    move(step)
  
def trifrac(level, scale):
  if level == 0:
    return
  
  tri(scale)
  for i in range(3):
    move(scale)
    turn(120)
    trifrac(level - 1, scale/2)

gradientmove(100, 0, 0, 0, 0, 255, 255, 255, 0)

"""
color("white")
move(-250)
turn(-90)
move(-250)

color("blue")
trifrac(10, 500)
"""