from tealight.art import *
from math import *

class Car:
  mesh = [(0, 5), (3, -2), (-3, -2)]
  angle = 0
  pos = (0, 0)
  vel = (0, 0)
  
  def step():
    pass
  
  def draw():
    s = sin(angle)
    c = cos(angle)
    
    for i in range(0, 3):
      x0 = mesh[i%3 - 1][0]
      y0 = mesh[i%3 - 1][1]
      x1 = mesh[(i+1)%3 - 1][0]
      y1 = mesh[(i+1)%3 - 1][1]
      
      line(x0, y0, x1, y1)
      
      
car = Car()
car.draw()
  