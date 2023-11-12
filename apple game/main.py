import pygame
import sys
import random

pygame.init()
screen = pygame.display.set_mode((350, 600))
screen_rect = screen.get_rect()
clock = pygame.time.Clock()

class Apple:
    def __init__(self, image, position, speed):
        self.image = image
        self.rect = self.image.get_rect(topleft = position)
        self.speed = speed
    def move(self):
        self.rect.y += self.speed    

class Bottle:
    def __init__(self, image, position, speed):
        self.image = image
        self.rect = self.image.get_rect(topleft = position)
        self.speed = speed
    def move(self):
        self.rect.y += self.speed    

# vars
speed = 3
score = 0
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

# apple

apple_image = pygame.image.load('assets/apple.png').convert_alpha()
apple_image = pygame.transform.scale(apple_image, (TILESIZE, TILESIZE))


apples = [
Apple(apple_image, (100, 0), 3),
Apple(apple_image, (250, 0), 3),

]

# bottle

bottle_image = pygame.image.load('assets/illustration.png').convert_alpha()
bottle_image = pygame.transform.scale(bottle_image, (TILESIZE/2, TILESIZE))


bottles = [
Bottle(bottle_image, (50, 0), 3),
Bottle(bottle_image, (150, 0), 3),

]

font = pygame.font.Font('assets/PixeloidMono.ttf', TILESIZE//2)
pickup = pygame.mixer.Sound('assets/powerup.mp3')
pickup.set_volume(0.1)

running = True 

def update():
    global speed
    global score

    keys = pygame.key.get_pressed()

    if keys[pygame.K_LEFT]:
        player_rect.x -= 8
    if keys[pygame.K_RIGHT]:
        player_rect.x += 8

    player_rect.clamp_ip(screen_rect)    

    # apple dept
    for apple in apples:
        apple.move()
        if apple.rect.colliderect(floor_rect):
            apples.remove(apple)
            apples.append(Apple(apple_image, (random.randint(50, 300), -50), speed))
            speed += 0.1
        elif apple.rect.colliderect(player_rect):
            apples.remove(apple)
            apples.append(Apple(apple_image, (random.randint(50, 300), -50), speed))
            score += 1   
            pickup.play()  


    # bottle dept

    for bottle in bottles:
        bottle.move()
        if bottle.rect.colliderect(floor_rect):
            bottles.remove(bottle)   
            bottles.append(Bottle(bottle_image, (random.randint(50, 300), -50), speed))
            speed += 0.2
            # 50 to 300 is padding for the random positions
        elif bottle.rect.colliderect(player_rect):
            bottles.remove(bottle)
            bottles.append(Bottle(bottle_image, (random.randint(50, 300), -50), speed))  
            score += 2 
            pickup.play()


def draw():
    screen.fill('lightblue')
    screen.blit(player_image, player_rect)
    screen.blit(floor_image, floor_rect)

    for apple in apples:
        screen.blit(apple.image, apple.rect)   

    for bottle in bottles:
        screen.blit(bottle.image, bottle.rect)  

    score_text = font.render(f'Score: {score}', True, "white")    
    screen.blit(score_text, (5 , 5))  

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

