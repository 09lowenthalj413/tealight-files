from tealight.art import *
from math import *

class Car:
  mesh = [(0, 60), (30, -20), (-30, -20)]
  angle = 0
  avel = 0
  pos = (200, 200)
  vel = (0, 0)
  friction = 0.99
  track = None
  
  def step(self):
    print(slef.angle)
    self.pos = (self.pos[0] + self.vel[0],
                self.pos[1] + self.vel[1])
    self.angle += self.avel
    
    self.vel = (self.vel[0] * self.friction,
                self.vel[1] * self.friction)
    self.avel = self.avel * self.friction
    
    res = [False, False, False]
    for i in range(0, 3):
      res[i] = self.track.check(self.pos[0] + self.mesh[i][0],
                                self.pos[1] + self.mesh[i][1])
  
  def draw(self):
    color("red")
    
    s = sin(self.angle)
    c = cos(self.angle)
    
    for i in range(0, 3):
      x0 = self.mesh[i%3 - 1][0]
      y0 = self.mesh[i%3 - 1][1]
      x1 = self.mesh[(i+1)%3 - 1][0]
      y1 = self.mesh[(i+1)%3 - 1][1]
      
      line(self.pos[0] + x0, self.pos[1] + y0,
           self.pos[0] + x1, self.pos[1] + y1)
  
  def applyImpulse(self, x, y, a=0):
    self.vel = (self.vel[0] + x, self.vel[1] + y)
    self.avel += a
    
  def __init__(self, racetrack):
    self.track = racetrack

  