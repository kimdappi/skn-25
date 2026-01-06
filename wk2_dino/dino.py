import pygame
import random

screen_width = 800
screen_height = 400

# 색상 정의
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
GREEN = (83, 165, 81) # 공룡 색상
GRAY = (83, 83, 83)   # 장애물 색상

# 게임 설정 변수
GRAVITY = 0.8
JUMP_STRENGTH = -16
GAME_SPEED = 7

class Dino(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        # 공룡 크기 40x60
        self.image = pygame.image.load("./src/dino.png").convert_alpha()
        self.image = pygame.transform.scale(self.image, (90,60))
        self.rect = self.image.get_rect()
        self.rect.x = 50
        self.rect.y = 300 # 바닥 위치
        
        self.vel_y = 0
        self.is_jumping = False

    def jump(self):
        # 바닥에 있을 때만 점프 가능
        if not self.is_jumping:
            self.vel_y = JUMP_STRENGTH
            self.is_jumping = True

    def update(self):
        # 중력 적용
        self.vel_y += GRAVITY
        self.rect.y += self.vel_y

        # 바닥 충돌 처리
        if self.rect.bottom >= 350:
            self.rect.bottom = 350
            self.is_jumping = False
            self.vel_y = 0

class Cactus(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        # 선인장 크기 랜덤 (너비 30 높이 40~70)
        height = random.randint(40, 70)
        self.image = pygame.image.load("./src/cactus.png").convert_alpha()
        self.image = pygame.transform.scale(self.image, (50,50))
        self.rect = self.image.get_rect()
        self.rect.x = screen_width + random.randint(0, 100)
        self.rect.bottom = 350 # 땅 위에 위치

    def update(self):
        # 왼쪽으로 이동
        self.rect.x -= GAME_SPEED
        # 화면 밖으로 나가면 삭제
        if self.rect.right < 0:
            self.kill()