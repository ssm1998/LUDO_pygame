import pygame, sys, LUDOfunctions

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

# initialising coin images
greenCoin=pygame.image.load('greencoin.png')
yellowCoin=pygame.image.load('yellowcoin.png')
redCoin=pygame.image.load('redcoin.png')
blueCoin=pygame.image.load('bluecoin.png')

#Setting up the surface
gameDisplay = pygame.display.set_mode((WIDTH,HEIGHT))
pygame.display.set_caption('LUDO')
gameDisplay.fill(WHITE)

pos = LUDOfunctions.genPos()
print pos

while True:
    LUDOfunctions.drawBoard()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
    pygame.display.flip()
