from tealight.art import *

mesh = []
index = 0
mesh.append([])

def handle_mousedown(x, y):
  print(mesh)
  
  mesh[index].append((x, y))
  
  color("white")
  box(0, 0, screen_width, screen_height)
  
  color("red")
  fill_polygon(mesh[index])
  
def handle_keydown(key):
  if key == "enter":
    mesh.append([])
    index += 1