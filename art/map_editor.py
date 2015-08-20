from tealight.art import *

poly = []
def handle_mousedown(x, y):
  poly.append((x, y))
  
  color("white")
  box(0, 0, screen_width, screen_height)
  
  color("red")
  fill_polygon(poly)