import pygame
import sys

pygame.init()
screen = pygame.display.set_mode((350, 600))
clock = pygame.time.Clock()

# constants
TILESIZE = 32

# player
player_image = pygame.image.load('assets/player_static.png').convert_alpha()
player_image = pygame.transform.scale(player_image, (TILESIZE, TILESIZE*2))

running = True 

def draw():
    screen.fill('lightblue')
    screen.blit(player_image, (175,300))

# game loop to keep screen open, create boolean variable

while running :
    for event in pygame.event.get() :
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    draw()
    clock.tick(60)        
    pygame.display.update()

