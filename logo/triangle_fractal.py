from tealight.logo import move, turn, color

def tri(scale):
  for i in range(3):
    move(scale)
    turn(120)
    
    
def gradientmove(distance,
                 r1, g1, b1, a1, 
                 r2, g2, b2, a2,
                 step=1):
  for i in range(1, distance, step):
    j = distance - i
    col = ("rgba("
          + str((r1*i + r2*j)/distance) + ","
          + str((g1*i + g2*j)/distance) + ","
          + str((b1*i + b2*j)/distance) + ","
          + str((a1*i + a2*j)/distance) + ")")
    colour(col)
    print(col)
    move(step)
  
def trifrac(level, scale):
  if level == 0:
    return
  
  tri(scale)
  for i in range(3):
    move(scale)
    turn(120)
    trifrac(level - 1, scale/2)

color("white")
move(-250)
turn(-90)
move(-250)

gradientmove(100, 0, 0, 0, 0, 255, 255, 255, 0)

#color("blue")
#trifrac(10, 500)