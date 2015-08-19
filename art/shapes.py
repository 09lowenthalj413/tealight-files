from tealight.art import (color, line, spot, circle, box, image, text, background)

color("blue")

def handle_mousemove(x, y, button):
  color("white")
  spot(300, 200, 49)
  
  color("black")
  
  newx = 300 + (x - 300) / 15
  newy = 200 + (y - 200) /15
  spot(newx, newy, 20)
  
circle(300,200,50)
box(250,250,100,100)