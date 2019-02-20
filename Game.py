import os
import pygame
from create_field import field
from Pause import Pause
import Dialogue
import Quest1
import time


class Game:
    def __init__(self, character, name):
        pygame.init()

        self.winw, self.winh = 1000, 600
        self.winx, self.winy = 2852, 1805

        self.screen = pygame.display.set_mode((1000, 600))
        pygame.display.set_caption("TheQuiz")

        self.michael = False
        self.musicStatus = False
        self.keysEggs = ''
        self.level = field
        self.directory = os.getcwd()

        self.solved1, self.solved2, self.solved3 = False, False, False

        self.character = character

        self.walkRight, self.walkLeft, self.walkUp, self.walkDown = [], [], [], []
        self.load_animations()

        self.clock = pygame.time.Clock()

        self.startx, self.starty = 468, 210
        self.right = None
        self.up = None

        self.oldMan = pygame.transform.scale(pygame.image.load("sprites/OldMan.png"), (48, 64))
        # self.mario = pygame.transform.scale(pygame.image.load("sprites/guido.png"), (34, 56))

        self.font = pygame.font.Font('fonts/freesansbold.ttf', 17)

        font = pygame.font.SysFont('Trebuchet MS', 12)
        font.set_bold(True)
        self.nick = font.render(name, False, pygame.Color('blue'))
        self.nameNpc1 = font.render("Brainfuck", 1, pygame.Color('blue'))

        self.k = 0
        self.pushed = None
        self.anim, self.speed = 0, 4

        self.set_interface()

        running = True
        while running:
            self.clock.tick(60)

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                    self.pushed = 'exit'
                if event.type == pygame.KEYDOWN:
                    print(event.key)
                    if event.key == 27:
                        p = Pause(self.screen, self)
                        if p.pushed == p.quit:
                            self.pushed = 'exit_main'
                            running = False
                    elif event.key == 101:
                        self.keysEggs += 'e'
                        if abs(self.npc1_x - 470) < 35 and abs(self.npc1_y - 200) < 35:
                            if not self.solved1:
                                phrases = Dialogue.create_dialogue1()
                            else:
                                phrases = Dialogue.create_dialogue5()
                            di = Dialogue.Dialogue(self.screen, self, phrases)
                            if di.pushed == 'exit':
                                running = False

                        elif 1130 >= self.winx >= 1030 and 2685 >= self.winy >= 2385 and not self.solved1:
                            phrases = Dialogue.create_dialogue2()
                            di = Dialogue.Dialogue(self.screen, self, phrases)
                            if di.pushed == 'exit':
                                self.pushed = 'exit'
                                running = False
                            else:
                                phrases = Quest1.create_dialogue1()
                                di = Quest1.Quest(self.screen, self, phrases)
                                if di.pushed == 'exit':
                                    self.pushed = 'exit'
                                    running = False
                                elif di.pushed == 'valid':
                                    self.solved1 = True
                                    phrases = Dialogue.create_dialogue3()
                                elif di.pushed == 'wrong':
                                    phrases = Dialogue.create_dialogue4()
                                if not (di.pushed is None) and di.pushed != 'exit':
                                    di = Dialogue.Dialogue(self.screen, self, phrases)
                                    if di.pushed == 'exit':
                                        self.pushed = 'exit'
                                        running = False
                        print(self.winx, self.winy)
                    elif event.key == 102:
                        self.keysEggs += 'f'
                    elif event.key == 97:
                        self.keysEggs += 'a'
                    elif event.key == 108:
                        self.keysEggs += 'l'
                    elif event.key == 115:
                        self.keysEggs += 's'
                    elif event.key == 98:
                        self.keysEggs += 'b'
                    elif event.key == 99:
                        self.keysEggs += 'c'
                    elif event.key == 100:
                        self.keysEggs += 'd'
                    elif event.key == 102:
                        self.keysEggs += 'f'
                    elif event.key == 103:
                        self.keysEggs += 'g'
                    elif event.key == 104:
                        self.keysEggs += 'h'
                    elif event.key == 105:
                        self.keysEggs += 'i'
                    elif event.key == 106:
                        self.keysEggs += 'j'
                    elif event.key == 107:
                        self.keysEggs += 'k'
                    elif event.key == 108:
                        self.keysEggs += 'l'
                    elif event.key == 109:
                        self.keysEggs += 'm'
                    elif event.key == 110:
                        self.keysEggs += 'n'
                    elif event.key == 111:
                        self.keysEggs += 'o'
                    elif event.key == 112:
                        self.keysEggs += 'p'
                    elif event.key == 114:
                        self.keysEggs += 'r'
                    elif event.key == 115:
                        self.keysEggs += 's'
                    elif event.key == 116:
                        self.keysEggs += 't'
                    elif event.key == 117:
                        self.keysEggs += 'u'
                    elif event.key == 118:
                        self.keysEggs += 'v'
                    elif event.key == 119:
                        self.keysEggs += 'w'
                    elif event.key == 120:
                        self.keysEggs += 'x'
                    elif event.key == 121:
                        self.keysEggs += 'y'
                    elif event.key == 122:
                        self.keysEggs += 'z'
                    elif event.key == 113:
                        self.keysEggs += 'q'
                        if self.michael is False:
                            self.michael = True
                        else:
                            self.michael = False

                    if 'falls' in self.keysEggs or 'gravity' in self.keysEggs:
                        print('GRAVITY FALLS')

                        # VIEW EGG
                        surf = pygame.image.load(self.directory + '/levels/px1.png')
                        rect = surf.get_rect(bottomright=(1000, 600))
                        self.screen.blit(surf, rect)
                        pygame.display.flip()

                        # self.background_surf = pygame.image.load(self.directory + '/levels/px1.png')
                        # self.background_surf = pygame.transform.scale(self.background_surf, (1000, 600))
                        # self.background_rect = self.background_surf.get_rect(bottomright=(1000, 600))

                        pygame.mixer.music.load(self.directory + '/sounds/gravity.mp3')
                        pygame.mixer.music.play(-1)
                        pygame.mixer.music.set_volume(1)

                        start = time.monotonic()
                        end = time.monotonic()
                        stop = False
                        while end - start <= 120:
                            for event in pygame.event.get():
                                if event.type == pygame.KEYDOWN:
                                    if event.key == 27:
                                        stop = True
                                        break
                                if event.type == pygame.QUIT:
                                    stop = True
                                    self.pushed = 'exit'
                                    running = False
                            if stop:
                                break
                            end = time.monotonic()

                        pygame.mixer.music.stop()

                        self.keysEggs = ''

                    if 'michael' in self.keysEggs or 'jackson' in self.keysEggs:
                        print('GRAVITY FALLS')

                        # VIEW EGG
                        surf = pygame.image.load(self.directory + '/levels/px2.jpg')
                        rect = surf.get_rect(bottomright=(1000, 600))
                        self.screen.blit(surf, rect)
                        pygame.display.flip()

                        # self.background_surf = pygame.image.load(self.directory + '/levels/px1.png')
                        # self.background_surf = pygame.transform.scale(self.background_surf, (1000, 600))
                        # self.background_rect = self.background_surf.get_rect(bottomright=(1000, 600))

                        pygame.mixer.music.load(self.directory + '/sounds/jackson.mp3')
                        pygame.mixer.music.play(-1)
                        pygame.mixer.music.set_volume(1)

                        start = time.monotonic()
                        end = time.monotonic()
                        stop = False
                        while end - start <= 240:
                            for event in pygame.event.get():
                                if event.type == pygame.KEYDOWN:
                                    if event.key == 27:
                                        stop = True
                                        break
                                if event.type == pygame.QUIT:
                                    stop = True
                                    self.pushed = 'exit'
                                    running = False
                            if stop:
                                break
                            end = time.monotonic()

                        pygame.mixer.music.stop()

                        self.keysEggs = ''

            x, y = (self.winx - 525) - self.winw // 2, (self.winy - 250) - self.winh // 2
            # print(y // 36, x // 36)

            if self.musicStatus is False:
                if (y // 36) == 61 and (x // 36) == 34:
                    self.musicStatus = True

                    pygame.mixer.music.stop()
                    pygame.mixer.music.load(self.directory + '/sounds/fight.mp3')
                    pygame.mixer.music.play(0)
                    pygame.mixer.music.set_volume(1)

            keys = pygame.key.get_pressed()

            if self.michael is False:
                if keys[pygame.K_LEFT]:
                    self.winx += self.speed
                    self.left, self.up = True, None
                elif keys[pygame.K_RIGHT]:
                    self.winx -= self.speed
                    self.left, self.up = False, None
                elif keys[pygame.K_UP]:
                    self.winy += self.speed
                    self.up, self.left = True, None
                elif keys[pygame.K_DOWN]:
                    self.winy -= self.speed
                    self.up, self.left = False, None
                else:
                    self.left, self.up = None, None
                    self.anim = 0
            else:
                if keys[pygame.K_LEFT]:
                    self.winx -= self.speed
                    self.left, self.up = True, None
                elif keys[pygame.K_RIGHT]:
                    self.winx += self.speed
                    self.left, self.up = False, None
                elif keys[pygame.K_UP]:
                    self.winy += self.speed
                    self.up, self.left = True, None
                elif keys[pygame.K_DOWN]:
                    self.winy -= self.speed
                    self.up, self.left = False, None
                else:
                    self.left, self.up = None, None
                    self.anim = 0

            if self.winx > 4720:
                self.winx = 4720
            if self.winx < 1050:
                self.winx = 1050
            if self.winy > 2743:
                self.winy = 2743
            if self.winy < 580:
                self.winy = 580

            self.render()

            pygame.display.flip()

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

    def set_interface(self):
        # LOAD BACKGROUND
        self.background_surf = pygame.image.load(self.directory + '/levels/MainLocation.png')
        self.background_rect = self.background_surf.get_rect(bottomright=(self.winx, self.winy))
        self.screen.blit(self.background_surf, self.background_rect)

        self.controls1 = self.font.render("esc - Пауза", 1, (0, 0, 0))
        self.controls1_x, self.controls1_y = 800, 520
        self.controls2 = self.font.render("e - Взаимодействовать", 1, (0, 0, 0))
        self.controls2_x, self.controls2_y = 800, 540

    def render(self):
        self.screen.fill((0, 0, 0))

        self.background_rect = self.background_surf.get_rect(bottomright=(self.winx, self.winy))
        self.screen.blit(self.background_surf, self.background_rect)

        self.npc1_x, self.npc1_y = -1730 + self.winx, -2350 + self.winy
        # print(self.npc1_x, self.npc1_y)
        self.screen.blit(self.oldMan, (self.npc1_x, self.npc1_y))
        # self.screen.blit(self.mario, (150, 150))

        self.screen.blit(self.nameNpc1, (self.npc1_x - 10, self.npc1_y - 15))

        self.screen.blit(self.nick, (self.startx - self.nick.get_width() // 2 + 24,
                                     self.starty - self.nick.get_height() // 2 - 5))

        self.screen.blit(self.controls1, (self.controls1_x, self.controls1_y))
        self.screen.blit(self.controls2, (self.controls2_x, self.controls2_y))

        if self.anim + 1 >= 30:
            self.anim = 0

        if self.left is None and self.up is None:
            self.screen.blit(self.STAY, (self.startx, self.starty))
            self.anim = 0
        else:
            if int(self.k) == 1:
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
            self.k += 0.15


if __name__ == "__main__":
    def test():
        HEROES = ['1(Townfolk-Child-M-001)', '2(Townfolk-Child-M)', '3(Townfolk-Adult-M-006)',
                  '4(coriander publish.)', '5(Mushroom-01)', '6(Cultist)']

        hero = HEROES[0]
        Game(hero, "SuperHero")


    test()
