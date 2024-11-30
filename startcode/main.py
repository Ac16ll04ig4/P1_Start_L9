import pygame, sys
from pygame.locals import QUIT
color = (0,0,0)
radius = (1)
pygame.init()
venster = pygame.display.set_mode((350, 350))
venster.fill((255,255,255))
while True:
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
        if pygame.mouse.get_pressed() == (True,False,False): #dit is de pen
            pygame.draw.circle(venster,color, pygame.mouse.get_pos(),radius)
        if pygame.mouse.get_pressed() == (False,False,True): #dit is de gom
            pygame.draw.circle(venster,(255,255,255), pygame.mouse.get_pos(),radius)
        if event.type == pygame.KEYDOWN: # kleur = roze
            if event.key == pygame.K_r:
                color = (255,192,203)
            if event.key == pygame.K_s: # tekening opslaan
                pygame.image.save(venster, "tekening" + ".jpg")
        if event.type == pygame.KEYUP : # dikker maken
            if event.key == pygame.K_UP:
                radius += 100
        if event.type == pygame.KEYDOWN : # dunner maken
            if event.key == pygame.K_DOWN :
                radius += -1


    pygame.display.update()

