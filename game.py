#!/usr/bin/python

import pygame
from pygame.locals import *
import launcher

pygame.init()
SURF = pygame.display.set_mode((500,400))
Black = (0,0,0)
Green = (0,128,0)
Sky_Blue = (135,206,235)
FPS = 30
fpsClock = pygame.time.Clock()

def main():
    while(True):
        draw_world(SURF)
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP:
                   launcher.changeAngle(3)
                if event.key == pygame.K_DOWN:
                    launcher.changeAngle(-3)
                if event.key == pygame.K_LEFT:
                    launcher.changeMagnitue(-5)
                if event.key == pygame.K_RIGHT:
                    launcher.changeMagnitude(5)
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
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
