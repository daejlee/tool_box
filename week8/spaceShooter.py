import pygame, sys
from pygame.locals import *

pygame.init()

width = 700
height = 500
screen = pygame.display.set_mode((width, height))

# 배경
bgImage = pygame.image.load("./background.jpg")
bgImage = pygame.transform.scale(bgImage, (width, height))
backX = 0
backX2 = width

# 주인공
img = pygame.image.load("./spaceship.png")
spaceship = {
    "rect": pygame.Rect(0, 215, 70, 70),
    "image": pygame.transform.scale(img, (70, 70)),
}

while True:
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()

    # 키보드 이벤트
    keyInput = pygame.key.get_pressed()
    if keyInput[K_LEFT]:
        backX += 3
        backX2 += 3
    elif keyInput[K_RIGHT]:
        backX -= 3
        backX2 -= 3

    # 배경 움직임
    """
    backX -= 1
    backX2 -= 1
    """

    if backX < -width:
        backX = width
    if backX2 < -width:
        backX2 = width

    if backX > 0:
        backX -= width
        backX2 -= width

    screen.blit(bgImage, (backX, 0))
    screen.blit(bgImage, (backX2, 0))
    screen.blit(spaceship["image"], spaceship["rect"])
    pygame.display.update()
