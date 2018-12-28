import os
import pygame


class Multiplayer():
    def __init__(self):
        pygame.init()

        self.screen = pygame.display.set_mode((1000, 600))

        self.directory = os.getcwd()

        pygame.display.set_caption("Анимация персонажа")

        self.walkRight = [pygame.image.load(self.directory + "/sprites/RIGHT_1.png"),
                          pygame.image.load(self.directory + "/sprites/RIGHT_2.png"),
                          pygame.image.load(self.directory + "/sprites/RIGHT_3.png"),
                          pygame.image.load(self.directory + "/sprites/RIGHT_4.png"),
                          pygame.image.load(self.directory + "/sprites/RIGHT_5.png"),
                          pygame.image.load(self.directory + "/sprites/RIGHT_6.png"),
                          pygame.image.load(self.directory + "/sprites/RIGHT_7.png"),
                          pygame.image.load(self.directory + "/sprites/RIGHT_8.png"),
                          pygame.image.load(self.directory + "/sprites/RIGHT_9.png"),
                          pygame.image.load(self.directory + "/sprites/RIGHT_10.png"),
                          pygame.image.load(self.directory + "/sprites/RIGHT_11.png"),
                          pygame.image.load(self.directory + "/sprites/RIGHT_12.png"),
                          pygame.image.load(self.directory + "/sprites/RIGHT_13.png"),
                          pygame.image.load(self.directory + "/sprites/RIGHT_14.png"),
                          pygame.image.load(self.directory + "/sprites/RIGHT_15.png"),
                          pygame.image.load(self.directory + "/sprites/RIGHT_16.png")]

        self.walkLeft = [pygame.image.load(self.directory + "/sprites/LEFT_1.png"),
                         pygame.image.load(self.directory + "/sprites/LEFT_2.png"),
                         pygame.image.load(self.directory + "/sprites/LEFT_3.png"),
                         pygame.image.load(self.directory + "/sprites/LEFT_4.png"),
                         pygame.image.load(self.directory + "/sprites/LEFT_5.png"),
                         pygame.image.load(self.directory + "/sprites/LEFT_6.png"),
                         pygame.image.load(self.directory + "/sprites/LEFT_7.png"),
                         pygame.image.load(self.directory + "/sprites/LEFT_8.png"),
                         pygame.image.load(self.directory + "/sprites/LEFT_9.png"),
                         pygame.image.load(self.directory + "/sprites/LEFT_10.png"),
                         pygame.image.load(self.directory + "/sprites/LEFT_11.png"),
                         pygame.image.load(self.directory + "/sprites/LEFT_12.png"),
                         pygame.image.load(self.directory + "/sprites/LEFT_13.png"),
                         pygame.image.load(self.directory + "/sprites/LEFT_14.png"),
                         pygame.image.load(self.directory + "/sprites/LEFT_15.png"),
                         pygame.image.load(self.directory + "/sprites/LEFT_16.png"),
                         ]

        self.walkUp = [pygame.image.load(self.directory + "/sprites/UP_1.png"),
                       pygame.image.load(self.directory + "/sprites/UP_2.png"),
                       pygame.image.load(self.directory + "/sprites/UP_3.png"),
                       pygame.image.load(self.directory + "/sprites/UP_4.png"),
                       pygame.image.load(self.directory + "/sprites/UP_5.png"),
                       pygame.image.load(self.directory + "/sprites/UP_6.png"),
                       pygame.image.load(self.directory + "/sprites/UP_7.png"),
                       pygame.image.load(self.directory + "/sprites/UP_8.png"),
                       pygame.image.load(self.directory + "/sprites/UP_9.png"),
                       pygame.image.load(self.directory + "/sprites/UP_10.png"),
                       pygame.image.load(self.directory + "/sprites/UP_11.png"),
                       pygame.image.load(self.directory + "/sprites/UP_12.png"),
                       pygame.image.load(self.directory + "/sprites/UP_13.png"),
                       pygame.image.load(self.directory + "/sprites/UP_14.png"),
                       pygame.image.load(self.directory + "/sprites/UP_15.png"),
                       pygame.image.load(self.directory + "/sprites/UP_16.png"),
                       ]

        self.walkDown = [pygame.image.load(self.directory + "/sprites/DOWN_1.png"),
                         pygame.image.load(self.directory + "/sprites/DOWN_2.png"),
                         pygame.image.load(self.directory + "/sprites/DOWN_3.png"),
                         pygame.image.load(self.directory + "/sprites/DOWN_4.png"),
                         pygame.image.load(self.directory + "/sprites/DOWN_5.png"),
                         pygame.image.load(self.directory + "/sprites/DOWN_6.png"),
                         pygame.image.load(self.directory + "/sprites/DOWN_7.png"),
                         pygame.image.load(self.directory + "/sprites/DOWN_8.png"),
                         pygame.image.load(self.directory + "/sprites/DOWN_9.png"),
                         pygame.image.load(self.directory + "/sprites/DOWN_10.png"),
                         pygame.image.load(self.directory + "/sprites/DOWN_11.png"),
                         pygame.image.load(self.directory + "/sprites/DOWN_12.png"),
                         pygame.image.load(self.directory + "/sprites/DOWN_13.png"),
                         pygame.image.load(self.directory + "/sprites/DOWN_14.png"),
                         pygame.image.load(self.directory + "/sprites/DOWN_15.png"),
                         pygame.image.load(self.directory + "/sprites/DOWN_16.png")
                         ]

        self.STAY = pygame.image.load(self.directory + "/sprites/STAY.png")

        self.clock = pygame.time.Clock()

        self.x = 110
        self.y = 100
        self.width = 15
        self.height = 22

        self.left = False
        self.right = False
        self.down = False
        self.up = False

        self.anim = 0
        self.speed = 5

        run = True

        while run:
            self.clock.tick(30)

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    run = False

            keys = pygame.key.get_pressed()

            if keys[pygame.K_LEFT] and self.x > self.speed:
                self.x -= self.speed
                self.left = True
                self.right = False
                self.up = False
                self.down = False

            elif keys[pygame.K_RIGHT]:
                self.x += self.speed
                self.right = True
                self.left = False
                self.up = False
                self.down = False

            elif keys[pygame.K_UP]:
                self.y -= self.speed
                self.up = True
                self.right = True
                self.left = False
                self.down = False

            elif keys[pygame.K_DOWN]:
                self.y += self.speed
                self.down = True
                self.right = True
                self.left = False
                self.up = False

            else:
                self.right = False
                self.left = False
                self.up = False
                self.down = False
                self.anim = 0

            self.draw()

    def draw(self):
        self.screen.fill((0, 0, 0))

        # LOAD BACKGROUND
        background_surf = pygame.image.load(self.directory + '/levels/level.png')
        background_surf = pygame.transform.scale(background_surf, (1000, 600))
        background_rect = background_surf.get_rect(bottomright=(1000, 600))
        self.screen.blit(background_surf, background_rect)

        if self.anim + 1 >= 30:
            self.anim = 0
        if self.right:
            self.screen.blit(self.walkRight[self.anim // 4], (self.x, self.y))
            self.anim += 2
        elif self.left:
            self.screen.blit(self.walkLeft[self.anim // 4], (self.x, self.y))
            self.anim += 2
        elif self.up:
            self.screen.blit(self.walkUp[self.anim // 4], (self.x, self.y))
            self.anim += 2
        elif self.down:
            self.screen.blit(self.walkDown[self.anim // 4], (self.x, self.y))
            self.anim += 2
        else:
            self.screen.blit(self.STAY, (self.x, self.y))
            self.anim = 0

        pygame.display.update()


if __name__ == "__main__":
    def start():
        win = Multiplayer()


    start()
