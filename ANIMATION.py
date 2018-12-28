import pygame

pygame.init()

screen = pygame.display.set_mode((1000, 600))

pygame.display.set_caption("Анимация персонажа")

walkRight = [pygame.image.load("D:/PycharmProjects/thequiz/sprites/alien/run/run_0.png"),
             pygame.image.load("D:/PycharmProjects/thequiz/sprites/alien/run/run_1.png"),
             pygame.image.load("D:/PycharmProjects/thequiz/sprites/alien/run/run_2.png"),
             pygame.image.load("D:/PycharmProjects/thequiz/sprites/alien/run/run_3.png"),
             pygame.image.load("D:/PycharmProjects/thequiz/sprites/alien/run/run_4.png"),
             pygame.image.load("D:/PycharmProjects/thequiz/sprites/alien/run/run_5.png")]

clock = pygame.time.Clock()

x = 100
y = 400
width = 150
height = 150

left = False
right = False

# derectory = os.getcwd()

anim = 0

speed = 5


def draw():
    global anim

    screen.fill((0, 0, 0))

    if anim + 1 >= 30:
        anim = 0
    if right:
        screen.blit(walkRight[anim // 5], (x, y))
        anim += 1
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

    elif keys[pygame.K_RIGHT]:
        x += speed
        right = True
        left = False

    elif keys[pygame.K_UP]:
        y -= speed
    elif keys[pygame.K_DOWN]:
        y += speed
    else:
        right = False
        left = False
        anim = 0
    draw()
