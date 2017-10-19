import pygame, sys,LUDOfunctions
from LUDOfunctions import *

pygame.init()

#COLORS         R   G   B
WHITE       = (255,255,255)
LIGHTGREEN  = (153,255,153)
GREEN       = ( 51,255, 51)
PINK        = (255,153,204)
RED         = (255, 51, 51)
LIGHTYELLOW = (255,255,153)
YELLOW      = (255,255, 51)
LIGHTBLUE   = (204,255,255)
BLUE        = (  0,128,255)
BLACK       = (  0,  0,  0)

#CONSTANTS
WIDTH = 1100    #Change the value of width in order to adjust your screen surface!(should be divisible by 11)
HEIGHT = WIDTH

#Setting up the surface
gameDisplay = pygame.display.set_mode((WIDTH,HEIGHT))
pygame.display.set_caption('LUDO')
gameDisplay.fill(WHITE)

def drawBoard():
    #Drawing LUDO board
    pygame.draw.polygon(gameDisplay, YELLOW, ((4*(WIDTH/11),4*(WIDTH/11)), (7*(WIDTH/11),4*(WIDTH/11)), (5.5*(WIDTH/11),5.5*(WIDTH/11))))
    pygame.draw.polygon(gameDisplay, GREEN, ((4*(WIDTH/11),4*(WIDTH/11)), (4*(WIDTH/11),7*(WIDTH/11)), (5.5*(WIDTH/11),5.5*(WIDTH/11))))
    pygame.draw.polygon(gameDisplay, RED, ((4*(WIDTH/11),7*(WIDTH/11)), (7*(WIDTH/11),7*(WIDTH/11)), (5.5*(WIDTH/11),5.5*(WIDTH/11))))
    pygame.draw.polygon(gameDisplay, BLUE, ((7*(WIDTH/11),4*(WIDTH/11)), (7*(WIDTH/11),7*(WIDTH/11)), (5.5*(WIDTH/11),5.5*(WIDTH/11))))
    
    #Main Boxes
    pygame.draw.rect(gameDisplay, LIGHTYELLOW, (7*(WIDTH/11),0,4*(WIDTH/11),4*(WIDTH/11)))
    pygame.draw.rect(gameDisplay, LIGHTBLUE, (7*(WIDTH/11),7*(WIDTH/11),4*(WIDTH/11),4*(WIDTH/11)))
    pygame.draw.rect(gameDisplay, LIGHTGREEN, (0,0,4*(WIDTH/11),4*(WIDTH/11)))
    pygame.draw.rect(gameDisplay, PINK, (0,7*(WIDTH/11),4*(WIDTH/11),4*(WIDTH/11)))

    pygame.draw.rect(gameDisplay, YELLOW, (7.5*(WIDTH/11),0.5*(WIDTH/11),3*(WIDTH/11),3*(WIDTH/11)))
    pygame.draw.rect(gameDisplay, BLUE, (7.5*(WIDTH/11),7.5*(WIDTH/11),3*(WIDTH/11),3*(WIDTH/11)))
    pygame.draw.rect(gameDisplay, GREEN, (0.5*(WIDTH/11),0.5*(WIDTH/11),3*(WIDTH/11),3*(WIDTH/11)))
    pygame.draw.rect(gameDisplay, RED, (0.5*(WIDTH/11),7.5*(WIDTH/11),3*(WIDTH/11),3*(WIDTH/11)))

    pygame.draw.rect(gameDisplay, YELLOW, (5*(WIDTH/11),0.5*(WIDTH/11),1*(WIDTH/11),4*(WIDTH/11)))
    pygame.draw.rect(gameDisplay, BLUE, (7*(WIDTH/11),5*(WIDTH/11),3.5*(WIDTH/11),1*(WIDTH/11)))
    pygame.draw.rect(gameDisplay, GREEN, (0.5*(WIDTH/11),5*(WIDTH/11),4*(WIDTH/11),1*(WIDTH/11)))
    pygame.draw.rect(gameDisplay, RED, (5*(WIDTH/11),7*(WIDTH/11),1*(WIDTH/11),3.5*(WIDTH/11)))

    pygame.draw.rect(gameDisplay, YELLOW, (6*(WIDTH/11),0.5*(WIDTH/11),1*(WIDTH/11),0.5*(WIDTH/11)))
    pygame.draw.rect(gameDisplay, BLUE, (10*(WIDTH/11),6*(WIDTH/11),0.5*(WIDTH/11),1*(WIDTH/11)))
    pygame.draw.rect(gameDisplay, GREEN, (0.5*(WIDTH/11),4*(WIDTH/11),0.5*(WIDTH/11),1*(WIDTH/11)))
    pygame.draw.rect(gameDisplay, RED, (4*(WIDTH/11),10*(WIDTH/11),1*(WIDTH/11),0.5*(WIDTH/11)))

    pygame.draw.circle(gameDisplay, LIGHTYELLOW, (int(8.25*(WIDTH/11)),int(1.25*(WIDTH/11))),int(0.4*(WIDTH/11)))
    pygame.draw.circle(gameDisplay, LIGHTYELLOW, (int(9.75*(WIDTH/11)),int(1.25*(WIDTH/11))),int(0.4*(WIDTH/11)))
    pygame.draw.circle(gameDisplay, LIGHTYELLOW, (int(8.25*(WIDTH/11)),int(2.75*(WIDTH/11))),int(0.4*(WIDTH/11)))
    pygame.draw.circle(gameDisplay, LIGHTYELLOW, (int(9.75*(WIDTH/11)),int(2.75*(WIDTH/11))),int(0.4*(WIDTH/11)))

    pygame.draw.circle(gameDisplay, LIGHTGREEN, (int(1.25*(WIDTH/11)),int(1.25*(WIDTH/11))),int(0.4*(WIDTH/11)))
    pygame.draw.circle(gameDisplay, LIGHTGREEN, (int(2.75*(WIDTH/11)),int(1.25*(WIDTH/11))),int(0.4*(WIDTH/11)))
    pygame.draw.circle(gameDisplay, LIGHTGREEN, (int(1.25*(WIDTH/11)),int(2.75*(WIDTH/11))),int(0.4*(WIDTH/11)))
    pygame.draw.circle(gameDisplay, LIGHTGREEN, (int(2.75*(WIDTH/11)),int(2.75*(WIDTH/11))),int(0.4*(WIDTH/11)))

    pygame.draw.circle(gameDisplay, LIGHTBLUE, (int(8.25*(WIDTH/11)),int(8.25*(WIDTH/11))),int(0.4*(WIDTH/11)))
    pygame.draw.circle(gameDisplay, LIGHTBLUE, (int(9.75*(WIDTH/11)),int(9.75*(WIDTH/11))),int(0.4*(WIDTH/11)))
    pygame.draw.circle(gameDisplay, LIGHTBLUE, (int(8.25*(WIDTH/11)),int(9.75*(WIDTH/11))),int(0.4*(WIDTH/11)))
    pygame.draw.circle(gameDisplay, LIGHTBLUE, (int(9.75*(WIDTH/11)),int(8.25*(WIDTH/11))),int(0.4*(WIDTH/11)))

    pygame.draw.circle(gameDisplay, PINK, (int(1.25*(WIDTH/11)),int(8.25*(WIDTH/11))),int(0.4*(WIDTH/11)))
    pygame.draw.circle(gameDisplay, PINK, (int(1.25*(WIDTH/11)),int(9.75*(WIDTH/11))),int(0.4*(WIDTH/11)))
    pygame.draw.circle(gameDisplay, PINK, (int(2.75*(WIDTH/11)),int(8.25*(WIDTH/11))),int(0.4*(WIDTH/11)))
    pygame.draw.circle(gameDisplay, PINK, (int(2.75*(WIDTH/11)),int(9.75*(WIDTH/11))),int(0.4*(WIDTH/11)))

    pygame.draw.line(gameDisplay, BLACK, (int(0.5*(WIDTH/11)),int(4*(WIDTH/11))),(int(0.5*(WIDTH/11)),int(7*(WIDTH/11))),int(0.05*(WIDTH/11)))
    pygame.draw.line(gameDisplay, BLACK, (int(1*(WIDTH/11)),  int(4*(WIDTH/11))),(int(1*(WIDTH/11)),  int(7*(WIDTH/11))),int(0.05*(WIDTH/11)))
    pygame.draw.line(gameDisplay, BLACK, (int(1.5*(WIDTH/11)),int(4*(WIDTH/11))),(int(1.5*(WIDTH/11)),int(7*(WIDTH/11))),int(0.05*(WIDTH/11)))
    pygame.draw.line(gameDisplay, BLACK, (int(2*(WIDTH/11)),  int(4*(WIDTH/11))),(int(2*(WIDTH/11)),  int(7*(WIDTH/11))),int(0.05*(WIDTH/11)))
    pygame.draw.line(gameDisplay, BLACK, (int(2.5*(WIDTH/11)),int(4*(WIDTH/11))),(int(2.5*(WIDTH/11)),int(7*(WIDTH/11))),int(0.05*(WIDTH/11)))
    pygame.draw.line(gameDisplay, BLACK, (int(3*(WIDTH/11)),  int(4*(WIDTH/11))),(int(3*(WIDTH/11)),  int(7*(WIDTH/11))),int(0.05*(WIDTH/11)))
    pygame.draw.line(gameDisplay, BLACK, (int(3.5*(WIDTH/11)),int(4*(WIDTH/11))),(int(3.5*(WIDTH/11)),int(7*(WIDTH/11))),int(0.05*(WIDTH/11)))
    pygame.draw.line(gameDisplay, BLACK, (int(4*(WIDTH/11)),  int(4*(WIDTH/11))),(int(4*(WIDTH/11)),  int(7*(WIDTH/11))),int(0.05*(WIDTH/11)))

    pygame.draw.line(gameDisplay, BLACK, (int(7*(WIDTH/11)),  int(4*(WIDTH/11))),(int(7*(WIDTH/11)),  int(7*(WIDTH/11))),int(0.05*(WIDTH/11)))
    pygame.draw.line(gameDisplay, BLACK, (int(7.5*(WIDTH/11)),int(4*(WIDTH/11))),(int(7.5*(WIDTH/11)),int(7*(WIDTH/11))),int(0.05*(WIDTH/11)))
    pygame.draw.line(gameDisplay, BLACK, (int(8*(WIDTH/11)),  int(4*(WIDTH/11))),(int(8*(WIDTH/11)),  int(7*(WIDTH/11))),int(0.05*(WIDTH/11)))
    pygame.draw.line(gameDisplay, BLACK, (int(8.5*(WIDTH/11)),int(4*(WIDTH/11))),(int(8.5*(WIDTH/11)),int(7*(WIDTH/11))),int(0.05*(WIDTH/11)))
    pygame.draw.line(gameDisplay, BLACK, (int(9*(WIDTH/11)),  int(4*(WIDTH/11))),(int(9*(WIDTH/11)),  int(7*(WIDTH/11))),int(0.05*(WIDTH/11)))
    pygame.draw.line(gameDisplay, BLACK, (int(9.5*(WIDTH/11)),int(4*(WIDTH/11))),(int(9.5*(WIDTH/11)),int(7*(WIDTH/11))),int(0.05*(WIDTH/11)))
    pygame.draw.line(gameDisplay, BLACK, (int(10*(WIDTH/11)), int(4*(WIDTH/11))),(int(10*(WIDTH/11)), int(7*(WIDTH/11))),int(0.05*(WIDTH/11)))
    pygame.draw.line(gameDisplay, BLACK, (int(10.5*(WIDTH/11)),int(4*(WIDTH/11))),(int(10.5*(WIDTH/11)),  int(7*(WIDTH/11))),int(0.05*(WIDTH/11)))

    pygame.draw.line(gameDisplay, BLACK, (4*(WIDTH/11),int(0.5*(WIDTH/11))),(7*(WIDTH/11),int(0.5*(WIDTH/11))),int(0.05*(WIDTH/11)))
    pygame.draw.line(gameDisplay, BLACK, (4*(WIDTH/11),int(1*(WIDTH/11))),  (7*(WIDTH/11),int(1*(WIDTH/11))),  int(0.05*(WIDTH/11)))
    pygame.draw.line(gameDisplay, BLACK, (4*(WIDTH/11),int(1.5*(WIDTH/11))),(7*(WIDTH/11),int(1.5*(WIDTH/11))),int(0.05*(WIDTH/11)))
    pygame.draw.line(gameDisplay, BLACK, (4*(WIDTH/11),int(2*(WIDTH/11))),  (7*(WIDTH/11),int(2*(WIDTH/11))),  int(0.05*(WIDTH/11)))
    pygame.draw.line(gameDisplay, BLACK, (4*(WIDTH/11),int(2.5*(WIDTH/11))),(7*(WIDTH/11),int(2.5*(WIDTH/11))),int(0.05*(WIDTH/11)))
    pygame.draw.line(gameDisplay, BLACK, (4*(WIDTH/11),int(3*(WIDTH/11))),  (7*(WIDTH/11),int(3*(WIDTH/11))),  int(0.05*(WIDTH/11)))
    pygame.draw.line(gameDisplay, BLACK, (4*(WIDTH/11),int(3.5*(WIDTH/11))),(7*(WIDTH/11),int(3.5*(WIDTH/11))),int(0.05*(WIDTH/11)))
    pygame.draw.line(gameDisplay, BLACK, (4*(WIDTH/11),int(4*(WIDTH/11))),  (7*(WIDTH/11),int(4*(WIDTH/11))),  int(0.05*(WIDTH/11)))

    pygame.draw.line(gameDisplay, BLACK, (4*(WIDTH/11),int(7*(WIDTH/11))),   (7*(WIDTH/11),int(7*(WIDTH/11))),   int(0.05*(WIDTH/11)))
    pygame.draw.line(gameDisplay, BLACK, (4*(WIDTH/11),int(7.5*(WIDTH/11))), (7*(WIDTH/11),int(7.5*(WIDTH/11))), int(0.05*(WIDTH/11)))
    pygame.draw.line(gameDisplay, BLACK, (4*(WIDTH/11),int(8*(WIDTH/11))),   (7*(WIDTH/11),int(8*(WIDTH/11))),   int(0.05*(WIDTH/11)))
    pygame.draw.line(gameDisplay, BLACK, (4*(WIDTH/11),int(8.5*(WIDTH/11))), (7*(WIDTH/11),int(8.5*(WIDTH/11))), int(0.05*(WIDTH/11)))
    pygame.draw.line(gameDisplay, BLACK, (4*(WIDTH/11),int(9*(WIDTH/11))),   (7*(WIDTH/11),int(9*(WIDTH/11))),   int(0.05*(WIDTH/11)))
    pygame.draw.line(gameDisplay, BLACK, (4*(WIDTH/11),int(9.5*(WIDTH/11))), (7*(WIDTH/11),int(9.5*(WIDTH/11))), int(0.05*(WIDTH/11)))
    pygame.draw.line(gameDisplay, BLACK, (4*(WIDTH/11),int(10*(WIDTH/11))),  (7*(WIDTH/11),int(10*(WIDTH/11))),  int(0.05*(WIDTH/11)))
    pygame.draw.line(gameDisplay, BLACK, (4*(WIDTH/11),int(10.5*(WIDTH/11))),(7*(WIDTH/11),int(10.5*(WIDTH/11))),int(0.05*(WIDTH/11)))

    pygame.draw.line(gameDisplay, BLACK, (0,5*(WIDTH/11)),(4*(WIDTH/11),5*(WIDTH/11)),int(0.05*(WIDTH/11)))
    pygame.draw.line(gameDisplay, BLACK, (0,6*(WIDTH/11)),(4*(WIDTH/11),6*(WIDTH/11)),int(0.05*(WIDTH/11)))

    pygame.draw.line(gameDisplay, BLACK, (5*(WIDTH/11),0),(5*(WIDTH/11),4*(WIDTH/11)),int(0.05*(WIDTH/11)))
    pygame.draw.line(gameDisplay, BLACK, (6*(WIDTH/11),0),(6*(WIDTH/11),4*(WIDTH/11)),int(0.05*(WIDTH/11)))

    pygame.draw.line(gameDisplay, BLACK, (7*(WIDTH/11),5*(WIDTH/11)),(11*(WIDTH/11),5*(WIDTH/11)),int(0.05*(WIDTH/11)))
    pygame.draw.line(gameDisplay, BLACK, (7*(WIDTH/11),6*(WIDTH/11)),(11*(WIDTH/11),6*(WIDTH/11)),int(0.05*(WIDTH/11)))

    pygame.draw.line(gameDisplay, BLACK, (5*(WIDTH/11),7*(WIDTH/11)),(5*(WIDTH/11),11*(WIDTH/11)),int(0.05*(WIDTH/11)))
    pygame.draw.line(gameDisplay, BLACK, (6*(WIDTH/11),7*(WIDTH/11)),(6*(WIDTH/11),11*(WIDTH/11)),int(0.05*(WIDTH/11)))

    pygame.draw.line(gameDisplay, BLACK, (4*(WIDTH/11),0),(4*(WIDTH/11),11*(WIDTH/11)),int(0.05*(WIDTH/11)))
    pygame.draw.line(gameDisplay, BLACK, (7*(WIDTH/11),0),(7*(WIDTH/11),11*(WIDTH/11)),int(0.05*(WIDTH/11)))
    pygame.draw.line(gameDisplay, BLACK, (0,4*(WIDTH/11)),(11*(WIDTH/11),4*(WIDTH/11)),int(0.05*(WIDTH/11)))
    pygame.draw.line(gameDisplay, BLACK, (0,7*(WIDTH/11)),(11*(WIDTH/11),7*(WIDTH/11)),int(0.05*(WIDTH/11)))

    pygame.draw.line(gameDisplay, BLACK, (4*(WIDTH/11),4*(WIDTH/11)),(7*(WIDTH/11),7*(WIDTH/11)),int(0.05*(WIDTH/11)))
    pygame.draw.line(gameDisplay, BLACK, (7*(WIDTH/11),4*(WIDTH/11)),(4*(WIDTH/11),7*(WIDTH/11)),int(0.05*(WIDTH/11)))
    

drawBoard()
pygame.display.flip()
while True:
    
    
    color1,color2,color3,color4=playerSpecify()
    initCoins(gameDisplay,WIDTH,color1,color2,color3,color4)
    pygame.display.flip()
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
    pygame.display.flip()
