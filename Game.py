import os
import pygame
from math import ceil


class Game():
    def __init__(self, winw, winh, caption, startx, starty, level, field, character):
        pygame.init()

        self.winw, self.winh = winw, winh

        self.screen = pygame.display.set_mode((winw, winh))
        pygame.display.set_caption(caption)

        self.level = level
        self.directory = os.getcwd()

        self.character = character

        self.walkRight, self.walkLeft, self.walkUp, self.walkDown = [], [], [], []
        self.load_animations()

        self.clock = pygame.time.Clock()

        self.x, self.y = startx, starty
        self.right = None
        self.left = None
        self.up = None
        self.pushed = None

        self.anim, self.speed = 0, 3

        self.load_background()

        run = True
        while run:
            self.clock.tick(30)

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    run = False
                    self.pushed = 'exit'

            if self.x < 0:
                self.x = 0
            if self.x >= winw - 15:
                self.x = winw - 21
            if self.y < 0:
                self.y = 0
            if self.y >= winh - 22:
                self.y = winh - 23
            x, y = self.x + 7, self.y + 11
            cell = field[ceil(y // 25)][ceil(x // 25)]
            if cell == 4:
                self.x, self.y = startx, starty
            elif cell == 3:
                self.speed = 3
            else:
                self.speed = 4

            keys = pygame.key.get_pressed()
            if keys[pygame.K_LEFT] and field[ceil(y // 25)][ceil((x - 8) // 25)] in [0, 3, 4]:
                self.x -= self.speed
                self.left, self.up = True, None
            elif keys[pygame.K_RIGHT] and field[ceil(y // 25)][ceil((x + 8) // 25)] in [0, 3, 4]:
                self.x += self.speed
                self.left, self.up = False, None
            elif keys[pygame.K_UP] and field[ceil((y - 11) // 25)][ceil(x // 25)] in [0, 3, 4]:
                self.y -= self.speed
                self.up, self.left = True, None
            elif keys[pygame.K_DOWN] and field[ceil((y + 11) // 25)][ceil(x // 25)] in [0, 3, 4]:
                self.y += self.speed
                self.up, self.left = False, None
            else:
                self.left, self.up = None, None
                self.anim = 0

            self.draw()
            pygame.display.update()

    def load_animations(self):
        for i in range(1, 4):
            self.walkRight.append(
                pygame.transform.scale(
                    pygame.image.load(self.directory + "/sprites/" + self.character + "/RIGHT_" + str(i) + '.png'),
                    (24, 32)))
            self.walkLeft.append(
                pygame.transform.scale(
                    pygame.image.load(self.directory + "/sprites/" + self.character + "/LEFT_" + str(i) + '.png'),
                    (24, 32)))
            self.walkUp.append(
                pygame.transform.scale(
                    pygame.image.load(self.directory + "/sprites/" + self.character + "/UP_" + str(i) + '.png'),
                    (24, 32)))
            self.walkDown.append(
                pygame.transform.scale(
                    pygame.image.load(self.directory + "/sprites/" + self.character + "/DOWN_" + str(i) + '.png'),
                    (24, 32)))
        self.STAY = pygame.transform.scale(
            pygame.image.load(self.directory + "/sprites/" + self.character + "/STAY" + '.png'), (24, 32))

    def load_background(self):
        # LOAD BACKGROUND
        self.background_surf = pygame.image.load(self.directory + '/levels/' + self.level)
        # self.background_surf = pygame.transform.scale(self.background_surf, (self.winw, self.winh))
        self.background_rect = self.background_surf.get_rect(bottomright=(self.winw, self.winh))
        self.screen.blit(self.background_surf, self.background_rect)

    def draw(self):
        self.screen.blit(self.background_surf, self.background_rect)

        if self.anim + 1 >= 30:
            self.anim = 0

        if self.left is None and self.up is None:
            self.screen.blit(self.STAY, (self.x, self.y))
            self.anim = 0
        else:
            if not self.left and not (self.left is None):
                self.screen.blit(self.walkRight[self.anim % 3], (self.x, self.y))
            elif self.left:
                self.screen.blit(self.walkLeft[self.anim % 3], (self.x, self.y))
            elif self.up:
                self.screen.blit(self.walkUp[self.anim % 3], (self.x, self.y))
            elif not self.up:
                self.screen.blit(self.walkDown[self.anim % 3], (self.x, self.y))
            self.anim += 1


if __name__ == "__main__":
    from field import field


    def test():
        win = Game(1000, 600, "Multiplayer", 100, 60, "level.png", field, '1(Townfolk-Child-M-001)')


    test()
