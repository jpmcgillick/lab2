#!/usr/bin/python

import pygame
from pygame.locals import *
import math
import sys

FPS = 30
max_mag = 100
min_mag = 10
max_angle = 90
min_angle = 0
RED = (128,0,0)

class Launcher:
  def __init__(self,x,y):
    self.locationx = x
    self.locationy = y
    self.magnitude = 20
    self.angle = 45

  def changeMagnitude(self,delta):
    new_mag = self.magnitude + delta
    if new_mag >= max_mag:
        self.magnitude = max_mag
    elif new_mag <= min_mag:
        self.magnitude = min_mag
    else:
        self.magnitude = new_mag

  def fire(self,rock):
    rock.vx = self.magnitude*math.cos(self.angle*math.pi/180)
    rock.vy = self.magnitude*math.sin(self.angle*math.pi/180)

  def changeAngle(self,delta):
    new_angle = self.angle + delta
    if new_angle >= max_angle:
        self.angle = max_angle
    elif new_angle <= min_angle:
        self.angle = min_angle
    else:
        self.angle = new_angle

  def draw(self,SURF):
    xend=self.locationx+self.magnitude*math.cos(math.radians(self.angle))
    yend=self.locationy-self.magnitude*math.sin(math.radians(self.angle))
    pygame.draw.line(SURF, RED, (self.locationx, self.locationy), (xend,yend), 10)
