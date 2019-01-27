import os
import pygame
from math import ceil
from ChooseCharacter import ChooseCharacter as CC
class Game():
    def __init__(self, winw, winh, caption, startx, starty, level, field):
        pygame.init()

        self.winw, self.winh = winw, winh

        self.screen = pygame.display.set_mode((winw, winh))
        pygame.display.set_caption(caption)

        self.level = level
        self.directory = os.getcwd()

        self.walkRight, self.walkLeft, self.walkUp, self.walkDown = [], [], [], []
        self.load_animations()

        self.clock = pygame.time.Clock()

        self.x, self.y = startx, starty

        self.left = None
        self.up = None

        self.pushed = None

        self.anim, self.speed = 0, 6

        run = True
        while run:
            self.clock.tick(60)

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    run = False
                    self.pushed = 'exit'
            # if CC(choosed=1):
            #     if self.x < 0:
            #         self.x = 0
            #     if self.x >= winw - 16:
            #         self.x = winw - 17
            #     if self.y < 0:
            #         self.y = 0
            #     if self.y >= winh - 23:
            #         self.y = winh - 24
            # elif CC(choosed=2):
            #     if self.x < 0:
            #         self.x = 0
            #     if self.x >= winw - 16:
            #         self.x = winw - 17
            #     if self.y < 0:
            #         self.y = 0
            #     if self.y >= winh - 24:
            #         self.y = winh - 25
            # elif CC(choosed=3):
            #     if self.x < 0:
            #         self.x = 0
            #     if self.x >= winw - 20:
            #         self.x = winw - 21
            #     if self.y < 0:
            #         self.y = 0
            #     if self.y >= winh - 28:
            #         self.y = winh - 29
            # elif CC(choosed=4):
            #     if self.x < 0:
            #         self.x = 0
            #     if self.x >= winw - 18:
            #         self.x = winw - 19
            #     if self.y < 0:
            #         self.y = 0
            #     if self.y >= winh - 31:
            #         self.y = winh - 32
            # elif CC(choosed=5):
            #     if self.x < 0:
            #         self.x = 0
            #     if self.x >= winw - 13:
            #         self.x = winw - 14
            #     if self.y < 0:
            #         self.y = 0
            #     if self.y >= winh - 17:
            #         self.y = winh - 18
            # elif CC(choosed=6):
            #     if self.x < 0:
            #         self.x = 0
            #     if self.x >= winw - 16:
            #         self.x = winw - 17
            #     if self.y < 0:
            #         self.y = 0
            #     if self.y >= winh - 29:
            #         self.y = winh - 30
            # else:
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
                self.speed = 6

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
        # MainCharacter
        # if CC(choosed=1):
        #     for i in range(1, 4):
        #         self.walkRight.append(
        #             pygame.image.load(self.directory + "/sprites/1(Townfolk-Child-M-001)/RIGHT_" + str(i) + '.png'))
        #         self.walkLeft.append(
        #             pygame.image.load(self.directory + "/sprites/1(Townfolk-Child-M-001)/LEFT_" + str(i) + '.png'))
        #         self.walkUp.append(pygame.image.load(self.directory + "/sprites/1(Townfolk-Child-M-001)/UP_" + str(i) + '.png'))
        #         self.walkDown.append(
        #             pygame.image.load(self.directory + "/sprites/1(Townfolk-Child-M-001)/DOWN_" + str(i) + '.png'))
        #     self.STAY = pygame.image.load(self.directory + "/sprites/1(Townfolk-Child-M-001)/STAY.png")
        # elif CC(choosed=2):
        #     for i in range(1, 4):
        #         self.walkRight.append(
        #             pygame.image.load(self.directory + "/sprites/2(Townfolk-Child-M)/RIGHT_" + str(i) + '.png'))
        #         self.walkLeft.append(
        #             pygame.image.load(self.directory + "/sprites/2(Townfolk-Child-M)/LEFT_" + str(i) + '.png'))
        #         self.walkUp.append(
        #             pygame.image.load(self.directory + "/sprites/2(Townfolk-Child-M)/UP_" + str(i) + '.png'))
        #         self.walkDown.append(
        #             pygame.image.load(self.directory + "/sprites/2(Townfolk-Child-M)/DOWN_" + str(i) + '.png'))
        #         self.STAY = pygame.image.load(self.directory + "/sprites/2(Townfolk-Child-M)/STAY.png")
        # elif CC(choosed=3):
        #     for i in range(1, 4):
        #         self.walkRight.append(
        #             pygame.image.load(self.directory + "/sprites/3(Townfolk-Adult-M-006)/RIGHT_" + str(i) + '.png'))
        #         self.walkLeft.append(
        #             pygame.image.load(self.directory + "/sprites/3(Townfolk-Adult-M-006)/LEFT_" + str(i) + '.png'))
        #         self.walkUp.append(
        #             pygame.image.load(self.directory + "/sprites/3(Townfolk-Adult-M-006)/UP_" + str(i) + '.png'))
        #         self.walkDown.append(
        #             pygame.image.load(self.directory + "/sprites/3(Townfolk-Adult-M-006)/DOWN_" + str(i) + '.png'))
        #     self.STAY = pygame.image.load(self.directory + "/sprites/3(Townfolk-Adult-M-006)/STAY.png")
        # elif CC(choosed=4):
        #     for i in range(1, 4):
        #         self.walkRight.append(
        #             pygame.image.load(self.directory + "/sprites/4(coriander publish.)/RIGHT_" + str(i) + '.png'))
        #         self.walkLeft.append(
        #             pygame.image.load(self.directory + "/sprites/4(coriander publish.)/LEFT_" + str(i) + '.png'))
        #         self.walkUp.append(
        #             pygame.image.load(self.directory + "/sprites/4(coriander publish.)/UP_" + str(i) + '.png'))
        #         self.walkDown.append(
        #             pygame.image.load(self.directory + "/sprites/4(coriander publish.)/DOWN_" + str(i) + '.png'))
        #     self.STAY = pygame.image.load(self.directory + "/sprites/4(coriander publish.)/STAY.png")
        # elif CC(choosed=5):
        #     for i in range(1, 4):
        #         self.walkRight.append(
        #             pygame.image.load(self.directory + "/sprites/5(Mushroom-01)/RIGHT_" + str(i) + '.png'))
        #         self.walkLeft.append(
        #             pygame.image.load(self.directory + "/sprites/5(Mushroom-01)/LEFT_" + str(i) + '.png'))
        #         self.walkUp.append(
        #             pygame.image.load(self.directory + "/sprites/5(Mushroom-01)/UP_" + str(i) + '.png'))
        #         self.walkDown.append(
        #             pygame.image.load(self.directory + "/sprites/5(Mushroom-01)/DOWN_" + str(i) + '.png'))
        #     self.STAY = pygame.image.load(self.directory + "/sprites/5(Mushroom-01)/STAY.png")
        # elif CC(choosed=6):
        #     for i in range(1, 4):
        #         self.walkRight.append(
        #             pygame.image.load(self.directory + "/sprites/6(Cultist)/RIGHT_" + str(i) + '.png'))
        #         self.walkLeft.append(
        #             pygame.image.load(self.directory + "/sprites/6(Cultist)/LEFT_" + str(i) + '.png'))
        #         self.walkUp.append(
        #             pygame.image.load(self.directory + "/sprites/6(Cultist)/UP_" + str(i) + '.png'))
        #         self.walkDown.append(
        #             pygame.image.load(self.directory + "/sprites/6(Cultist)/DOWN_" + str(i) + '.png'))
        #     self.STAY = pygame.image.load(self.directory + "/sprites/6(Cultist)/STAY.png")
        # else:
        for i in range(1, 17):
            self.walkRight.append(
                pygame.image.load(self.directory + "/sprites/MainCharacter/RIGHT_" + str(i) + '.png'))
            self.walkLeft.append(
                pygame.image.load(self.directory + "/sprites/MainCharacter/LEFT_" + str(i) + '.png'))
            self.walkUp.append(pygame.image.load(self.directory + "/sprites/MainCharacter/UP_" + str(i) + '.png'))
            self.walkDown.append(
                pygame.image.load(self.directory + "/sprites/MainCharacter/DOWN_" + str(i) + '.png'))

        self.STAY = pygame.image.load(self.directory + "/sprites/MainCharacter/STAY.png")

    def load_background(self):
        # LOAD BACKGROUND
        background_surf = pygame.image.load(self.directory + '/levels/' + self.level)
        background_surf = pygame.transform.scale(background_surf, (self.winw, self.winh))
        background_rect = background_surf.get_rect(bottomright=(self.winw, self.winh))
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
            self.anim += 1


if __name__ == "__main__":
    from field import field


    def test():
        win = Game(1000, 600, "Multiplayer", 100, 60, "level.png", field)


    test()
