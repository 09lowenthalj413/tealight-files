from tealight.art import *
from math import *
from random import *

from github.dhs11.art.race_track import *

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
  
  pos = checkpoints[0]
  vel = (0, 0)
  
  friction = 0.9
  
  cc = 0
  laps = 0
  
  def step(self):
    self.pos = (self.pos[0] + self.vel[0],
                self.pos[1] + self.vel[1])
    self.angle += self.avel
    
    self.collide()
    
    self.vel = (self.vel[0] * self.friction,
                self.vel[1] * self.friction)
    self.avel = self.avel * self.friction * 0.95
    
    self.angle = (self.angle + pi) % (2 * pi) - pi
  
  def draw(self):
    color("red")
    
    text(self.pos[0], self.pos[1],
         "C" + str(self.cc + 1) + " L" + str(self.laps))
       
    for i in range(0, 3):
      a = rotate(self.mesh[i%3 - 1][0],
                 self.mesh[i%3 - 1][1],
                 self.angle)
      b = rotate(self.mesh[(i+1)%3 - 1][0],
                 self.mesh[(i+1)%3 - 1][1],
                 self.angle)
      
      line(self.pos[0] + a[0], self.pos[1] + a[1],
           self.pos[0] + b[0], self.pos[1] + b[1])
      
    back = (self.mesh[1][0] - self.mesh[2][0],
            self.mesh[1][1] - self.mesh[2][1])
    flames = 10
    step = (back[0] / flames, back[1] / flames)
    
    for i in range(flames):
      pos = rotate(self.mesh[1][0] + i * step[0],
                   self.mesh[1][1] + i * step[1],
                   self.angle)
      pos = (pos[0] + self.pos[0],
             pos[1] + self.pos[1])
      back = rotate(back[0], back[1], self.angle)
      line(pos[0], pos[1],
           pos[0] - back[1]
           #* randint(0, int(self.vel[0]**2 + self.vel[1]**2)),
           pos[1] + back[0]
           #* randint(0, int(self.vel[0]**2 + self.vel[1]**2)))
           
  
  def applyImpulse(self, x, y, a=0):
    self.vel = (self.vel[0] + x, self.vel[1] + y)
    self.avel += a
    
  def collide(self):
    for i in range(0, 3):
      check_check(self.pos[0], self.pos[1], self)
      if (check_track(self.pos[0] + self.mesh[i][0],
                      self.pos[1] + self.mesh[i][1])):
        #self.vel = (0, 0)
        line(self.pos[0] + self.mesh[i][0],
             self.pos[1] + self.mesh[i][1],
             self.pos[0] + self.mesh[i][0] + randint(-30, 30),
             self.pos[1] + self.mesh[i][1] + randint(-30, 30))
        self.vel = (-self.vel[0] * 0.5, -self.vel[1] * 0.5)

  