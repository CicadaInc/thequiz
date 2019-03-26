import os
import time

import Dialogue
import Quest1
import Quest2
import eztext
import pygame
from Egg import Egg
from Pause import Pause
from create_field import field


class Game:
    def __init__(self, character, name):
        pygame.init()

        self.winw, self.winh = 1000, 600
        self.winx, self.winy = 2852, 1805

        self.needEggs = 6
        self.eggs = 0
        self.greeting = True
        self.falls = True
        self.queen = True
        self.sonic = True
        self.watchdogs = True
        self.python = True
        self.jackson = True

        self.name = name

        self.screen = pygame.display.set_mode((1000, 600))
        pygame.display.set_caption("TheQuiz")

        self.music = 0
        self.musicList = [
            'sounds/radio/1.mp3',
            'sounds/radio/2.mp3',
            'sounds/radio/3.mp3',
            'sounds/radio/4.mp3'
        ]
        self.lessonEasterEgg = True
        self.michael = False
        self.keysEggs = ''
        self.level = field
        self.directory = os.getcwd()
        self.sonicDogs = True

        self.show_info_flower = False
        self.solved1, self.solved2, self.solved3 = False, False, False

        self.character = character

        self.walkRight, self.walkLeft, self.walkUp, self.walkDown = [], [], [], []
        self.load_animations()

        self.music_played = False

        self.clock = pygame.time.Clock()

        self.startx, self.starty = 468, 210
        self.right = None
        self.up = None

        mars1 = False

        stime = 0

        self.k = 0
        self.pushed = None
        self.anim, self.speed = 0, 5

        self.set_interface()

        running = True
        while running:
            t = self.clock.tick(60)

            if self.music_played:
                stime += t

            x, y = (self.winx - 525) - self.winw // 2, (
                    self.winy - 250) - self.winh // 2
            print(y // 36, x // 36)
            print(self.winx, self.winy)

            self.events = pygame.event.get()
            for event in self.events:
                if event.type == pygame.QUIT:
                    running = False
                    self.pushed = 'exit'
                if event.type == pygame.KEYDOWN:
                    if self.greeting:
                        self.greeting = False
                        phrases = Dialogue.create_greeting_dialogue1()
                        di = Dialogue.Dialogue(self.screen, self, phrases)
                        if di.pushed == 'exit':
                            running = False
                        phrases = Dialogue.create_greeting_dialogue2()
                        di = Dialogue.Dialogue(self.screen, self, phrases)
                        if di.pushed == 'exit':
                            running = False
                        phrases = Dialogue.create_greeting_dialogue3()
                        di = Dialogue.Dialogue(self.screen, self, phrases)
                        if di.pushed == 'exit':
                            running = False
                    if event.key == 27:
                        p = Pause(self.screen, self)
                        if p.pushed == p.quit:
                            self.pushed = 'exit_main'
                            running = False
                    elif event.key == 101:
                        self.keysEggs += 'e'
                        if abs(self.npc1_x - 470) < 35 and abs(
                                self.npc1_y - 200) < 35:
                            if not self.solved1:
                                phrases = Dialogue.create_dialogue_for_quest1()
                            else:
                                phrases = Dialogue.create_dialogue_for_quest1_3()
                                self.solved3 = True
                            di = Dialogue.Dialogue(self.screen, self, phrases)
                            if di.pushed == 'exit':
                                running = False
                            phrases = Dialogue.create_dialogue20()
                            di = Dialogue.Dialogue(self.screen, self, phrases)
                            if di.pushed == 'exit':
                                running = False

                        elif y // 36 == 4 and x // 36 == 93:
                            phrases = Dialogue.create_dialogue21()
                            di = Dialogue.Dialogue(self.screen, self, phrases)
                            if di.pushed == 'exit':
                                running = False
                            mars1 = True
                        elif y // 36 == 32 and x // 36 == 83:
                            phrases = Dialogue.create_dialogue22()
                            di = Dialogue.Dialogue(self.screen, self, phrases)
                            if di.pushed == 'exit':
                                running = False
                        elif 1130 >= self.winx >= 1030 and 2685 >= self.winy >= 2385 \
                                and not self.solved1:
                            phrases = Dialogue.create_dialogue_for_quest1_2()
                            di = Dialogue.Dialogue(self.screen, self, phrases)
                            if di.pushed == 'exit':
                                self.pushed = 'exit'
                                running = False
                            else:
                                phrases = Quest1.create_text()
                                di = Quest1.Quest(self.screen, self, phrases)
                                if di.pushed == 'exit':
                                    self.pushed = 'exit'
                                    running = False
                                elif di.pushed == 'valid':
                                    self.solved1 = True
                                    phrases = Dialogue.create_win_dialogue_for_quest1()
                                elif di.pushed == 'wrong':
                                    phrases = Dialogue.create_wrong_dialogue_for_quests()
                                if not (
                                        di.pushed is None) and di.pushed != 'exit':
                                    di = Dialogue.Dialogue(self.screen, self,
                                                           phrases)
                                    if di.pushed == 'exit':
                                        self.pushed = 'exit'
                                        running = False
                        elif abs(self.npc2_x - 472) < 35 and abs(
                                self.npc2_y - 210) < 35:
                            if not self.solved2:
                                phrases = Dialogue.create_guide_dialogue1()
                                di = Dialogue.Dialogue(self.screen, self,
                                                       phrases)
                                if di.pushed == 'exit':
                                    running = False
                            else:
                                if not self.show_info_flower:
                                    self.show_info_flower = True
                                    phrases = Dialogue.create_guide_dialogue2()
                                    di = Dialogue.Dialogue(self.screen, self,
                                                           phrases)
                                    if di.pushed == 'exit':
                                        running = False
                                phrases = Dialogue.create_guide_dialogue3()
                                di = Dialogue.Dialogue(self.screen, self,
                                                       phrases)
                                if di.pushed == 'exit':
                                    running = False
                                phrases = Dialogue.create_guide_dialogue4()
                                di = Dialogue.Dialogue(self.screen, self,
                                                       phrases)
                                if di.pushed == 'exit':
                                    running = False
                        elif 3737 >= self.winx >= 3507 and 835 >= self.winy >= 780 \
                                and not self.solved2:
                            phrases = Dialogue.create_dialogue_for_quest2()
                            di = Dialogue.Dialogue(self.screen, self, phrases)
                            if di.pushed == 'exit':
                                self.pushed = 'exit'
                                running = False
                            else:
                                phrases = Quest2.create_text()
                                di = Quest2.Quest(self.screen, self, phrases)
                                if di.pushed == 'exit':
                                    self.pushed = 'exit'
                                    running = False
                                elif di.pushed == 'valid':
                                    self.solved2 = True
                                    phrases = Dialogue.create_win_dialogue_for_quest2()
                                elif di.pushed == 'wrong':
                                    phrases = Dialogue.create_wrong_dialogue_for_quests()
                                if not (
                                        di.pushed is None) and di.pushed != 'exit':
                                    di = Dialogue.Dialogue(self.screen, self,
                                                           phrases)
                                    if di.pushed == 'exit':
                                        self.pushed = 'exit'
                                        running = False

            self.textbox.update(self.events)

            if 'fm' in self.textbox.value:
                self.music += 1
                self.directory = os.getcwd()
                pygame.mixer.music.load(
                    self.directory + '/' + self.musicList[self.music % 4])
                pygame.mixer.music.play(-1)
                pygame.mixer.music.set_volume(1)
                self.textbox.value = ''

            if 'falls' in self.textbox.value or 'gravity' in self.textbox.value:
                if self.falls:
                    self.eggs += 1
                    Egg(self.screen, self.directory + '/levels/px1.png',
                        self.directory + '/sounds/gravity.mp3')
                    self.textbox.value = ''
                    self.falls = False
                    if self.eggs != self.needEggs:
                        phrases = Dialogue.create_dialogue_for_eggs(
                            self.needEggs - self.eggs)
                        di = Dialogue.Dialogue(self.screen, self, phrases)
                        if di.pushed == 'exit':
                            running = False

            if 'queen' in self.textbox.value or 'free' in self.textbox.value:
                if self.queen:
                    self.eggs += 1
                    Egg(self.screen, self.directory + '/levels/queen.jpg',
                        self.directory + '/sounds/queen.mp3')
                    self.textbox.value = ''
                    self.queen = False
                    if self.eggs != self.needEggs:
                        phrases = Dialogue.create_dialogue_for_eggs(
                            self.needEggs - self.eggs)
                        di = Dialogue.Dialogue(self.screen, self, phrases)
                        if di.pushed == 'exit':
                            running = False

            if 'sonic' in self.textbox.value:
                if self.sonic:
                    self.eggs += 1
                    Egg(self.screen, self.directory + '/levels/sonic.jpg',
                        self.directory + '/sounds/sonic.mp3')
                    self.textbox.value = ''
                    self.sonic = False
                    self.speed *= 3
                    if self.eggs != self.needEggs:
                        phrases = Dialogue.create_dialogue_for_eggs(
                            self.needEggs - self.eggs)
                        di = Dialogue.Dialogue(self.screen, self, phrases)
                        if di.pushed == 'exit':
                            running = False

            if 'watch' in self.textbox.value or 'dogs' in self.textbox.value:
                if self.watchdogs:
                    self.eggs += 1
                    Egg(self.screen, self.directory + '/levels/dogs.jpg',
                        self.directory + '/sounds/dogs.mp3')
                    self.textbox.value = ''
                    self.watchdogs = False
                    if self.eggs != self.needEggs:
                        phrases = Dialogue.create_dialogue_for_eggs(
                            self.needEggs - self.eggs)
                        di = Dialogue.Dialogue(self.screen, self, phrases)
                        if di.pushed == 'exit':
                            running = False

            if 'python' in self.textbox.value:
                if self.python:
                    self.eggs += 1
                    Egg(self.screen, self.directory + '/levels/python.jpg',
                        self.directory + '/sounds/dogs.mp3')
                    self.textbox.value = ''
                    self.python = False
                    if self.eggs != self.needEggs:
                        phrases = Dialogue.create_dialogue_for_eggs(
                            self.needEggs - self.eggs)
                        di = Dialogue.Dialogue(self.screen, self, phrases)
                        if di.pushed == 'exit':
                            running = False

            if 'michael' in self.textbox.value or 'jackson' in self.textbox.value:
                if self.jackson:
                    self.eggs += 1
                    Egg(self.screen, self.directory + '/levels/px2.jpg',
                        self.directory + '/sounds/jackson.mp3')
                    self.textbox.value = ''
                    self.michael = not self.michael
                    self.jackson = False
                    if self.eggs != self.needEggs:
                        phrases = Dialogue.create_dialogue_for_eggs(
                            self.needEggs - self.eggs)
                        di = Dialogue.Dialogue(self.screen, self, phrases)
                        if di.pushed == 'exit':
                            running = False

            if self.eggs == self.needEggs and self.solved1 and self.solved2 and self.solved3:
                self.surf = pygame.image.load(
                    self.directory + '/levels/theend.jpg')
                self.rect = self.surf.get_rect(bottomright=(1000, 600))

                self.screen.blit(self.surf, self.rect)
                pygame.mixer.music.load(self.directory + '/sounds/end.mp3')
                pygame.mixer.music.play(-1)
                pygame.mixer.music.set_volume(1)
                start = time.monotonic()
                end = time.monotonic()
                pygame.display.flip()
                end_of_end = False
                while end - start < 180:
                    if end_of_end:
                        break
                    end = time.monotonic()
                    for event in pygame.event.get():
                        if event.type == pygame.QUIT:
                            end_of_end = True

                running = False
                self.pushed = 'exit'

            if y // 36 == 4 and x // 36 == 7 and not self.music_played:
                pygame.mixer.music.load(self.directory + '/sounds/NLO.mp3')
                pygame.mixer.music.play(0)
                pygame.mixer.music.set_volume(1)
                self.music_played = True

            elif y // 36 == 53 and x // 36 == 32 and not self.music_played:
                pygame.mixer.music.load(self.directory + '/sounds/GodKnows.mp3')
                pygame.mixer.music.play(0)
                pygame.mixer.music.set_volume(1)
                self.music_played = True

            elif y // 36 == 51 and x // 36 == 96:
                if self.sonicDogs:
                    phrases = Dialogue.create_dialogue19()
                    di = Dialogue.Dialogue(self.screen, self, phrases)
                    if di.pushed == 'exit':
                        running = False
                    self.sonicDogs = False

            elif y // 36 == 6 and x // 36 == 66 and not self.music_played:
                pygame.mixer.music.load(
                    self.directory + '/sounds/morse_code.mp3')
                pygame.mixer.music.play(0)
                pygame.mixer.music.set_volume(1)
                pygame.event.wait()
                stime = 0
                self.music_played = True

            elif stime > 1500 and self.music_played:
                pygame.mixer.music.load(
                    self.directory + '/' + self.musicList[self.music % 4])
                pygame.mixer.music.play(-1)
                pygame.mixer.music.set_volume(1)
                stime = 0
                self.music_played = False

            self.move_player()
            self.check_border_relative()

            self.render()

            pygame.display.flip()

    def move_player(self):
        x, y = (self.winx - 525) - self.winw // 2, (
                self.winy - 250) - self.winh // 2
        keys = pygame.key.get_pressed()

        if keys[pygame.K_LEFT] or keys[pygame.K_a]:
            if not self.michael:
                if self.level[y // 36][(x + self.speed + 12) // 36] == 0:
                    self.winx += self.speed
                else:
                    self.up, self.left = None, None
            else:
                if self.level[y // 36][(x - self.speed) // 36] == 0:
                    self.winx -= self.speed
                else:
                    self.up, self.left = None, None
            self.up, self.left = None, True
        elif keys[pygame.K_RIGHT] or keys[pygame.K_d]:
            if not self.michael:
                if self.level[y // 36][(x - self.speed) // 36] == 0:
                    self.winx -= self.speed
                else:
                    self.up, self.left = None, None
            else:
                if self.level[y // 36][(x + self.speed + 12) // 36] == 0:
                    self.winx += self.speed
                else:
                    self.up, self.left = None, None
            self.up, self.left = None, False
        elif keys[pygame.K_UP] or keys[pygame.K_w]:
            if not self.michael:
                if self.level[(y + self.speed) // 36][x // 36] == 0:
                    self.winy += self.speed
                else:
                    self.up, self.left = None, None
            else:
                if self.level[(y - self.speed) // 36][x // 36] == 0:
                    self.winy -= self.speed
                else:
                    self.up, self.left = None, None
            self.up, self.left = True, None
        elif keys[pygame.K_DOWN] or keys[pygame.K_s]:
            if not self.michael:
                if self.level[(y - self.speed) // 36][x // 36] == 0:
                    self.winy -= self.speed
                else:
                    self.up, self.left = None, None
            else:
                if self.level[(y + self.speed) // 36][x // 36] == 0:
                    self.winy += self.speed
                else:
                    self.up, self.left = None, None
            self.up, self.left = False, None
        else:
            self.left, self.up = None, None
            self.anim = 0

    def check_border_relative(self):
        if self.winx > 4650:
            self.winx = 4650
        if self.winx < 1125:
            self.winx = 1125
        if self.winy > 2670:
            self.winy = 2670
        if self.winy < 670:
            self.winy = 670

    def load_animations(self):
        for i in range(1, 4):
            self.walkRight.append(
                pygame.transform.scale(
                    pygame.image.load(
                        self.directory + "/sprites/" + self.character + "/RIGHT_" + str(
                            i) + '.png'),
                    (48, 64)))
            self.walkLeft.append(
                pygame.transform.scale(
                    pygame.image.load(
                        self.directory + "/sprites/" + self.character + "/LEFT_" + str(
                            i) + '.png'),
                    (48, 64)))
            self.walkUp.append(
                pygame.transform.scale(
                    pygame.image.load(
                        self.directory + "/sprites/" + self.character + "/UP_" + str(
                            i) + '.png'),
                    (48, 64)))
            self.walkDown.append(
                pygame.transform.scale(
                    pygame.image.load(
                        self.directory + "/sprites/" + self.character + "/DOWN_" + str(
                            i) + '.png'),
                    (48, 64)))
        self.STAY = pygame.transform.scale(
            pygame.image.load(
                self.directory + "/sprites/" + self.character + "/STAY" + '.png'),
            (48, 64))

    def set_interface(self):
        # LOAD BACKGROUND
        self.font = pygame.font.Font('fonts/freesansbold.ttf', 17)

        self.background_surf = pygame.image.load(
            self.directory + '/levels/MainLocation.png')
        self.background_rect = self.background_surf.get_rect(
            bottomright=(self.winx, self.winy))
        self.screen.blit(self.background_surf, self.background_rect)

        self.controls1 = self.font.render("esc - Пауза", 1, (0, 0, 0))
        self.controls1_x, self.controls1_y = 800, 520
        self.controls2 = self.font.render("e - Взаимодействовать", 1, (0, 0, 0))
        self.controls2_x, self.controls2_y = 800, 540

        self.oldMan = pygame.transform.scale(
            pygame.image.load("sprites/OldMan.png"), (48, 64))
        self.guide = pygame.transform.scale(
            pygame.image.load("sprites/guide.png"), (48, 64))
        self.ilon_mask = pygame.transform.scale(
            pygame.image.load("sprites/ilon_mask.png"), (48, 64))

        font = pygame.font.SysFont('Trebuchet MS', 12)
        font.set_bold(True)
        self.nick = font.render(self.name, False, pygame.Color('blue'))
        self.nameNpc1 = font.render("Brainfuck", 1, pygame.Color('blue'))
        self.nameNpc2 = font.render("Гид Абрам", 1, pygame.Color('blue'))
        self.nameNpc3 = font.render("Ilon Mysk", 1, pygame.Color('blue'))

        self.textbox = eztext.Input(maxlength=1000, color=(0, 0, 0), prompt='',
                                    font=self.font)

    def render(self):
        self.screen.fill((255, 255, 255))

        self.background_rect = self.background_surf.get_rect(
            bottomright=(self.winx, self.winy))
        self.screen.blit(self.background_surf, self.background_rect)

        self.npc1_x, self.npc1_y = -1730 + self.winx, -2350 + self.winy
        self.screen.blit(self.oldMan, (self.npc1_x, self.npc1_y))
        self.npc2_x, self.npc2_y = -2590 + self.winx, -1460 + self.winy
        self.screen.blit(self.guide, (self.npc2_x, self.npc2_y))
        self.npc3_x, self.npc3_y = -3950 + self.winx, -535 + self.winy
        self.screen.blit(self.ilon_mask, (self.npc3_x, self.npc3_y))
        self.screen.blit(self.nameNpc1, (self.npc1_x - 10, self.npc1_y - 15))
        self.screen.blit(self.nameNpc2, (self.npc2_x - 10, self.npc2_y - 10))
        self.screen.blit(self.nameNpc3, (self.npc3_x - 10, self.npc3_y - 5))

        self.screen.blit(self.nick,
                         (self.startx - self.nick.get_width() // 2 + 24,
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
                self.screen.blit(self.walkRight[self.anim % 3],
                                 (self.startx, self.starty))
            elif self.left:
                self.screen.blit(self.walkLeft[self.anim % 3],
                                 (self.startx, self.starty))
            elif self.up:
                self.screen.blit(self.walkUp[self.anim % 3],
                                 (self.startx, self.starty))
            elif not self.up:
                self.screen.blit(self.walkDown[self.anim % 3],
                                 (self.startx, self.starty))
            self.k += 0.15


if __name__ == "__main__":
    def test():
        HEROES = ['1(Townfolk-Child-M-001)', '2(Townfolk-Child-M)',
                  '3(Townfolk-Adult-M-006)',
                  '4(coriander publish.)', '5(Mushroom-01)', '6(Cultist)']

        hero = HEROES[1]
        Game(hero, "SuperHero")


    test()
