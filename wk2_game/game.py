import pygame 

pygame.init()

WIDTH = 800
HEIGHT = 600

screen = pygame.display.set_mode((WIDTH, HEIGHT))

clock = pygame.time.Clock()

class Player(pygame.sprite.Sprite):

    def __init__(self):
        super().__init__()
        self.image = pygame.image.load("./pikimin.png").convert_alpha()
        self.image = pygame.transform.scale(self.image, (110,140))

        self.rect = self.image.get_rect()
        self.rect.center = (WIDTH/2, HEIGHT/2)

        self.speed = 5 

    def update(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT]:
            self.rect.x -= self.speed
        if keys[pygame.K_RIGHT]:
            self.rect.x += self.speed
        if keys[pygame.K_UP]:
            self.rect.y -= self.speed
        if keys[pygame.K_DOWN]:
            self.rect.y += self.speed

        if self.rect.left < 0:
            self.rect.left = 0 
        if self.rect.right > WIDTH:
            self.rect.right = WIDTH 
        if self.rect.top < 0:
            self.rect.top = 0 
        if self.rect.bottom > HEIGHT:
            self.rect.bottom = HEIGHT 


player = Player()
all_sprites = pygame.sprite.Group()
all_sprites.add(player)

running = True 

while running:
    for evnet in pygame.event.get():
        if evnet.type == pygame.QUIT:
            running = False 

    all_sprites.update()

    all_sprites.draw(screen)
    pygame.display.flip()
    clock.tick(60)

pygame.quit()