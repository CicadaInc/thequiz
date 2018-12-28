import os

import pygame

pygame.init()

screen = pygame.display.set_mode((1000, 600))

directory = os.getcwd()

# LOAD BACKGROUND
background_surf = pygame.image.load(directory + '/levels/level.png')
background_surf = pygame.transform.scale(background_surf, (1000, 600))
background_rect = background_surf.get_rect(bottomright=(1000, 600))
screen.blit(background_surf, background_rect)

pygame.display.set_caption("Анимация персонажа")

directory = os.getcwd()

walkRight = [pygame.image.load(directory + "/sprites/RIGHT_1.png"),
             pygame.image.load(directory + "/sprites/RIGHT_2.png"),
             pygame.image.load(directory + "/sprites/RIGHT_3.png"),
             pygame.image.load(directory + "/sprites/RIGHT_4.png"),
             pygame.image.load(directory + "/sprites/RIGHT_5.png"),
             pygame.image.load(directory + "/sprites/RIGHT_6.png"),
             pygame.image.load(directory + "/sprites/RIGHT_7.png"),
             pygame.image.load(directory + "/sprites/RIGHT_8.png"),
             pygame.image.load(directory + "/sprites/RIGHT_9.png"),
             pygame.image.load(directory + "/sprites/RIGHT_10.png"),
             pygame.image.load(directory + "/sprites/RIGHT_11.png"),
             pygame.image.load(directory + "/sprites/RIGHT_12.png"),
             pygame.image.load(directory + "/sprites/RIGHT_13.png"),
             pygame.image.load(directory + "/sprites/RIGHT_14.png"),
             pygame.image.load(directory + "/sprites/RIGHT_15.png"),
             pygame.image.load(directory + "/sprites/RIGHT_16.png")]

walkLeft = [pygame.image.load(directory + "/sprites/LEFT_1.png"),
            pygame.image.load(directory + "/sprites/LEFT_2.png"),
            pygame.image.load(directory + "/sprites/LEFT_3.png"),
            pygame.image.load(directory + "/sprites/LEFT_4.png"),
            pygame.image.load(directory + "/sprites/LEFT_5.png"),
            pygame.image.load(directory + "/sprites/LEFT_6.png"),
            pygame.image.load(directory + "/sprites/LEFT_7.png"),
            pygame.image.load(directory + "/sprites/LEFT_8.png"),
            pygame.image.load(directory + "/sprites/LEFT_9.png"),
            pygame.image.load(directory + "/sprites/LEFT_10.png"),
            pygame.image.load(directory + "/sprites/LEFT_11.png"),
            pygame.image.load(directory + "/sprites/LEFT_12.png"),
            pygame.image.load(directory + "/sprites/LEFT_13.png"),
            pygame.image.load(directory + "/sprites/LEFT_14.png"),
            pygame.image.load(directory + "/sprites/LEFT_15.png"),
            pygame.image.load(directory + "/sprites/LEFT_16.png"),
            ]

walkUp = [pygame.image.load(directory + "/sprites/UP_1.png"),
          pygame.image.load(directory + "/sprites/UP_2.png"),
          pygame.image.load(directory + "/sprites/UP_3.png"),
          pygame.image.load(directory + "/sprites/UP_4.png"),
          pygame.image.load(directory + "/sprites/UP_5.png"),
          pygame.image.load(directory + "/sprites/UP_6.png"),
          pygame.image.load(directory + "/sprites/UP_7.png"),
          pygame.image.load(directory + "/sprites/UP_8.png"),
          pygame.image.load(directory + "/sprites/UP_9.png"),
          pygame.image.load(directory + "/sprites/UP_10.png"),
          pygame.image.load(directory + "/sprites/UP_11.png"),
          pygame.image.load(directory + "/sprites/UP_12.png"),
          pygame.image.load(directory + "/sprites/UP_13.png"),
          pygame.image.load(directory + "/sprites/UP_14.png"),
          pygame.image.load(directory + "/sprites/UP_15.png"),
          pygame.image.load(directory + "/sprites/UP_16.png"),
          ]

walkDown = [pygame.image.load(directory + "/sprites/DOWN_1.png"),
            pygame.image.load(directory + "/sprites/DOWN_2.png"),
            pygame.image.load(directory + "/sprites/DOWN_3.png"),
            pygame.image.load(directory + "/sprites/DOWN_4.png"),
            pygame.image.load(directory + "/sprites/DOWN_5.png"),
            pygame.image.load(directory + "/sprites/DOWN_6.png"),
            pygame.image.load(directory + "/sprites/DOWN_7.png"),
            pygame.image.load(directory + "/sprites/DOWN_8.png"),
            pygame.image.load(directory + "/sprites/DOWN_9.png"),
            pygame.image.load(directory + "/sprites/DOWN_10.png"),
            pygame.image.load(directory + "/sprites/DOWN_11.png"),
            pygame.image.load(directory + "/sprites/DOWN_12.png"),
            pygame.image.load(directory + "/sprites/DOWN_13.png"),
            pygame.image.load(directory + "/sprites/DOWN_14.png"),
            pygame.image.load(directory + "/sprites/DOWN_15.png"),
            pygame.image.load(directory + "/sprites/DOWN_16.png")
            ]

STAY = pygame.image.load(directory + "/sprites/STAY.png")

clock = pygame.time.Clock()

x = 112
y = 85
width = 15
height = 22

left = False
right = False
down = False
up = False

anim = 0

speed = 5


def draw():
    global anim

    background_surf = pygame.image.load(directory + '/levels/level.png')
    background_surf = pygame.transform.scale(background_surf, (1000, 600))
    background_rect = background_surf.get_rect(bottomright=(1000, 600))
    screen.blit(background_surf, background_rect)

    if anim + 1 >= 30:
        anim = 0
    if right:
        screen.blit(walkRight[anim // 4], (x, y))
        anim += 2
    elif left:
        screen.blit(walkLeft[anim // 4], (x, y))
        anim += 2
    elif up:
        screen.blit(walkUp[anim // 4], (x, y))
        anim += 2
    elif down:
        screen.blit(walkDown[anim // 4], (x, y))
        anim += 2
    else:
        screen.blit(STAY, (x, y))
        anim = 0

    pygame.display.update()


run = True

while run:
    clock.tick(30)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    keys = pygame.key.get_pressed()

    if keys[pygame.K_LEFT] and x > speed:
        x -= speed
        left = True
        right = False
        up = False
        down = False

    elif keys[pygame.K_RIGHT]:
        x += speed
        right = True
        left = False
        up = False
        down = False

    elif keys[pygame.K_UP]:
        y -= speed
        up = True
        down = False
        left = False
        right = False

    elif keys[pygame.K_DOWN]:
        y += speed
        down = True
        up = False
        left = False
        right = False

    else:
        right = False
        left = False
        up = False
        down = False
        anim = 0

    draw()
