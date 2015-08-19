from tealight.art import (color, line, spot, circle, box, image, text, background)

color("blue")

def handle_mousemove(x, y, button):
  color("white")
  spot(300, 200, 49)
  
  color("black")
  spot(300 + (x - 300) / 100,
       200 + (y - 200) / 100,
       30)
  

spot(280,200,30)
circle(300,200,50)
box(250,250,100,100)