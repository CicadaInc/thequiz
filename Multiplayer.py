import os
import math
import pygame
from field import field


class Multiplayer():
    def __init__(self):
        self.field = field

        pygame.init()

        self.screenwidth = 1000
        self.screenheight = 600

        self.screen = pygame.display.set_mode((self.screenwidth, self.screenheight))
        pygame.display.set_caption("Multiplayer")

        self.directory = os.getcwd()

        self.walkRight, self.walkLeft, self.walkUp, self.walkDown = [], [], [], []
        self.load_animations()

        self.clock = pygame.time.Clock()

        self.x, self.y = 110, 100
        self.width, self.height = 15, 22

        self.left = None
        self.up = None

        self.anim, self.speed = 0, 6

        run = True
        while run:
            self.clock.tick(30)

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    run = False

            keys = pygame.key.get_pressed()

            if keys[pygame.K_LEFT]:
                self.x -= self.speed
                self.left, self.up = True, None
            elif keys[pygame.K_RIGHT]:
                self.x += self.speed
                self.left, self.up = False, None
            elif keys[pygame.K_UP]:
                self.y -= self.speed
                self.up, self.left = True, None
            elif keys[pygame.K_DOWN]:
                self.y += self.speed
                self.up, self.left = False, None
            else:
                self.left, self.up = None, None
                self.anim = 0

            if self.x < 0:
                self.x = 0
            if self.x >= 985:
                self.x = 985
            if self.y < 0:
                self.y = 0
            if self.y >= 578:
                self.y = 578

            if self.field[math.ceil(self.y // 25)][math.ceil(self.x // 25)] == 4:
                self.x = 110
                self.y = 100
            elif self.field[math.ceil(self.y // 25)][math.ceil(self.x // 25)] == 3:
                self.speed = 3
            elif self.field[math.ceil(self.y // 25)][math.ceil(self.x // 25)] == 1 or \
                    self.field[math.ceil(self.y // 25)][math.ceil(self.x // 25)] == 2:
                pass
            else:
                self.speed = 6

            self.draw()
            pygame.display.update()

    def load_animations(self):
        for i in range(1, 17):
            self.walkRight.append(
                pygame.image.load(self.directory + "/sprites/RIGHT_" + str(i) + '.png'))
            self.walkLeft.append(
                pygame.image.load(self.directory + "/sprites/LEFT_" + str(i) + '.png'))
            self.walkUp.append(pygame.image.load(self.directory + "/sprites/UP_" + str(i) + '.png'))
            self.walkDown.append(
                pygame.image.load(self.directory + "/sprites/DOWN_" + str(i) + '.png'))

        self.STAY = pygame.image.load(self.directory + "/sprites/STAY.png")

    def load_background(self):
        # LOAD BACKGROUND
        background_surf = pygame.image.load(self.directory + '/levels/level.png')
        background_surf = pygame.transform.scale(background_surf, (1000, 600))
        background_rect = background_surf.get_rect(bottomright=(1000, 600))
        self.screen.blit(background_surf, background_rect)

    def draw(self):
        self.load_background()

        if self.anim + 1 >= 30:
            self.anim = 0

        if (self.left is None and self.up is None):
            self.screen.blit(self.STAY, (self.x, self.y))
            self.anim = 0
        else:
            if not self.left and not (self.left is None):
                self.screen.blit(self.walkRight[self.anim // 4], (self.x, self.y))
            elif self.left:
                self.screen.blit(self.walkLeft[self.anim // 4], (self.x, self.y))
            elif self.up:
                self.screen.blit(self.walkUp[self.anim // 4], (self.x, self.y))
            elif not self.up:
                self.screen.blit(self.walkDown[self.anim // 4], (self.x, self.y))
            self.anim += 2


if __name__ == "__main__":
    def start():
        win = Multiplayer()


    start()
