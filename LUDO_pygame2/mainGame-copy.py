import pygame, sys,random

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

FPS=30  #frames per second setting
fpsClock = pygame.time.Clock()

def rollDice():
    return random.choice([1,2,3,4,5,6])

def getBoard():
    gameDisplay = pygame.display.set_mode((1100,1100))
    pygame.display.set_caption('LUDO')
    gameDisplay.fill(WHITE)

    #Drawing LUDO board
    pygame.draw.polygon(gameDisplay, YELLOW, ((400,400), (700,400), (550,550)))
    pygame.draw.polygon(gameDisplay, GREEN, ((400,400), (400,700), (550,550)))
    pygame.draw.polygon(gameDisplay, RED, ((400,700), (700,700), (550,550)))
    pygame.draw.polygon(gameDisplay, BLUE, ((700,400), (700,700), (550,550)))

    pygame.draw.rect(gameDisplay, LIGHTYELLOW, (700,0,400,400))
    pygame.draw.rect(gameDisplay, LIGHTBLUE, (700,700,400,400))
    pygame.draw.rect(gameDisplay, LIGHTGREEN, (0,0,400,400))
    pygame.draw.rect(gameDisplay, PINK, (0,700,400,400))

    pygame.draw.rect(gameDisplay, YELLOW, (750,50,300,300))
    pygame.draw.rect(gameDisplay, BLUE, (750,750,300,300))
    pygame.draw.rect(gameDisplay, GREEN, (50,50,300,300))
    pygame.draw.rect(gameDisplay, RED, (50,750,300,300))

    pygame.draw.rect(gameDisplay, YELLOW, (500,0,100,400))
    pygame.draw.rect(gameDisplay, BLUE, (700,500,400,100))
    pygame.draw.rect(gameDisplay, GREEN, (0,500,400,100))
    pygame.draw.rect(gameDisplay, RED, (500,700,100,400))

    pygame.draw.rect(gameDisplay, YELLOW, (600,0,100,50))
    pygame.draw.rect(gameDisplay, BLUE, (1050,600,50,100))
    pygame.draw.rect(gameDisplay, GREEN, (0,400,50,100))
    pygame.draw.rect(gameDisplay, RED, (400,1050,100,50))

    pygame.draw.circle(gameDisplay, LIGHTYELLOW, (825,125),40)
    pygame.draw.circle(gameDisplay, LIGHTYELLOW, (975,125),40)
    pygame.draw.circle(gameDisplay, LIGHTYELLOW, (825,275),40)
    pygame.draw.circle(gameDisplay, LIGHTYELLOW, (975,275),40)

    pygame.draw.circle(gameDisplay, LIGHTGREEN, (125,125),40)
    pygame.draw.circle(gameDisplay, LIGHTGREEN, (275,125),40)
    pygame.draw.circle(gameDisplay, LIGHTGREEN, (125,275),40)
    pygame.draw.circle(gameDisplay, LIGHTGREEN, (275,275),40)

    pygame.draw.circle(gameDisplay, LIGHTBLUE, (825,825),40)
    pygame.draw.circle(gameDisplay, LIGHTBLUE, (975,975),40)
    pygame.draw.circle(gameDisplay, LIGHTBLUE, (825,975),40)
    pygame.draw.circle(gameDisplay, LIGHTBLUE, (975,825),40)

    pygame.draw.circle(gameDisplay, PINK, (125,825),40)
    pygame.draw.circle(gameDisplay, PINK, (125,975),40)
    pygame.draw.circle(gameDisplay, PINK, (275,825),40)
    pygame.draw.circle(gameDisplay, PINK, (275,975),40)

    pygame.draw.line(gameDisplay, BLACK, (50,400),(50,700),5)
    pygame.draw.line(gameDisplay, BLACK, (100,400),(100,700),5)
    pygame.draw.line(gameDisplay, BLACK, (150,400),(150,700),5)
    pygame.draw.line(gameDisplay, BLACK, (200,400),(200,700),5)
    pygame.draw.line(gameDisplay, BLACK, (250,400),(250,700),5)
    pygame.draw.line(gameDisplay, BLACK, (300,400),(300,700),5)
    pygame.draw.line(gameDisplay, BLACK, (350,400),(350,700),5)
    pygame.draw.line(gameDisplay, BLACK, (400,400),(400,700),5)

    pygame.draw.line(gameDisplay, BLACK, (700,400),(700,700),5)
    pygame.draw.line(gameDisplay, BLACK, (750,400),(750,700),5)
    pygame.draw.line(gameDisplay, BLACK, (800,400),(800,700),5)
    pygame.draw.line(gameDisplay, BLACK, (850,400),(850,700),5)
    pygame.draw.line(gameDisplay, BLACK, (900,400),(900,700),5)
    pygame.draw.line(gameDisplay, BLACK, (950,400),(950,700),5)
    pygame.draw.line(gameDisplay, BLACK, (1000,400),(1000,700),5)
    pygame.draw.line(gameDisplay, BLACK, (1050,400),(1050,700),5)

    pygame.draw.line(gameDisplay, BLACK, (400,50),(700,50),5)
    pygame.draw.line(gameDisplay, BLACK, (400,100),(700,100),5)
    pygame.draw.line(gameDisplay, BLACK, (400,150),(700,150),5)
    pygame.draw.line(gameDisplay, BLACK, (400,200),(700,200),5)
    pygame.draw.line(gameDisplay, BLACK, (400,250),(700,250),5)
    pygame.draw.line(gameDisplay, BLACK, (400,300),(700,300),5)
    pygame.draw.line(gameDisplay, BLACK, (400,350),(700,350),5)
    pygame.draw.line(gameDisplay, BLACK, (400,400),(700,400),5)

    pygame.draw.line(gameDisplay, BLACK, (400,700),(700,700),5)
    pygame.draw.line(gameDisplay, BLACK, (400,750),(700,750),5)
    pygame.draw.line(gameDisplay, BLACK, (400,800),(700,800),5)
    pygame.draw.line(gameDisplay, BLACK, (400,850),(700,850),5)
    pygame.draw.line(gameDisplay, BLACK, (400,900),(700,900),5)
    pygame.draw.line(gameDisplay, BLACK, (400,950),(700,950),5)
    pygame.draw.line(gameDisplay, BLACK, (400,1000),(700,1000),5)
    pygame.draw.line(gameDisplay, BLACK, (400,1050),(700,1050),5)

    pygame.draw.line(gameDisplay, BLACK, (0,500),(400,500),5)
    pygame.draw.line(gameDisplay, BLACK, (0,600),(400,600),5)

    pygame.draw.line(gameDisplay, BLACK, (500,0),(500,400),5)
    pygame.draw.line(gameDisplay, BLACK, (600,0),(600,400),5)

    pygame.draw.line(gameDisplay, BLACK, (700,500),(1100,500),5)
    pygame.draw.line(gameDisplay, BLACK, (700,600),(1100,600),5)

    pygame.draw.line(gameDisplay, BLACK, (500,700),(500,1100),5)
    pygame.draw.line(gameDisplay, BLACK, (600,700),(600,1100),5)

    pygame.draw.line(gameDisplay, BLACK, (400,0),(400,1100),5)
    pygame.draw.line(gameDisplay, BLACK, (700,0),(700,1100),5)
    pygame.draw.line(gameDisplay, BLACK, (0,400),(1100,400),5)
    pygame.draw.line(gameDisplay, BLACK, (0,700),(1100,700),5)

    pygame.draw.line(gameDisplay, BLACK, (400,400),(700,700),5)
    pygame.draw.line(gameDisplay, BLACK, (700,400),(400,700),5)
    return gameDisplay
gameDisplay = getBoard()
#initialising positions of rectangles in a list
# height of each rectangle=50
#length of each rectangle =100
pos=[(25,450),(75,450),(125,450),(175,450),(225,450),(275,450),(325,450),(375,450),(450,375),(450,325),(450,275),(450,225),(450,175),(450,125),(450,75),(450,25),(550,25),(650,25),(650,75),(650,125),(650,175),(650,225),(650,275),(650,325),(650,375),(725,450),(775,450),(825,450),(875,450),(925,450),(975,450),(1025,450),(1075,450),(1075,550),(1075,650),(1025,650),(975,650),(925,650),(875,650),(825,650),(775,650),(725,650),(650,725),(650,775),(650,825),(650,875),(650,925),(650,975),(650,1025),(650,1075),(550,1075),(450,1075),(450,1025),(450,975),(450,925),(450,875),(450,825),(450,775),(450,725),(375,650),(325,650),(275,650),(225,650),(175,650),(125,650),(75,650),(25,650),(25,550)]

i=0#to initialise position
coin=pygame.image.load('GreenCoin.png')#initialising the image

#function to move the coin
def moveCoin(event):
     global i
     if(event.type==pygame.KEYDOWN and event.key == pygame.K_SPACE):
         gameDisplay=getBoard()
         gameDisplay.blit(coin,pos[i%68])
         i+=rollDice()
         
while True:
    for event in pygame.event.get():
         moveCoin(event)
         if event.type == pygame.QUIT:
             pygame.quit()
             sys.exit()
    pygame.display.update()
    fpsClock.tick(FPS)
