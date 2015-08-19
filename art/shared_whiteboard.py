from tealight.art import (color, line, spot, circle, box, image, text, background, screen_width, screen_height)

from tealight.net import connect, send

lastx = 0
lasty = 0

color("blue")
connect("shared_whiteboard")

def fill(colour):
  color(colour)
  for x in range(screen_width):
    line(x, 0, x, screen_height)
    send({"x1": x, "y1": 0, "x2": x, "y2": screen_height})
    return

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
  if key == "right":
    fill("black")