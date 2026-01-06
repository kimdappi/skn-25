import pygame

pygame.init()

screen = pygame.display.set_mode((800, 600))
pygame.display.set_caption("이동!!!")
##============================== 색상 코드 ==============================##

RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLACK = (0, 0,0 )
BLUE = (0, 0, 255)
WHITE = (255, 255, 255)
SKY = (100, 150, 200)
##============================== 색상 코드 ==============================##

clock = pygame.time.Clock()
##============================== 오브제 ============================== ##

cat = pygame.image.load("./cat.png").convert_alpha()
cat = pygame.transform.scale(cat, (200,200))

back_img = pygame.image.load("./background.png").convert_alpha()
back_img = pygame.transform.scale(back_img, (800,600))
##============================== 오브제  ==============================##

## 초기 좌표값
rect_x = 0
rect_y = 250

running = True

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    # rect_x += 1

    keys = pygame.key.get_pressed()
    # print(keys)

    if keys[pygame.K_LEFT]:
        rect_x -= 1

    if keys[pygame.K_UP]:
        rect_y -= 1

    if keys[pygame.K_DOWN]:
        rect_y += 1

    if keys[pygame.K_LEFT] and keys[pygame.K_DOWN]:
        rect_x -= 1
        rect_y += 1

    if keys[pygame.K_RIGHT]:
        rect_x += 1

    if rect_x > 800:
        rect_x = 0

    if rect_y > 600:
        rect_y = 0
   
    screen.fill((255,255,255))

    screen.blit(back_img,(0,0))
    screen.blit(cat, (rect_x, rect_y))
    pygame.display.flip()
    clock.tick(240)

pygame.quit()