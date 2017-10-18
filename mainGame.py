mport pygame, sys

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
x = 40       #Modify x in order to readjust your screen surface! 
WIDTH = 11*x
HEIGHT = 11*x
gameDisplay = pygame.display.set_mode((WIDTH,HEIGHT))
pygame.display.set_caption('LUDO')
gameDisplay.fill(WHITE)

#Drawing LUDO board
pygame.draw.polygon(gameDisplay, YELLOW, ((4*x,4*x), (7*x,4*x), (5.5*x,5.5*x)))
pygame.draw.polygon(gameDisplay, GREEN, ((4*x,4*x), (4*x,7*x), (5.5*x,5.5*x)))
pygame.draw.polygon(gameDisplay, RED, ((4*x,7*x), (7*x,7*x), (5.5*x,5.5*x)))
pygame.draw.polygon(gameDisplay, BLUE, ((7*x,4*x), (7*x,7*x), (5.5*x,5.5*x)))

pygame.draw.rect(gameDisplay, LIGHTYELLOW, (7*x,0,4*x,4*x))
pygame.draw.rect(gameDisplay, LIGHTBLUE, (7*x,7*x,4*x,4*x))
pygame.draw.rect(gameDisplay, LIGHTGREEN, (0,0,4*x,4*x))
pygame.draw.rect(gameDisplay, PINK, (0,7*x,4*x,4*x))

pygame.draw.rect(gameDisplay, YELLOW, (7.5*x,0.5*x,3*x,3*x))
pygame.draw.rect(gameDisplay, BLUE, (7.5*x,7.5*x,3*x,3*x))
pygame.draw.rect(gameDisplay, GREEN, (0.5*x,0.5*x,3*x,3*x))
pygame.draw.rect(gameDisplay, RED, (0.5*x,7.5*x,3*x,3*x))

pygame.draw.rect(gameDisplay, YELLOW, (5*x,0,1*x,4*x))
pygame.draw.rect(gameDisplay, BLUE, (7*x,5*x,4*x,1*x))
pygame.draw.rect(gameDisplay, GREEN, (0,5*x,4*x,1*x))
pygame.draw.rect(gameDisplay, RED, (5*x,7*x,1*x,4*x))

pygame.draw.rect(gameDisplay, YELLOW, (6*x,0,1*x,0.5*x))
pygame.draw.rect(gameDisplay, BLUE, (10.5*x,6*x,0.5*x,1*x))
pygame.draw.rect(gameDisplay, GREEN, (0,4*x,0.5*x,1*x))
pygame.draw.rect(gameDisplay, RED, (4*x,10.5*x,1*x,0.5*x))

pygame.draw.circle(gameDisplay, LIGHTYELLOW, (int(8.25*x),int(1.25*x)),int(0.4*x))
pygame.draw.circle(gameDisplay, LIGHTYELLOW, (int(9.75*x),int(1.25*x)),int(0.4*x))
pygame.draw.circle(gameDisplay, LIGHTYELLOW, (int(8.25*x),int(2.75*x)),int(0.4*x))
pygame.draw.circle(gameDisplay, LIGHTYELLOW, (int(9.75*x),int(2.75*x)),int(0.4*x))

pygame.draw.circle(gameDisplay, LIGHTGREEN, (int(1.25*x),int(1.25*x)),int(0.4*x))
pygame.draw.circle(gameDisplay, LIGHTGREEN, (int(2.75*x),int(1.25*x)),int(0.4*x))
pygame.draw.circle(gameDisplay, LIGHTGREEN, (int(1.25*x),int(2.75*x)),int(0.4*x))
pygame.draw.circle(gameDisplay, LIGHTGREEN, (int(2.75*x),int(2.75*x)),int(0.4*x))

pygame.draw.circle(gameDisplay, LIGHTBLUE, (int(8.25*x),int(8.25*x)),int(0.4*x))
pygame.draw.circle(gameDisplay, LIGHTBLUE, (int(9.75*x),int(9.75*x)),int(0.4*x))
pygame.draw.circle(gameDisplay, LIGHTBLUE, (int(8.25*x),int(9.75*x)),int(0.4*x))
pygame.draw.circle(gameDisplay, LIGHTBLUE, (int(9.75*x),int(8.25*x)),int(0.4*x))

pygame.draw.circle(gameDisplay, PINK, (int(1.25*x),int(8.25*x)),int(0.4*x))
pygame.draw.circle(gameDisplay, PINK, (int(1.25*x),int(9.75*x)),int(0.4*x))
pygame.draw.circle(gameDisplay, PINK, (int(2.75*x),int(8.25*x)),int(0.4*x))
pygame.draw.circle(gameDisplay, PINK, (int(2.75*x),int(9.75*x)),int(0.4*x))

pygame.draw.line(gameDisplay, BLACK, (int(0.5*x),int(4*x)),(int(0.5*x),int(7*x)),int(0.05*x))
pygame.draw.line(gameDisplay, BLACK, (int(1*x),  int(4*x)),(int(1*x),  int(7*x)),int(0.05*x))
pygame.draw.line(gameDisplay, BLACK, (int(1.5*x),int(4*x)),(int(1.5*x),int(7*x)),int(0.05*x))
pygame.draw.line(gameDisplay, BLACK, (int(2*x),  int(4*x)),(int(2*x),  int(7*x)),int(0.05*x))
pygame.draw.line(gameDisplay, BLACK, (int(2.5*x),int(4*x)),(int(2.5*x),int(7*x)),int(0.05*x))
pygame.draw.line(gameDisplay, BLACK, (int(3*x),  int(4*x)),(int(3*x),  int(7*x)),int(0.05*x))
pygame.draw.line(gameDisplay, BLACK, (int(3.5*x),int(4*x)),(int(3.5*x),int(7*x)),int(0.05*x))
pygame.draw.line(gameDisplay, BLACK, (int(4*x),  int(4*x)),(int(4*x),  int(7*x)),int(0.05*x))

pygame.draw.line(gameDisplay, BLACK, (int(7*x),  int(4*x)),(int(7*x),  int(7*x)),int(0.05*x))
pygame.draw.line(gameDisplay, BLACK, (int(7.5*x),int(4*x)),(int(7.5*x),int(7*x)),int(0.05*x))
pygame.draw.line(gameDisplay, BLACK, (int(8*x),  int(4*x)),(int(8*x),  int(7*x)),int(0.05*x))
pygame.draw.line(gameDisplay, BLACK, (int(8.5*x),int(4*x)),(int(8.5*x),int(7*x)),int(0.05*x))
pygame.draw.line(gameDisplay, BLACK, (int(9*x),  int(4*x)),(int(9*x),  int(7*x)),int(0.05*x))
pygame.draw.line(gameDisplay, BLACK, (int(9.5*x),int(4*x)),(int(9.5*x),int(7*x)),int(0.05*x))
pygame.draw.line(gameDisplay, BLACK, (int(10*x), int(4*x)),(int(10*x), int(7*x)),int(0.05*x))
pygame.draw.line(gameDisplay, BLACK, (int(10.5*x),int(4*x)),(int(10.5*x),  int(7*x)),int(0.05*x))

pygame.draw.line(gameDisplay, BLACK, (4*x,int(0.5*x)),(7*x,int(0.5*x)),int(0.05*x))
pygame.draw.line(gameDisplay, BLACK, (4*x,int(1*x)),  (7*x,int(1*x)),  int(0.05*x))
pygame.draw.line(gameDisplay, BLACK, (4*x,int(1.5*x)),(7*x,int(1.5*x)),int(0.05*x))
pygame.draw.line(gameDisplay, BLACK, (4*x,int(2*x)),  (7*x,int(2*x)),  int(0.05*x))
pygame.draw.line(gameDisplay, BLACK, (4*x,int(2.5*x)),(7*x,int(2.5*x)),int(0.05*x))
pygame.draw.line(gameDisplay, BLACK, (4*x,int(3*x)),  (7*x,int(3*x)),  int(0.05*x))
pygame.draw.line(gameDisplay, BLACK, (4*x,int(3.5*x)),(7*x,int(3.5*x)),int(0.05*x))
pygame.draw.line(gameDisplay, BLACK, (4*x,int(4*x)),  (7*x,int(4*x)),  int(0.05*x))

pygame.draw.line(gameDisplay, BLACK, (4*x,int(7*x)),   (7*x,int(7*x)),   int(0.05*x))
pygame.draw.line(gameDisplay, BLACK, (4*x,int(7.5*x)), (7*x,int(7.5*x)), int(0.05*x))
pygame.draw.line(gameDisplay, BLACK, (4*x,int(8*x)),   (7*x,int(8*x)),   int(0.05*x))
pygame.draw.line(gameDisplay, BLACK, (4*x,int(8.5*x)), (7*x,int(8.5*x)), int(0.05*x))
pygame.draw.line(gameDisplay, BLACK, (4*x,int(9*x)),   (7*x,int(9*x)),   int(0.05*x))
pygame.draw.line(gameDisplay, BLACK, (4*x,int(9.5*x)), (7*x,int(9.5*x)), int(0.05*x))
pygame.draw.line(gameDisplay, BLACK, (4*x,int(10*x)),  (7*x,int(10*x)),  int(0.05*x))
pygame.draw.line(gameDisplay, BLACK, (4*x,int(10.5*x)),(7*x,int(10.5*x)),int(0.05*x))

pygame.draw.line(gameDisplay, BLACK, (0,5*x),(4*x,5*x),int(0.05*x))
pygame.draw.line(gameDisplay, BLACK, (0,6*x),(4*x,6*x),int(0.05*x))

pygame.draw.line(gameDisplay, BLACK, (5*x,0),(5*x,4*x),int(0.05*x))
pygame.draw.line(gameDisplay, BLACK, (6*x,0),(6*x,4*x),int(0.05*x))

pygame.draw.line(gameDisplay, BLACK, (7*x,5*x),(11*x,5*x),int(0.05*x))
pygame.draw.line(gameDisplay, BLACK, (7*x,6*x),(11*x,6*x),int(0.05*x))

pygame.draw.line(gameDisplay, BLACK, (5*x,7*x),(5*x,11*x),int(0.05*x))
pygame.draw.line(gameDisplay, BLACK, (6*x,7*x),(6*x,11*x),int(0.05*x))

pygame.draw.line(gameDisplay, BLACK, (4*x,0),(4*x,11*x),int(0.05*x))
pygame.draw.line(gameDisplay, BLACK, (7*x,0),(7*x,11*x),int(0.05*x))
pygame.draw.line(gameDisplay, BLACK, (0,4*x),(11*x,4*x),int(0.05*x))
pygame.draw.line(gameDisplay, BLACK, (0,7*x),(11*x,7*x),int(0.05*x))

pygame.draw.line(gameDisplay, BLACK, (4*x,4*x),(7*x,7*x),int(0.05*x))
pygame.draw.line(gameDisplay, BLACK, (7*x,4*x),(4*x,7*x),int(0.05*x))




while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
    pygame.display.flip()
