from tealight.art import *
from math import *

def rotate(x, y, theta):
  c = cos(theta)
  s = sin(theta)
  return (x*c - y*s, x*s + y*c)

class Car:
  mesh = [(0, 30), (15, -10), (-15, -10)]
  angle = 0
  avel = 0
  pos = (200, 200)
  vel = (0, 0)
  friction = 0.99
  track = None
  
  def step(self):
    self.pos = (self.pos[0] + self.vel[0],
                self.pos[1] + self.vel[1])
    self.angle += self.avel
    
    self.vel = (self.vel[0] * self.friction,
                self.vel[1] * self.friction)
    self.avel = self.avel * self.friction * 0.95
    
    self.angle = (self.angle + pi) % (2 * pi) - pi
    
    self.collide()
  
  def draw(self):
    color("red")
       
    for i in range(0, 3):
      a = rotate(self.mesh[i%3 - 1][0],
                 self.mesh[i%3 - 1][1],
                 self.angle)
      b = rotate(self.mesh[(i+1)%3 - 1][0],
                 self.mesh[(i+1)%3 - 1][1],
                 self.angle)
      
      line(self.pos[0] + a[0], self.pos[1] + a[1],
           self.pos[0] + b[0], self.pos[1] + b[1])
  
  def applyImpulse(self, x, y, a=0):
    self.vel = (self.vel[0] + x, self.vel[1] + y)
    self.avel += a
    
  def collide(self):
    for i in range(0, 3):
      if (self.track.check(self.pos[0] + self.mesh[i][0],
                           self.pos[1] + self.mesh[i][1])):
        self.vel = (-self.vel[0], -self.vel[1])
      
    
  def __init__(self, racetrack):
    self.track = racetrack

  