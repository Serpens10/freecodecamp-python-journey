import pygame
import sys

pygame.init()
screen = pygame.display.set_mode((350, 600))
screen_rect = screen.get_rect()
clock = pygame.time.Clock()

# constants
TILESIZE = 32

# floor
floor_image = pygame.image.load('assets/floor.png').convert_alpha()
floor_image = pygame.transform.scale(floor_image, (TILESIZE*15, TILESIZE*5))
floor_rect = floor_image.get_rect(bottomleft = (0, screen.get_height()))

# player
player_image = pygame.image.load('assets/player_static.png').convert_alpha()
player_image = pygame.transform.scale(player_image, (TILESIZE, TILESIZE*2))
player_rect = player_image.get_rect(center = (screen.get_width()/2,
                                    screen.get_height()-floor_image.get_height()-player_image.get_height()/2))

def update():
    keys = pygame.key.get_pressed()

    if keys[pygame.K_LEFT]:
        player_rect.x -= 8
    if keys[pygame.K_RIGHT]:
        player_rect.x += 8

    player_rect.clamp_ip(screen_rect)    

running = True 

def draw():
    screen.fill('lightblue')
    screen.blit(player_image, player_rect)
    screen.blit(floor_image, floor_rect)

# game loop to keep screen open, create boolean variable

while running :
    for event in pygame.event.get() :
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    update()
    draw()
    clock.tick(60)        
    pygame.display.update()

