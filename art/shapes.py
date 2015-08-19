from tealight.art import (color, line, spot, circle, box, image, text, background)

color("blue")

def handle_mousemove(x, y, button):
  ox = (x - 300) / 15
  oy = (y - 200) / 15
  
  if ox**2 + oy**2 > (50-20)**2:
    ratio = float(ox**2 + oy**2) / (50-20)**2
    ox /= ratio
    oy /= ratio
  
  color("white")
  spot(300, 200, 49)
  
  color("black")
  spot(300 + ox, 200 + oy, 20)
  
circle(300,200,50)
box(250,250,100,100)