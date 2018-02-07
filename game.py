#!/usr/bin/python

import pygame
from pygame.locals import *
import sys

import launcher
import rock

pygame.init()
SURF = pygame.display.set_mode((500,400))
Black = (0,0,0)
Green = (0,128,0)
Sky_Blue = (135,206,235)
FPS = 30
fpsClock = pygame.time.Clock()
x = 0
y = 380
my_launcher = launcher.Launcher(x,y)
my_rock = rock.Rock(x,y)

def main():
    while(True):
        #1. Pygame events
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP:
                   my_launcher.changeAngle(3)
                if event.key == pygame.K_DOWN:
                    my_launcher.changeAngle(-3)
                if event.key == pygame.K_LEFT:
                    my_launcher.changeMagnitude(-5)
                if event.key == pygame.K_RIGHT:
                    my_launcher.changeMagnitude(5)
                if (event.key == pygame.K_SPACE) and (not my_rock.isMoving()):
                    my_launcher.fire(my_rock)
                    print("FIRE!")
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
        #2. Game logic
        my_rock.move(1.0/FPS)
        #3. Draw everything
        draw_world(SURF)
        my_launcher.draw(SURF)
        my_rock.draw(SURF)
        pygame.display.update()
        fpsClock.tick(FPS)

        
def draw_world(SURF):
    pygame.display.set_caption('Launchr 1.0')
    SURF.fill(Sky_Blue)
    pygame.draw.rect(SURF,Green,(0,380,500,20))
    Title = pygame.font.Font('freesansbold.ttf',24)
    TitleObj = Title.render('Launchr 1.0',True,Black)
    TitleRectObj = TitleObj.get_rect()
    TitleRectObj.center = (250,30)
    SURF.blit(TitleObj, TitleRectObj)
main()
