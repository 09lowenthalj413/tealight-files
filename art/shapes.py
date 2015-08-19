from tealight.art import (color, line, spot, circle, box, image, text, background)

color("blue")

def handle_mousemove(x, y, button):
  color("white")
  spot(300, 200, 49)
  
  color("black")
  
  ox = (x - 300) / 15
  oy = (y - 200) / 15
  
  ox = (ox + 20) % 40
  
  spot(300 + newx, 200 + newy, 20)
  
circle(300,200,50)
box(250,250,100,100)