print("Robolab Python Pro Course / Shooter template project =) ")


# link for presentation => https://docs.google.com/presentation/d/1UkxfjWFpecW7BD-9ngFL7hs1fSykJnfQynp53x15_i8/edit#slide=id.g122dbdc220d_1_85


# modules import 
import pygame
import random
from os import path
#colors and window size set up
WHITE = (255,255,255)
BLACK = (0,0,0)
WIDTH = 480
HEIGHT = 600
FPS = 15 
# Window creating
pygame.init()
pygame.mixer.init()
window_size = (WIDTH,HEIGHT)
screen = pygame.display.set_mode(window_size)
pygame.display.set_caption("Shooter 2nd lesson")
clock = pygame.time.Clock() 
# Game sprites 
img_dir = path.join(path.dirname(__file__),"img")
background = pygame.image.load(path.join(img_dir,"field.png")).convert()
background_rect = background.get_rect() 
player_img = pygame.image.load(path.join(img_dir,"ship.png")).convert()
npc_img = pygame.image.load(path.join(img_dir,"npc.png")).convert()
bullet_img = pygame.image.load(path.join(img_dir,"bullet.png")).convert()

#player class
class Player(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        player_size = (50,50)
        self.image = pygame.transform.scale(player_img,player_size)
        self.image.set_colorkey(WHITE)
        self.rect = self.image.get_rect()
        self.rect.centerx = WIDTH /2
        self.rect.bottom = HEIGHT - 50
        self.speedx = 0

    def update(self):
        self.speedx = 0
        keysate = pygame.key.get_pressed()
        if keysate[pygame.K_LEFT]:
            self.speedx = -8 
        if keysate[pygame.K_RIGHT]:
            self.speedx = 8   
        self.rect.x += self.speedx
        if self.rect.right > WIDTH:
            self.rect.right = WIDTH
        if self.rect.left < 0:
            self.rect.left = 0

class Mob(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image + pygame.transform.scale(npc_img, (50, 50))
        self.image.set_colorkey(WHITE)
        self.rect = self.image.get_rect()
        self.rect.x = random.randrange(WIDTH - self.rect.width)
        self.rect.y = random.randrange(-300, -30)
        self.speefy = random.randrange(1, 8)
        self.speedx = random.randrange(-3, 3)

    def update(self):
        self.rect.x += self.speedx
        self.rect.y += self.speedy
        if self.rect.top > HIEGHT + 10 or self.rect.left < -25 or self.rect.right > WIDTH + 20:
            self.rect.x = random.randrange(WIDTH - self.rect.width)
            self.rect.y = random.randrange(-100, -40)
            self.speedy = random.randrange(1, 8)

    #game entities innitiation
    all_sprites = pygame.sprite.Group()
    mobs = pygame.sprite.Group()
    bullets = pygame.sprite.Group()
    player = Player()
    all_sprites.add(player)

    for i in range(2):
        m = Mob()
        all_sprites.add(m)
        mobs.add(m)

    #Game life cycle
    running = True
    while running:
        #fps
        clock.tick(FPS)
        #event handler
        for event in pygame.event.get():
            #event for close
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE: #shoot
                    print("Shoot")

    #render update
    all_sprites.update()
    screen.fill(BLACK)
    screen.blit(background, background_rect)
    all_sprites.draw(Screen)
    #scrennflip
    pygame.display.flip()

pygame.quit()

    
    #shoot mechanic function


#mob generation system ~ mob (NPC) class

#mob generation system ~ generation

#Game lifecycle
    #fps

    #event handler

        #event to close window

        #shoot [if event.type == pygame.KEYDOWN] [if event.key == pygame.K_SPACE]

    #update of render

    #screen flip


 


 






 

 