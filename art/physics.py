from tealight.art import *
from math import *

class Car:
  mesh = [(0, 5), (3, -2), (-3, -2)]
  angle = 0
  pos = (0, 0)
  vel = (0, 0)
  
  def step(self):
    pass
  
  def draw(self):
    s = sin(self.angle)
    c = cos(self.angle)
    
    for i in range(0, 3):
      x0 = self.mesh[i%3 - 1][0]
      y0 = self.mesh[i%3 - 1][1]
      x1 = self.mesh[(i+1)%3 - 1][0]
      y1 = self.mesh[(i+1)%3 - 1][1]
      
      line(x0, y0, x1, y1)
      
      
car = Car()
car.draw()
  