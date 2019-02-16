import os
import pygame
from create_field import field


class Game:
    def __init__(self, character):
        pygame.init()

        self.winw, self.winh = 1000, 600
        self.winx, self.winy = 2300, 1550

        self.screen = pygame.display.set_mode((1000, 600))
        pygame.display.set_caption("TheQuiz")

        self.level = field
        self.directory = os.getcwd()

        self.character = character

        self.walkRight, self.walkLeft, self.walkUp, self.walkDown = [], [], [], []
        self.load_animations()

        self.clock = pygame.time.Clock()

        self.startx, self.starty = 468, 210
        self.right = None
        self.up = None

        self.k = 0

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

            x, y = self.winx - self.winw // 2, self.winy - self.winh // 2
            self.speed = 4
            # cell = self.level[y // 36][x // 36]
            # print(self.level[y // 36][((x + 24) // 36)])
            print(y // 36, x // 36)

            keys = pygame.key.get_pressed()
            if keys[pygame.K_LEFT] and self.level[y // 36][((x + self.speed) // 36)] in [0, 3, 4]:
                self.winx += self.speed
                self.left, self.up = True, None
            elif keys[pygame.K_RIGHT] and self.level[y // 36][(x - self.speed - 24) // 36] in [0, 3, 4]:
                self.winx -= self.speed
                self.left, self.up = False, None
            elif keys[pygame.K_UP] and self.level[(y + self.speed) // 36][(x - 12) // 36] in [0, 3, 4]:
                self.winy += self.speed
                self.up, self.left = True, None
            elif keys[pygame.K_DOWN] and self.level[(y - self.speed) // 36][(x - 12) // 36] in [0, 3, 4]:
                self.winy -= self.speed
                self.up, self.left = False, None
            else:
                self.left, self.up = None, None
                self.anim = 0

            if self.winx > 4236:
                self.winx = 4236
            if self.winx < 500:
                self.winx = 500
            if self.winy > 2472:
                self.winy = 2472
            if self.winy < 300:
                self.winy = 300
            if self.winx > 4204:
                self.winx = 4204
            print('self.winx: {}; self.winy: {}'.format(self.winx ,self.winy))

            self.render()
            pygame.display.update()

    def load_animations(self):
        for i in range(1, 4):
            self.walkRight.append(
                pygame.transform.scale(
                    pygame.image.load(self.directory + "/sprites/" + self.character + "/RIGHT_" + str(i) + '.png'),
                    (48, 64)))
            self.walkLeft.append(
                pygame.transform.scale(
                    pygame.image.load(self.directory + "/sprites/" + self.character + "/LEFT_" + str(i) + '.png'),
                    (48, 64)))
            self.walkUp.append(
                pygame.transform.scale(
                    pygame.image.load(self.directory + "/sprites/" + self.character + "/UP_" + str(i) + '.png'),
                    (48, 64)))
            self.walkDown.append(
                pygame.transform.scale(
                    pygame.image.load(self.directory + "/sprites/" + self.character + "/DOWN_" + str(i) + '.png'),
                    (48, 64)))
        self.STAY = pygame.transform.scale(
            pygame.image.load(self.directory + "/sprites/" + self.character + "/STAY" + '.png'), (48, 64))

    def load_background(self):
        # LOAD BACKGROUND
        self.background_surf = pygame.image.load(self.directory + '/levels/MainLocation.png')
        # self.background_surf = pygame.transform.scale(self.background_surf, (self.winw, self.winh))
        self.background_rect = self.background_surf.get_rect(bottomright=(self.winx, self.winy))
        self.screen.blit(self.background_surf, self.background_rect)

    def render(self):
        self.screen.fill((0, 0, 0))

        self.background_rect = self.background_surf.get_rect(bottomright=(self.winx, self.winy))
        self.screen.blit(self.background_surf, self.background_rect)

        if self.anim + 1 >= 30:
            self.anim = 0

        if self.left is None and self.up is None:
            self.screen.blit(self.STAY, (self.startx, self.starty))
            self.anim = 0
        else:
            if self.k == 1:
                self.anim += 1
                self.k = 0
            if not self.left and not (self.left is None):
                self.screen.blit(self.walkRight[self.anim % 3], (self.startx, self.starty))
            elif self.left:
                self.screen.blit(self.walkLeft[self.anim % 3], (self.startx, self.starty))
            elif self.up:
                self.screen.blit(self.walkUp[self.anim % 3], (self.startx, self.starty))
            elif not self.up:
                self.screen.blit(self.walkDown[self.anim % 3], (self.startx, self.starty))
            self.k += 0.25


if __name__ == "__main__":
    def test():
        HEROES = ['1(Townfolk-Child-M-001)', '2(Townfolk-Child-M)', '3(Townfolk-Adult-M-006)',
                  '4(coriander publish.)', '5(Mushroom-01)', '6(Cultist)']

        hero = HEROES[1]
        Game(hero)


    test()
