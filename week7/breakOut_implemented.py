import pygame, sys
from pygame.locals import *

pygame.init()

width = 800
height = 500

screen = pygame.display.set_mode((width, height))
r1 = pygame.Rect(0, 420, 80, 80)

# 목표물
rectList = []

x = 25
y = 10

for i in range(8):
    rect = pygame.Rect(x, y, 50, 50)
    rectList.append(rect)
    x += 100

# 총알
bullets = []

while True:
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
        if event.type == KEYDOWN and event.key == K_SPACE:
            bullet = pygame.Rect(r1.centerx - 5, r1.centery - 10, 10, 20)
            bullets.append(bullet)

    # r1 움직임 (좌우)
    keyInput = pygame.key.get_pressed()

    if keyInput[K_LEFT] and r1.left >= 0:
        r1.left -= 1
    elif keyInput[K_RIGHT] and r1.right <= width:
        r1.right += 1

    # 총알과 목표물의 충돌
    for bullet in bullets:
        for rect in rectList:
            if bullet.colliderect(rect):
                bullets.remove(bullet)
                rectList.remove(rect)

    screen.fill((255, 255, 255))
    pygame.draw.rect(screen, (0, 0, 255), r1)

    for r in rectList:
        pygame.draw.rect(screen, (0, 0, 0), r)

    for bullet in bullets:
        bullet.y -= 5
        pygame.draw.rect(screen, (255, 0, 0), bullet)

    pygame.display.update()
