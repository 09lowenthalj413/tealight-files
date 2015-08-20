from tealight.art import *
from math import *
from random import *

def star(x, y, w, h, spines):
  angle = 0
  for i in range(0, spines):
    x0 = x + (w * cos(angle)) + randint(0, 10)
    y0 = y + (h * sin(angle)) + randint(0, 10)
    line(x, y, x0, y0)
    angle = angle + (2 * pi / spines)

def rotate(x, y, theta):
  c = cos(theta)
  s = sin(theta)
  return (x*c - y*s, x*s + y*c)

class Car:
  mesh = [(0, 10), (5, -7), (-5, -7)]
  
  angle = 0
  avel = 0
  aacc = 0
  
  pos = (200, 250)
  vel = (0, 0)
  acc = (0, 0)
  
  friction = 0.99
  track = None
  
  def step(self):
    self.vel = (self.vel[0] + self.acc[0],
                self.vel[1] + self.acc[1])
    
    self.pos = (self.pos[0] + self.vel[0],
                self.pos[1] + self.vel[1])
    
    
    self.avel += self.aacc
    self.angle += self.avel
    
    self.collide()
    
    self.vel = (self.vel[0] * self.friction,
                self.vel[1] * self.friction)
    self.avel = self.avel * self.friction * 0.95
    
    self.angle = (self.angle + pi) % (2 * pi) - pi
  
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
        self.vel = (0, 0)
        star(self.pos[0], self.pos[1], 50, 50, 32)
      
    
  def __init__(self, racetrack):
    self.track = racetrack

  