#!/usr/bin/python

import pygame
from pygame.locals import *
import math

FPS = 30
max_mag = 100
min_mag = 10
max_angle = 90
min_angle = 0
Red = (128,0,0)

class Launcher:
  def __init__(self,x,y):
    self.location = (x,y)
    self.magnitude = 20
    self.angle = 45
    launcher.draw(SURF)

  def changeMagnitude(delta):
    new_mag = self.magnitude + delta
    if new_mag >= max_mag:
        self.magnitude = max_mag
    elif new_mag <= min_mag:
        self.magnitude = min_mag
    else:
        self.magnitude = new_mag
    launcher.draw(SURF)


  def changeAngle(delta):
    new_angle = self.angle + delta
    if new_angle >= max_angle:
        self.angle = max_angle
    elif new_angle <= min_angle:
        self.angle = min_angle
    else:
        self.angle = new_angle
    launcher.draw(SURF)


  def draw(SURF):
    xend=self.x+self.magnitude*math.cos(math.radians(self.angle))
    yend=self.y-self.magnitude*math.sin(math.radians(self.angle))
    pygame.draw.rect(surf, RED, (xend,yend), 10)
