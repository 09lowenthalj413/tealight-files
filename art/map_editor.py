from tealight.art import *

mesh = [[,]]
index = 0
def handle_mousedown(x, y):
  mesh[index].append((x, y))
  
  color("white")
  box(0, 0, screen_width, screen_height)
  
  color("red")
  fill_polygon(mesh[index])