import pygame, sys

pygame.init()

resolution = (800,800)

white = (255,255,255)

game_display = pygame.display.set_mode(resolution)

pygame.display.set_caption('My first window')

game_display.fill(white)

pygame.display.flip()

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
