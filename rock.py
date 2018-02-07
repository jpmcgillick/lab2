#!/usr/bin/python

import pygame
from pygame.locals import *
import math
import sys
GREY = (128,128,128)

class Rock:
  def __init__(self,x,y):
    #TODO figure stuff out
    self.x = x
    self.y = y
    self.vx = 0
    self.vy = 0
    
  def isMoving(self,):
    return (self.vx !=0) or (self.vy !=0)
    
  def move(self,time):
    self.x = self.x + self.vx*time
    self.y = self.y - self.vy*time 

  def draw(self,SURF):
    r = pygame.Rect((0,0,10,10))
    r.center = (self.x,self.y)
    pygame.draw.rect(SURF,GREY, r)
