import pygame 
import random
import time

pygame.init()

WIDTH = 800
HEIGHT = 600
##============================== 색상 코드 & 폰트 ==============================##

RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLACK = (0, 0,0 )
BLUE = (0, 0, 255)
WHITE = (255, 255, 255)
SKY = (100, 150, 200)
# ✅ 먼저 화면 설정(비디오 모드)
screen = pygame.display.set_mode((WIDTH, HEIGHT))
clock = pygame.time.Clock()

# ✅ 그 다음에 convert_alpha() 사용 가능
back_img = pygame.image.load("./src/background.jpg").convert_alpha()
back_img = pygame.transform.scale(back_img, (WIDTH, HEIGHT))


##============================== 색상 코드 & 폰트 ==============================##



class Player(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load("./src/cat.png").convert_alpha()
        self.image = pygame.transform.scale(self.image, (90,110))

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

class enemy(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load("./src/pikimin.png").convert_alpha()
        self.image = pygame.transform.scale(self.image, (40,40))

        self.rect=self.image.get_rect()

        self.rect.x =random.randrange(0, WIDTH-30)
        self.rect.y =random.randrange(-100,-40)
        self.speed = random.randrange(3,6)

    def update(self):
        self.rect.y += self.speed

        if self.rect.top > HEIGHT:
            self.rect.x = random.randrange(0, WIDTH- 30)
            self.rect.y = random.randrange(-100, -40)


##============================== 추가: UI/룰 ==============================##

def draw_lives(surface, lives, x=20, y=20):
    r = 10
    gap = 15
    for i in range(3):
        cx = x + i * (r * 2 + gap) + r
        cy = y + r
        if i < lives:
            pygame.draw.circle(surface, RED, (cx, cy), r)
        else:
            pygame.draw.circle(surface, WHITE, (cx, cy), r, 2)

##============================== 구현 ==============================##
player = Player()
all_sprites = pygame.sprite.Group()
all_sprites.add(player)

enemy_grp = pygame.sprite.Group()
for _ in range(10):
    m = enemy()

    m.base_speed = m.speed

    all_sprites.add(m)
    enemy_grp.add(m)

lives = 3
invincible_until = 0  # ms 기준
speed_bonus = 0       # 30초마다 +1 같은 보너스
last_speedup = pygame.time.get_ticks()
SPEEDUP_INTERVAL_MS = 30_000   # 30초
SPEEDUP_AMOUNT = 1            #  올리는 값

running = True 

while running:
    for evnet in pygame.event.get():
        if evnet.type == pygame.QUIT:
            running = False 

    # 30초마다 적 속도 증가 (일정하게)
    now = pygame.time.get_ticks()
    if now - last_speedup >= SPEEDUP_INTERVAL_MS:
        last_speedup = now
        speed_bonus += SPEEDUP_AMOUNT

    for e in enemy_grp:
        e.speed = e.base_speed + speed_bonus

    all_sprites.update()

    if now >= invincible_until:
        hits = pygame.sprite.spritecollide(player, enemy_grp, False)
        if hits:
            lives -= 1

            # 목숨 다 쓰면 종료
            if lives <= 0:
                running = False
            else:
                player.rect.center = (WIDTH/2, HEIGHT/2)
                invincible_until = now + 1000 

    screen.blit(back_img, (0,0))


    all_sprites.draw(screen)

    # 상단에 목숨 게이지 표시
    draw_lives(screen, lives, x=20, y=20)

    pygame.display.flip()
    clock.tick(60)

pygame.quit()