import pygame

pygame.init()

screen = pygame.display.set_mode((800,600))

##============================== 색상 코드 ==============================##
BLUE=(0,0,255)
WHITE=(255,255,255)
RED=(255,0,0)
SKYBLUE=(136,221,221)
BLACK=(0,0,0)
##============================== 색상 코드 ==============================##


running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    screen.fill(SKYBLUE)

    pygame.draw.circle(screen,WHITE,[400,200],80) #좌표, 지름
    pygame.draw.circle(screen,WHITE,[400,350],100) #좌표, 지름
    pygame.draw.rect(screen, RED, [340,249,130,30], 50)

    pygame.draw.circle(screen, BLACK, [362, 180],5)
    pygame.draw.circle(screen, BLACK, [432, 180],5)

    pygame.draw.circle(screen, BLACK, [400, 200],5)


    x,y= pygame.mouse.get_pos()

    print(f"{x} {y}")
    pygame.display.flip()


pygame.quit()
