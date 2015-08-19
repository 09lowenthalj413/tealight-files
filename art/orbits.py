from tealight.art import (color, line, spot, circle, box, image, text, background)
from tealight.art import screen_width, screen_height
from math import sqrt

x = screen_width / 2 - 100
y = screen_height / 2
vx = 0
vy = 1
m = 1
g = 981

power = 0.4

def handle_keydown(key):
  global vx, vy
  
  if key == "left":
    vx -= power / m
  elif key == "right":
    vx += power / m
  elif key == "up":
    vy -= power / m
  elif key == "down":
    vy += power / m
    
def handle_frame():
  global x,y,vx,vy
  
  color("white")
  spot(x,y,8)
  
  rx = x - screen_width / 2
  ry = y - screen_height / 2
  
  magsq = rx**2 + ry**2
  if magsq != 0:
    # normalise
    mag = sqrt(magsq)
    rx /= mag
    ry /= mag
    
    # apply inverse square rule
    rx *= g/magsq
    ry *= g/magsq
    
    vx -= rx / m
    vy -= ry / m
  
  x = x + vx
  y = y + vy
  
  color("blue")
  spot(x,y,8)
  
  
