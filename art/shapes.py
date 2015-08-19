from tealight.art import (color, line, spot, circle, box, image, text, background)

color("blue")

def handle_mousemove(x, y, button):
  color("white")
  spot(300, 200, 49)
  
  color("black")
  
  ox = (x - 300) / 15
  oy = (y - 200) / 15
  
  if ox > 20:
    ox = 20
  elif ox < -20:
    ox = -20
  
  if oy > 20:
    oy = 20
  elif oy < 20:
    oy = 20
  
  spot(300 + ox, 200 + oy, 20)
  
circle(300,200,50)
box(250,250,100,100)