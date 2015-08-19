from tealight.art import (color, line, spot, circle, box, image, text, background)

from tealight.net import connect, send

lastx = 0
lasty = 0

color("blue")
connect("shared_whiteboard")

def handle_mousedown(x,y):
  global lastx, lasty
  
  lastx = x
  lasty = y

def handle_mousemove(x,y,button):
  global lastx, lasty
  
  if button == "left":
    line(lastx, lasty, x, y)
    send({"x1": lastx, "y1": lasty, "x2": x, "y2": y})
    lastx = x
    lasty = y
  
def handle_message(message):
  line(message["x1"], message["y1"], message["x2"], message["y2"])
  
def handle_keydown(key):
  max_xy = 1000
  if key == "right":
    for x in range(max_xy):
      line(x, 0, x, max_xy)
      send({"x1": x, "y1": 0, "x2": x, "y2": max_xy})