from tealight.art import *

mesh = []
index = 0
mesh.append([])

def handle_mousedown(x, y):
  mesh[index].append((x, y))
  
def handle_keydown(key):
  global index
  if key == "return":
    if mesh[index] == []:
      mesh.pop()
      print(mesh)    
    mesh.append([])
    index += 1
    
def handle_frame():
  color("white")
  box(0, 0, screen_width, screen_height)
  color("red")
  
  for poly in mesh:
    if poly != []:
      fill_polygon(poly)