import os
import time

import pygame
from pygame.locals import *


class Dialogue:
    def __init__(self, screen, game, phrases):
        self.screen = screen
        self.surface = pygame.Surface((230, 180), pygame.SRCALPHA)
        self.font = pygame.font.Font("fonts/freesansbold.ttf", 20)
        self.phrases = phrases
        self.pushed = None
        self.game = game

        pygame.mouse.set_visible(False)

        self.set_interface()

        running = True
        while running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.pushed = 'exit'
                    running = False
                if event.type == pygame.MOUSEBUTTONDOWN:
                    x, y = event.pos
                    if self.close.collidepoint(x - 400, y - 200):
                        running = False

            self.render()
            pygame.display.flip()

    def set_interface(self):
        self.close = pygame.Rect(70, 140, 100, 30)
        self.close_text = self.font.render("Закрыть", 1, (0, 0, 0))
        self.close_x, self.close_y = 80, 145
        self.win = pygame.Rect(0, 0, 229, 179)
        self.cursor = pygame.image.load('sprites/ForGUI/cursor1.png')

    def render(self):
        self.game.render()

        self.surface.fill((200, 220, 190))

        pygame.draw.rect(self.surface, (0, 0, 0), self.win, 2)

        pygame.draw.rect(self.surface, (250, 175, 255), self.close)
        pygame.draw.rect(self.surface, (0, 0, 0), self.close, 2)
        self.surface.blit(self.close_text, (self.close_x, self.close_y))

        for i in range(len(self.phrases)):
            self.surface.blit(self.phrases[i][0], self.phrases[i][1])

        self.screen.blit(self.surface, (400, 200))

        pos = pygame.mouse.get_pos()
        rect = self.cursor.get_rect(topleft=pos)
        self.screen.blit(self.cursor, rect)


def create_greeting_dialogue1():
    font = pygame.font.Font('fonts/comic.ttf', 16)

    return [(font.render("Добро пожаловать в", 1, (0, 0, 0)), (10, 0)),
            (font.render("The Quiz, игру главной", 1, (0, 0, 0)), (10, 15)),
            (font.render("целью которой явлется", 1, (0, 0, 0)), (10, 30)),
            (font.render("поиск пасхалок", 1, (0, 0, 0)), (10, 45)),
            (font.render("и разгадывание сюжетов.", 1, (0, 0, 0)), (10, 60)),
            (font.render("Чтобы узнать больше", 1, (0, 0, 0)), (10, 75)),
            (font.render("отправляйтесь к гиду", 1, (0, 0, 0)), (10, 90)),
            (
                font.render("Абраму. Он знает здесь все", 1, (0, 0, 0)),
                (10, 105)),
            (font.render("(или почти все)", 1, (0, 0, 0)), (10, 120))]


def create_greeting_dialogue2():
    font = pygame.font.Font('fonts/comic.ttf', 16)

    return [(font.render("И, кстати, игра", 1, (0, 0, 0)), (10, 0)),
            (font.render("создана для развития", 1, (0, 0, 0)), (10, 15)),
            (font.render("умственных способностей,", 1, (0, 0, 0)), (10, 30)),
            (font.render("поэтому порой будет", 1, (0, 0, 0)), (10, 45)),
            (font.render("совсем-совсем нелего.", 1, (0, 0, 0)), (10, 60)),
            (font.render("Во время прохождения", 1, (0, 0, 0)), (10, 75)),
            (font.render("будьте предельно", 1, (0, 0, 0)), (10, 90)),
            (font.render("внимательны.", 1, (0, 0, 0)), (10, 105))]


def create_greeting_dialogue3():
    font = pygame.font.Font('fonts/comic.ttf', 16)

    return [(font.render("По окончанию игры", 1, (0, 0, 0)), (10, 0)),
            (font.render("вы можете считать себя", 1, (0, 0, 0)), (10, 15)),
            (font.render("очень эрудированным", 1, (0, 0, 0)), (10, 30)),
            (font.render("человеком!", 1, (0, 0, 0)), (10, 45)),
            (font.render("P.s. Для закрытия пасхалки", 1, (0, 0, 0)), (10, 75)),
            (font.render("нажмите 'Esc'.", 1, (0, 0, 0)), (10, 90)),
            (font.render("Для смены музыки", 1, (0, 0, 0)), (10, 105)),
            (font.render('введите "fm".', 1, (0, 0, 0)), (10, 120))]


def create_guide_dialogue1():
    font = pygame.font.Font('fonts/comic.ttf', 16)

    return [(font.render("Таки прифетсфую тебя, мо-", 1, (0, 0, 0)), (10, 10)),
            (font.render("лодой челофек. Добро поша-", 1, (0, 0, 0)), (10, 25)),
            (font.render("лофать в Страну Недураков.", 1, (0, 0, 0)), (10, 40)),
            (font.render("Таки если принесешь мне", 1, (0, 0, 0)), (10, 55)),
            (font.render("шейкелей, шо Буратино у", 1, (0, 0, 0)), (10, 70)),
            (font.render("моста на юго-западе зарыл", 1, (0, 0, 0)), (10, 85)),
            (font.render("то таки узнаешь все про все.", 1, (0, 0, 0)),
             (10, 100))]


def create_dialogue_for_quest2():
    font = pygame.font.Font('fonts/comic.ttf', 16)

    return [(font.render("Вы откопали сундук.", 1, (0, 0, 0)), (10, 10)),
            (font.render("Но он закрыт мегасекретным", 1, (0, 0, 0)), (10, 25)),
            (font.render("кодом. Также на сундуке", 1, (0, 0, 0)), (10, 40)),
            (font.render("вы находите надписи", 1, (0, 0, 0)), (10, 55)),
            (font.render("на латинице", 1, (0, 0, 0)), (10, 70)),
            (font.render("(Хорошо, что вы учились", 1, (0, 0, 0)), (10, 85)),
            (font.render("на медфаке, поэтому", 1, (0, 0, 0)), (10, 100)),
            (font.render("сможете их прочитать)", 1, (0, 0, 0)), (10, 115))]


def create_win_dialogue_for_quest2():
    font = pygame.font.Font('fonts/comic.ttf', 20)

    return [(font.render("Хорошая работа ^_^", 1, (0, 0, 0)), (10, 10)),
            (font.render("Шейкели + 100", 1, (0, 0, 0)), (10, 40))]


def create_guide_dialogue2():
    font = pygame.font.Font('fonts/comic.ttf', 16)

    return [(font.render("Таки ты не промах,", 1, (0, 0, 0)), (10, 10)),
            (font.render("как я погляжу.", 1, (0, 0, 0)), (10, 25)),
            (font.render("Как и договаривались,", 1, (0, 0, 0)), (10, 40)),
            (font.render("я расскажу тебе", 1, (0, 0, 0)), (10, 55)),
            (font.render("все, что происходит", 1, (0, 0, 0)), (10, 70)),
            (font.render("в нашей чудесной стране.", 1, (0, 0, 0)), (10, 85)),
            (font.render("ШЕЙКЕЛИ - 100", 1, (0, 0, 0)), (10, 115))]


def create_guide_dialogue3():
    font = pygame.font.Font('fonts/comic.ttf', 16)

    return [(font.render("На калдбище к сеферу", 1, (0, 0, 0)), (10, 10)),
            (font.render("расположено феликое", 1, (0, 0, 0)), (10, 25)),
            (font.render("творение разработчиков.", 1, (0, 0, 0)), (10, 40)),
            (font.render("А на сеферо-западе", 1, (0, 0, 0)), (10, 55)),
            (font.render("кто-то кто-то", 1, (0, 0, 0)), (10, 70)),
            (font.render("кто-то кто-то", 1, (0, 0, 0)), (10, 85)),
            (font.render("кто-то кто-то", 1, (0, 0, 0)), (10, 100)),
            (font.render("кто-то кто-то", 1, (0, 0, 0)), (10, 115))]


def create_guide_dialogue4():
    font = pygame.font.Font('fonts/comic.ttf', 16)

    return [(font.render("Могу сказать, что", 1, (0, 0, 0)), (10, 10)),
            (font.render("тут Майкл Джексон", 1, (0, 0, 0)), (10, 25)),
            (font.render("ф почете. И еще", 1, (0, 0, 0)), (10, 40)),
            (font.render("мы фсе фанатеем от", 1, (0, 0, 0)), (10, 55)),
            (font.render("Гравити Фолз.", 1, (0, 0, 0)), (10, 70)),
            (font.render("Таки это был очень прямой", 1, (0, 0, 0)), (10, 85)),
            (font.render("намек на использование", 1, (0, 0, 0)), (10, 100)),
            (font.render("устройства ввода.", 1, (0, 0, 0)), (10, 115))]


def create_dialogue_for_quest1():
    font = pygame.font.Font('fonts/comic.ttf', 16)

    return [(font.render("Зравствуй, странник.", 1, (0, 0, 0)), (10, 10)),
            (font.render("Мое имя Brainfuck.", 1, (0, 0, 0)), (10, 25)),
            (font.render("Меня прозвали в честь", 1, (0, 0, 0)), (10, 40)),
            (font.render("одноименного ЯП.", 1, (0, 0, 0)), (10, 55)),
            (font.render("Найди компилятор", 1, (0, 0, 0)), (10, 70)),
            (font.render("у водопада", 1, (0, 0, 0)), (10, 85)),
            (font.render("мой верный, и да будет", 1, (0, 0, 0)), (10, 100)),
            (font.render("карма твоя чиста", 1, (0, 0, 0)), (10, 115))]


def create_dialogue_for_quest1_2():
    font = pygame.font.Font('fonts/comic.ttf', 16)

    return [(font.render("Вы нашли компилятор,", 1, (0, 0, 0)), (10, 10)),
            (font.render("но все не может быть", 1, (0, 0, 0)), (10, 25)),
            (font.render("так просто - ", 1, (0, 0, 0)), (10, 40)),
            (font.render("компилятор зашифрован", 1, (0, 0, 0)), (10, 55)),
            (font.render("суперкодом, и вам", 1, (0, 0, 0)), (10, 70)),
            (font.render("придется решить эту задачу", 1, (0, 0, 0)),
             (10, 85)), ]


def create_win_dialogue_for_quest1():
    font = pygame.font.Font('fonts/comic.ttf', 20)

    return [(font.render("Хорошая работа ^_^", 1, (0, 0, 0)), (10, 10)),
            (font.render("Карма + 100", 1, (0, 0, 0)), (10, 55)), ]


def create_wrong_dialogue_for_quests():
    font = pygame.font.Font('fonts/comic.ttf', 20)

    return [(font.render("Неверно", 1, (0, 0, 0)), (10, 10)),
            (font.render("Попробуйте еще :(", 1, (0, 0, 0)), (10, 40)), ]


def create_dialogue_for_quest1_3():
    font = pygame.font.Font('fonts/comic.ttf', 16)

    return [(font.render("Благодарю тебя, странник.", 1, (0, 0, 0)), (10, 10)),
            (font.render("Теперь я могу снова", 1, (0, 0, 0)), (10, 25)),
            (font.render("выносить мозги.", 1, (0, 0, 0)), (10, 40)),
            (font.render("И да будет карма", 1, (0, 0, 0)), (10, 55)),
            (font.render("твоя чиста.", 1, (0, 0, 0)), (10, 70))]


def create_dialogue_for_eggs(number):
    font = pygame.font.Font('fonts/comic.ttf', 16)

    return [(font.render("Поздравляем!", 1, (0, 0, 0)), (10, 0)),
            (font.render("найдена пасхалка", 1, (0, 0, 0)), (10, 15)),
            (
                font.render("осталось ещё " + str(number), 1, (0, 0, 0)),
                (10, 30)), ]


def create_dialogue19():
    font = pygame.font.Font('fonts/comic.ttf', 16)

    return [(font.render("Привет!", 1, (0, 0, 0)), (10, 0)),
            (font.render('ищи "вторую собаку"', 1, (0, 0, 0)), (10, 15)),
            (font.render(";)", 1, (0, 0, 0)), (10, 30)), ]


def create_dialogue20():
    font = pygame.font.Font('fonts/comic.ttf', 16)

    return [(font.render("Кстати, ходят слухи,", 1, (0, 0, 0)), (10, 0)),
            (font.render('что в наших краях марс"', 1, (0, 0, 0)), (10, 15)),
            (font.render("колонизировать собираются.", 1, (0, 0, 0)), (10, 30)),
            (font.render("Иди к юго-западу, да", 1, (0, 0, 0)), (10, 45)),
            (font.render("побори нечесть, добрый", 1, (0, 0, 0)), (10, 60)),
            (font.render("странник.", 1, (0, 0, 0)), (10, 75))]


def create_dialogue21():
    font = pygame.font.Font('fonts/comic.ttf', 16)

    return [(font.render("Еммн...", 1, (0, 0, 0)), (10, 0)),
            (font.render('Привет, марсианин, ой', 1, (0, 0, 0)), (10, 15)),
            (font.render("странник. Не ведал ли ты", 1, (0, 0, 0)), (10, 30)),
            (font.render("где тут блюдце летающее", 1, (0, 0, 0)), (10, 45)),
            (font.render("упало? Вроде мелькнула на", 1, (0, 0, 0)), (10, 60)),
            (
                font.render("востоке. Отыщи её и принеси", 1, (0, 0, 0)),
                (10, 75)),
            (font.render("мне код ошибки. Но знай,", 1, (0, 0, 0)), (10, 90)),
            (font.render("он зашифрован.", 1, (0, 0, 0)), (10, 105))]


def create_dialogue22():
    font = pygame.font.Font('fonts/comic.ttf', 16)

    return [(font.render("Еммн...", 1, (0, 0, 0)), (10, 0)),
            (font.render('Здравствуй, странник.', 1, (0, 0, 0)), (10, 15)),
            (font.render("Иди на северо-восток, к", 1, (0, 0, 0)), (10, 30)),
            (font.render("доброму старцу, ему нужна", 1, (0, 0, 0)), (10, 45)),
            (font.render("помощь, а потом", 1, (0, 0, 0)), (10, 60)),
            (font.render("возвращайся.", 1, (0, 0, 0)), (10, 75)),
            (font.render("...", 1, (0, 0, 0)), (10, 90)),
            (font.render("Удачи, странник.", 1, (0, 0, 0)), (10, 105))]


def create_dialogue_for_Ilon_1():
    font = pygame.font.Font('fonts/comic.ttf', 16)

    return [(font.render("Пшпхпх... Бум...", 1, (0, 0, 0)), (10, 0)),
            (font.render('Напугался? Не стоит.', 1, (0, 0, 0)), (10, 15)),
            (font.render("Я всего лишь ИИ, который", 1, (0, 0, 0)), (10, 30)),
            (font.render("умнее тебя в 51 раз.", 1, (0, 0, 0)), (10, 45)),
            (font.render("Отнеси код Ilon'у", 1, (0, 0, 0)), (10, 60)),
            (font.render('"OCTU"', 1, (0, 0, 0)), (10, 75)),
            (font.render("", 1, (0, 0, 0)), (10, 90)),
            (font.render("", 1, (0, 0, 0)), (10, 105))]


def create_dialogue_for_Ilon_2():
    font = pygame.font.Font('fonts/comic.ttf', 16)

    return [(font.render("Его нужно расшифровать.", 1, (0, 0, 0)), (10, 0)),
            (font.render('Я бы сам... Да', 1, (0, 0, 0)), (10, 15)),
            (font.render("компилятор сломан, так", 1, (0, 0, 0)), (10, 30)),
            (font.render("что тебе придётся это", 1, (0, 0, 0)), (10, 45)),
            (font.render("сделать самому.", 1, (0, 0, 0)), (10, 60)),
            (font.render('Вспомни древнеримских', 1, (0, 0, 0)), (10, 75)),
            (font.render("политических деятелей.", 1, (0, 0, 0)), (10, 90)),
            (font.render("Удачи, землянин.", 1, (0, 0, 0)), (10, 105))]


def create_dialogue_for_Ilon_4():
    font = pygame.font.Font('fonts/comic.ttf', 16)

    return [(font.render("Спасибо, странник.", 1, (0, 0, 0)), (10, 0)),
            (font.render('Теперь я снова могу', 1, (0, 0, 0)), (10, 15)),
            (font.render("летать автостопом по", 1, (0, 0, 0)), (10, 30)),
            (font.render("галактике!", 1, (0, 0, 0)), (10, 45)),
            (font.render("", 1, (0, 0, 0)), (10, 60)),
            (font.render('', 1, (0, 0, 0)), (10, 75)),
            (font.render("", 1, (0, 0, 0)), (10, 90)),
            (font.render("", 1, (0, 0, 0)), (10, 105))]


def create_dialogue_for_Ilon_5():
    font = pygame.font.Font('fonts/comic.ttf', 16)

    return [(font.render("Дам тебе совет.", 1, (0, 0, 0)), (10, 0)),
            (font.render('По дороге домой, идя', 1, (0, 0, 0)), (10, 15)),
            (font.render("по тропе услышишь звуки.", 1, (0, 0, 0)), (10, 30)),
            (font.render("Это шифр. Чтобы его", 1, (0, 0, 0)), (10, 45)),
            (font.render("разгадать, приостановись,", 1, (0, 0, 0)), (10, 60)),
            (font.render('дослушай до конца. Это', 1, (0, 0, 0)), (10, 75)),
            (font.render("что-то в духе морзянки.", 1, (0, 0, 0)), (10, 90)),
            (font.render("Удачи, странник, спасибо!", 1, (0, 0, 0)), (10, 105))]


class ConfigError(KeyError): pass


class Config:
    """ A utility for configuration """

    def __init__(self, options, *look_for):
        assertions = []
        for key in look_for:
            if key[0] in options.keys():
                exec('self.' + key[0] + ' = options[\'' + key[0] + '\']')
            else:
                exec('self.' + key[0] + ' = ' + key[1])
            assertions.append(key[0])
        for key in options.keys():
            if key not in assertions: raise ConfigError(
                key + ' not expected as option')


class Input:
    """ A text input for pg apps """

    def __init__(self, **options):
        """ Options: x, y, font, color, restricted, maxlength, prompt """
        self.options = Config(options, ['x', '0'], ['y', '0'],
                              ['font', 'pg.font.Font(None, 32)'],
                              ['color', '(0,0,0)'], ['restricted',
                                                     '\'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789!"#$%&\\\'()*+,-./:;<=>?@[\]^_`{|}~\''],
                              ['maxlength', '-1'], ['prompt', '\'\''])
        self.x = self.options.x;
        self.y = self.options.y
        self.font = self.options.font
        self.color = self.options.color
        self.restricted = self.options.restricted
        self.maxlength = self.options.maxlength
        self.prompt = self.options.prompt;
        self.value = ''
        self.shifted = False

    def set_pos(self, x, y):
        """ Set the position to x, y """
        self.x = x
        self.y = y

    def set_font(self, font):
        """ Set the font for the input """
        self.font = font

    def draw(self, surface):
        """ Draw the text input to a surface """
        text = self.font.render(self.prompt + self.value, 1, self.color)
        surface.blit(text, (self.x, self.y))

    def update(self, events):
        """ Update the input based on passed events """
        for event in events:
            if event.type == KEYUP:
                if event.key == K_LSHIFT or event.key == K_RSHIFT: self.shifted = False
            if event.type == KEYDOWN:
                if event.key == K_BACKSPACE:
                    self.value = self.value[:-1]
                elif event.key == K_LSHIFT or event.key == K_RSHIFT:
                    self.shifted = True
                elif event.key == K_SPACE:
                    self.value += ' '
                if not self.shifted:
                    if event.key == K_a and 'a' in self.restricted:
                        self.value += 'a'
                    elif event.key == K_b and 'b' in self.restricted:
                        self.value += 'b'
                    elif event.key == K_c and 'c' in self.restricted:
                        self.value += 'c'
                    elif event.key == K_d and 'd' in self.restricted:
                        self.value += 'd'
                    elif event.key == K_e and 'e' in self.restricted:
                        self.value += 'e'
                    elif event.key == K_f and 'f' in self.restricted:
                        self.value += 'f'
                    elif event.key == K_g and 'g' in self.restricted:
                        self.value += 'g'
                    elif event.key == K_h and 'h' in self.restricted:
                        self.value += 'h'
                    elif event.key == K_i and 'i' in self.restricted:
                        self.value += 'i'
                    elif event.key == K_j and 'j' in self.restricted:
                        self.value += 'j'
                    elif event.key == K_k and 'k' in self.restricted:
                        self.value += 'k'
                    elif event.key == K_l and 'l' in self.restricted:
                        self.value += 'l'
                    elif event.key == K_m and 'm' in self.restricted:
                        self.value += 'm'
                    elif event.key == K_n and 'n' in self.restricted:
                        self.value += 'n'
                    elif event.key == K_o and 'o' in self.restricted:
                        self.value += 'o'
                    elif event.key == K_p and 'p' in self.restricted:
                        self.value += 'p'
                    elif event.key == K_q and 'q' in self.restricted:
                        self.value += 'q'
                    elif event.key == K_r and 'r' in self.restricted:
                        self.value += 'r'
                    elif event.key == K_s and 's' in self.restricted:
                        self.value += 's'
                    elif event.key == K_t and 't' in self.restricted:
                        self.value += 't'
                    elif event.key == K_u and 'u' in self.restricted:
                        self.value += 'u'
                    elif event.key == K_v and 'v' in self.restricted:
                        self.value += 'v'
                    elif event.key == K_w and 'w' in self.restricted:
                        self.value += 'w'
                    elif event.key == K_x and 'x' in self.restricted:
                        self.value += 'x'
                    elif event.key == K_y and 'y' in self.restricted:
                        self.value += 'y'
                    elif event.key == K_z and 'z' in self.restricted:
                        self.value += 'z'
                    elif event.key == K_0 and '0' in self.restricted:
                        self.value += '0'
                    elif event.key == K_1 and '1' in self.restricted:
                        self.value += '1'
                    elif event.key == K_2 and '2' in self.restricted:
                        self.value += '2'
                    elif event.key == K_3 and '3' in self.restricted:
                        self.value += '3'
                    elif event.key == K_4 and '4' in self.restricted:
                        self.value += '4'
                    elif event.key == K_5 and '5' in self.restricted:
                        self.value += '5'
                    elif event.key == K_6 and '6' in self.restricted:
                        self.value += '6'
                    elif event.key == K_7 and '7' in self.restricted:
                        self.value += '7'
                    elif event.key == K_8 and '8' in self.restricted:
                        self.value += '8'
                    elif event.key == K_9 and '9' in self.restricted:
                        self.value += '9'
                    elif event.key == K_BACKQUOTE and '`' in self.restricted:
                        self.value += '`'
                    elif event.key == K_MINUS and '-' in self.restricted:
                        self.value += '-'
                    elif event.key == K_EQUALS and '=' in self.restricted:
                        self.value += '='
                    elif event.key == K_LEFTBRACKET and '[' in self.restricted:
                        self.value += '['
                    elif event.key == K_RIGHTBRACKET and ']' in self.restricted:
                        self.value += ']'
                    elif event.key == K_BACKSLASH and '\\' in self.restricted:
                        self.value += '\\'
                    elif event.key == K_SEMICOLON and ';' in self.restricted:
                        self.value += ';'
                    elif event.key == K_QUOTE and '\'' in self.restricted:
                        self.value += '\''
                    elif event.key == K_COMMA and ',' in self.restricted:
                        self.value += ','
                    elif event.key == K_PERIOD and '.' in self.restricted:
                        self.value += '.'
                    elif event.key == K_SLASH and '/' in self.restricted:
                        self.value += '/'
                elif self.shifted:
                    if event.key == K_a and 'A' in self.restricted:
                        self.value += 'A'
                    elif event.key == K_b and 'B' in self.restricted:
                        self.value += 'B'
                    elif event.key == K_c and 'C' in self.restricted:
                        self.value += 'C'
                    elif event.key == K_d and 'D' in self.restricted:
                        self.value += 'D'
                    elif event.key == K_e and 'E' in self.restricted:
                        self.value += 'E'
                    elif event.key == K_f and 'F' in self.restricted:
                        self.value += 'F'
                    elif event.key == K_g and 'G' in self.restricted:
                        self.value += 'G'
                    elif event.key == K_h and 'H' in self.restricted:
                        self.value += 'H'
                    elif event.key == K_i and 'I' in self.restricted:
                        self.value += 'I'
                    elif event.key == K_j and 'J' in self.restricted:
                        self.value += 'J'
                    elif event.key == K_k and 'K' in self.restricted:
                        self.value += 'K'
                    elif event.key == K_l and 'L' in self.restricted:
                        self.value += 'L'
                    elif event.key == K_m and 'M' in self.restricted:
                        self.value += 'M'
                    elif event.key == K_n and 'N' in self.restricted:
                        self.value += 'N'
                    elif event.key == K_o and 'O' in self.restricted:
                        self.value += 'O'
                    elif event.key == K_p and 'P' in self.restricted:
                        self.value += 'P'
                    elif event.key == K_q and 'Q' in self.restricted:
                        self.value += 'Q'
                    elif event.key == K_r and 'R' in self.restricted:
                        self.value += 'R'
                    elif event.key == K_s and 'S' in self.restricted:
                        self.value += 'S'
                    elif event.key == K_t and 'T' in self.restricted:
                        self.value += 'T'
                    elif event.key == K_u and 'U' in self.restricted:
                        self.value += 'U'
                    elif event.key == K_v and 'V' in self.restricted:
                        self.value += 'V'
                    elif event.key == K_w and 'W' in self.restricted:
                        self.value += 'W'
                    elif event.key == K_x and 'X' in self.restricted:
                        self.value += 'X'
                    elif event.key == K_y and 'Y' in self.restricted:
                        self.value += 'Y'
                    elif event.key == K_z and 'Z' in self.restricted:
                        self.value += 'Z'
                    elif event.key == K_0 and ')' in self.restricted:
                        self.value += ')'
                    elif event.key == K_1 and '!' in self.restricted:
                        self.value += '!'
                    elif event.key == K_2 and '@' in self.restricted:
                        self.value += '@'
                    elif event.key == K_3 and '#' in self.restricted:
                        self.value += '#'
                    elif event.key == K_4 and '$' in self.restricted:
                        self.value += '$'
                    elif event.key == K_5 and '%' in self.restricted:
                        self.value += '%'
                    elif event.key == K_6 and '^' in self.restricted:
                        self.value += '^'
                    elif event.key == K_7 and '&' in self.restricted:
                        self.value += '&'
                    elif event.key == K_8 and '*' in self.restricted:
                        self.value += '*'
                    elif event.key == K_9 and '(' in self.restricted:
                        self.value += '('
                    elif event.key == K_BACKQUOTE and '~' in self.restricted:
                        self.value += '~'
                    elif event.key == K_MINUS and '_' in self.restricted:
                        self.value += '_'
                    elif event.key == K_EQUALS and '+' in self.restricted:
                        self.value += '+'
                    elif event.key == K_LEFTBRACKET and '{' in self.restricted:
                        self.value += '{'
                    elif event.key == K_RIGHTBRACKET and '}' in self.restricted:
                        self.value += '}'
                    elif event.key == K_BACKSLASH and '|' in self.restricted:
                        self.value += '|'
                    elif event.key == K_SEMICOLON and ':' in self.restricted:
                        self.value += ':'
                    elif event.key == K_QUOTE and '"' in self.restricted:
                        self.value += '"'
                    elif event.key == K_COMMA and '<' in self.restricted:
                        self.value += '<'
                    elif event.key == K_PERIOD and '>' in self.restricted:
                        self.value += '>'
                    elif event.key == K_SLASH and '?' in self.restricted:
                        self.value += '?'

        if len(
                self.value) > self.maxlength and self.maxlength >= 0: self.value = self.value[
                                                                                   :-1]


class ChooseCharacter:
    def __init__(self, choosed=0):
        pygame.init()

        pygame.mouse.set_visible(False)

        self.screen = pygame.display.set_mode((1000, 600))

        self.font = pygame.font.Font('fonts/freesansbold.ttf', 30)

        self.choosed = choosed
        self.pushed = None

        self.set_interface()

        running = True
        while running:
            self.events = pygame.event.get()
            for event in self.events:
                if event.type == pygame.QUIT:
                    self.pushed = 'exit'
                    running = False
                if event.type == pygame.MOUSEBUTTONDOWN:
                    for i in range(len(self.chooseButtons)):
                        if self.chooseButtons[i].collidepoint(event.pos):
                            self.choosed = i
                        elif self.back.collidepoint(*event.pos):
                            self.pushed = self.back
                            running = False
                        elif self.start.collidepoint(*event.pos):
                            self.pushed = self.start
                            self.textbox.update(self.events)
                            self.nick = self.textbox.value
                            running = False
                if event.type == pygame.KEYDOWN:
                    print(event.key)
                    if event.key == 13:
                        self.pushed = self.start
                        self.textbox.update(self.events)
                        self.nick = self.textbox.value

            self.render()

            pygame.display.flip()

    def render(self):
        # ФОН
        self.screen.blit(self.background_surf, self.background_rect)

        # ПОЛЕ ВВОДА НИКА
        pygame.draw.rect(self.screen, (250, 175, 255),
                         pygame.Rect(640, 150, 250, 43))
        pygame.draw.rect(self.screen, (0, 0, 0),
                         pygame.Rect(640, 150, 250, 43), 2)
        self.textbox.update(self.events)
        self.textbox.draw(self.screen)

        # НАЗАД
        pygame.draw.rect(self.screen, (250, 175, 255), self.back)
        pygame.draw.rect(self.screen, (0, 0, 0), self.back, 2)
        self.screen.blit(self.text_back, (self.text_x_1, self.text_y_1))

        # ПЕРСОНАЖИ
        i = 0
        for y in range(150, 301, 150):
            for x in range(50, 351, 150):
                i += 1
                pygame.draw.rect(self.screen, pygame.Color('black'),
                                 pygame.Rect(x, y, 100, 100), 2)

                if self.choosed == i - 1:
                    pygame.draw.rect(self.screen, pygame.Color('red'),
                                     pygame.Rect(x, y, 100, 100), 2)

                character = self.characters[i - 1]
                self.screen.blit(character, (x + 2, y + 2))

        # СТАРТ
        pygame.draw.rect(self.screen, (250, 175, 255), self.start)
        pygame.draw.rect(self.screen, (0, 0, 0), self.start, 2)

        # НАДПИСИ
        self.screen.blit(self.text_start, (self.text_x_2, self.text_y_2))
        self.screen.blit(self.text_view, (self.text_x_3, self.text_y_3))
        self.screen.blit(self.text_name, (self.text_x_4, self.text_y_4))

        # КУРСОР
        pos = pygame.mouse.get_pos()
        rect = self.cursor.get_rect(topleft=pos)
        self.screen.blit(self.cursor, rect)

    def set_interface(self):
        directory = os.getcwd()

        # LOAD BACKGROUND
        self.background_surf = pygame.image.load(
            directory + '/backgrounds/quizFone.png')
        self.background_surf = pygame.transform.scale(self.background_surf,
                                                      (1000, 600))
        self.background_rect = self.background_surf.get_rect(
            bottomright=(1000, 600))
        self.screen.blit(self.background_surf, self.background_rect)

        # КУРСОР
        self.cursor = pygame.image.load('sprites/ForGUI/cursor1.png')

        # ПОЛЕ ДЛЯ ВВОДА НИКА
        self.textbox = Input(maxlength=10, color=(0, 0, 0), prompt='',
                             font=self.font)
        self.textbox.set_pos(655, 155)

        # BUTTON BACK
        self.back = pygame.Rect(50, 515, 200, 35)
        self.text_back = self.font.render("Назад", 1, (100, 25, 100))
        self.text_x_1, self.text_y_1 = 150 - self.text_back.get_width() // 2, 550 - self.text_back.get_height()

        # ОКНА ПЕРСОНАЖЕЙ
        self.chooseButtons, self.characters = [], []
        i = 0
        for y in range(150, 301, 150):
            for x in range(50, 351, 150):
                i += 1

                self.chooseButtons.append(pygame.Rect(x, y, 100, 100))

                character = pygame.image.load(
                    'sprites/characters/' + str(i) + '.png')
                self.characters.append(
                    pygame.transform.scale(character, (97, 97)))

        # КНОПКА СТАРТА
        self.start = pygame.Rect(750, 515, 200, 35)
        self.text_start = self.font.render("Старт", 1, (100, 25, 100))
        self.text_x_2, self.text_y_2 = 850 - self.text_start.get_width() // 2, 550 - self.text_start.get_height()

        # НАДПИСИ
        self.text_view = self.font.render("Выберите персонажа", 1,
                                          (100, 25, 100))
        self.text_x_3, self.text_y_3 = 65, 60

        self.text_name = self.font.render("Введите имя", 1, (100, 25, 100))
        self.text_x_4, self.text_y_4 = 665, 60


class Egg:
    def __init__(self, screen, img_path, sound_path):
        self.screen = screen

        self.surf = pygame.image.load(img_path)
        self.rect = self.surf.get_rect(bottomright=(1000, 600))

        self.directory = os.getcwd()
        pygame.mixer.music.load(sound_path)
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
                if event.type == pygame.QUIT:
                    stop = True
                    self.pushed = 'exit'
            if stop:
                pygame.mixer.music.load(self.directory + '/sounds/radio/1.mp3')
                pygame.mixer.music.play(-1)
                pygame.mixer.music.set_volume(1)
                break

            end = time.monotonic()

            self.render()

            pygame.display.flip()

    def render(self):
        self.screen.blit(self.surf, self.rect)


class Pause:
    def __init__(self, screen, game):
        pygame.init()

        self.screen = screen
        self.surface = pygame.Surface((200, 180), pygame.SRCALPHA)

        self.game = game

        pygame.mouse.set_visible(False)

        self.pushed = None

        self.font = pygame.font.Font('fonts/freesansbold.ttf', 25)

        self.set_interface()

        running = True
        while running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.pushed = self.quit
                    running = False
                if event.type == pygame.MOUSEBUTTONDOWN:
                    x, y = event.pos
                    if self.start.collidepoint(x - 400, y - 200):
                        running = False
                    elif self.quit.collidepoint(x - 400, y - 200):
                        self.pushed = self.quit
                        running = False

            self.render()

            pygame.display.flip()

    def set_interface(self):
        # ПРОДОЛЖИТЬ
        self.start = pygame.Rect(5, 65, 190, 35)
        self.text_start = self.font.render("Продолжить", 1, (100, 25, 100))
        self.text_x_1, self.text_y_1 = 100 - self.text_start.get_width() // 2, 100 - self.text_start.get_height()

        # ВЫХОД
        self.quit = pygame.Rect(5, 120, 190, 35)
        self.text_quit = self.font.render("Выход", 1, (100, 25, 100))
        self.text_x_2, self.text_y_2 = 100 - self.text_quit.get_width() // 2, 155 - self.text_quit.get_height()

        # НАДПИСЬ ПАУЗА
        self.inf = self.font.render("ПАУЗА", 2, (0, 0, 0))
        self.text_x_3, self.text_y_3 = 100 - self.inf.get_width() // 2, 50 - self.inf.get_height()

        # РАМКА
        self.win = pygame.Rect(0, 0, 199, 179)

        # КУРСОР
        self.cursor = pygame.image.load('sprites/ForGUI/cursor1.png')

    def render(self):
        self.game.render()

        self.surface.fill((200, 220, 190))

        pygame.draw.rect(self.surface, (250, 175, 255), self.start)
        pygame.draw.rect(self.surface, (0, 0, 0), self.start, 2)
        self.surface.blit(self.text_start, (self.text_x_1, self.text_y_1))

        pygame.draw.rect(self.surface, (250, 175, 255), self.quit)
        pygame.draw.rect(self.surface, (0, 0, 0), self.quit, 2)
        self.surface.blit(self.text_quit, (self.text_x_2, self.text_y_2))

        pygame.draw.rect(self.surface, (0, 0, 0), self.win, 2)

        self.surface.blit(self.inf, (self.text_x_3, self.text_y_3))

        self.screen.blit(self.surface, (400, 200))

        pos = pygame.mouse.get_pos()
        rect = self.cursor.get_rect(topleft=pos)
        self.screen.blit(self.cursor, rect)


field = [
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
     0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
     0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
     0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
     0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
     0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
     0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
     0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
     0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
     0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
     0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
     0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
     0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
     0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
     0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
     0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
     0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 0, 0,
     0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
     0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 0, 0,
     0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
     0],
    [0, 0, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
     0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 0, 0,
     0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
     0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 0, 0,
     0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
     0],
    [0, 0, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
     0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 0, 0,
     0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 0, 0, 0, 0, 0,
     0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 0, 0,
     0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 0, 0, 0,
     0],
    [0, 0, 1, 1, 1, 1, 0, 0, 0, 0, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
     0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 0, 0,
     0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 0, 0, 0, 0, 0,
     0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
     0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1,
     0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
     0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 0, 0,
     0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 0, 0, 0, 0, 0,
     0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 0, 0,
     0, 0, 0, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1,
     0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
     0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
     0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 0, 0, 0, 0, 0,
     0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 0, 0,
     0, 0, 0, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 0, 1, 1, 1, 1, 1, 1, 1,
     0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
     0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
     0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 0, 0, 0, 0, 0,
     0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 0, 0,
     0, 0, 0, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 0, 1, 1, 1, 1, 1, 1, 1,
     0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
     0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
     0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
     0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 0,
     0, 0, 0, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 0, 1, 1, 1, 1, 1, 1, 1,
     0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1,
     1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1,
     1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
     0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 0,
     0, 0, 0, 1, 1, 1, 1, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 0, 1, 1, 1, 1, 1, 1, 1,
     0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1,
     1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1,
     1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
     0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1,
     0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 0, 1, 1, 1, 1, 1, 1, 1,
     0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
     0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
     0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
     0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1,
     1, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1,
     0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1,
     1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1,
     1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
     0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1,
     1, 1, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1,
     0],
    [0, 0, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1,
     1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1,
     1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
     0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1,
     1, 1, 1, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1,
     0],
    [0, 0, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 1, 1, 0, 0, 0, 0, 0, 0, 0,
     0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
     0, 0, 0, 0, 0, 0, 0, 1, 0, 1, 0, 0, 1, 0, 0, 0, 0, 0, 0, 1, 1, 1, 0, 0, 0,
     0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1,
     1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1,
     0],
    [0, 0, 1, 1, 1, 1, 1, 1, 1, 0, 0, 0, 1, 0, 0, 0, 1, 1, 0, 0, 0, 0, 0, 0, 0,
     0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
     0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 1, 0, 1, 0, 0, 0, 0, 0, 0, 1, 1, 1, 0, 0, 0,
     0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1,
     1, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1,
     0],
    [0, 0, 1, 0, 0, 1, 1, 1, 1, 0, 0, 0, 1, 0, 0, 1, 0, 1, 0, 0, 0, 0, 0, 0, 0,
     0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
     0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 0, 0, 0,
     0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
     1, 1, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1,
     0],
    [0, 0, 1, 0, 0, 1, 1, 1, 1, 0, 0, 0, 1, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0,
     0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
     0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 0, 0, 0,
     0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
     0, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1,
     0],
    [0, 0, 1, 0, 0, 1, 1, 1, 1, 0, 0, 0, 1, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0,
     0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
     0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 0, 0, 0,
     0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
     0, 0, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1,
     0],
    [0, 0, 0, 0, 0, 1, 1, 1, 1, 0, 0, 0, 1, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0,
     0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
     0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
     0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
     0, 0, 0, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1,
     0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0,
     0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
     0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
     0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 0,
     0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0, 0, 1, 1, 1, 1, 0, 0, 0, 1, 1, 1,
     0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 1, 0, 0, 1, 1, 1, 0, 0, 0, 0,
     0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1,
     1, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
     0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 0,
     0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0, 1, 1, 1, 1, 0, 0, 0, 1, 1, 1,
     0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 1, 0, 0, 1, 1, 1, 0, 0, 0, 0,
     0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1,
     1, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
     0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 0,
     0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 0, 0, 0, 0, 1, 1, 1, 1, 0, 0, 0, 1, 1, 1,
     0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 1, 0, 0, 1, 1, 1, 0, 0, 0, 0,
     0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1,
     1, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
     0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 0,
     0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 0, 0, 0, 1, 1, 1, 1, 0, 0, 0, 1, 1, 1,
     0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 1, 0, 0, 1, 1, 1, 0, 0, 0, 0,
     0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1,
     1, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
     0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 0,
     0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 0, 0, 1, 1, 1, 1, 0, 0, 0, 1, 1, 1,
     0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 1, 0, 0, 1, 1, 1, 0, 0, 0, 0,
     0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1,
     1, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
     0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
     0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1,
     0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0,
     0, 0, 0, 0, 1, 1, 1, 1, 0, 0, 0, 0, 0,
     0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 0, 1, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0,
     0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
     0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1,
     0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0,
     0, 0, 0, 0, 1, 1, 1, 1, 0, 0, 0, 0, 0,
     0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 0, 1, 1, 1, 1, 1, 0, 0, 0, 0, 0, 1, 1, 0,
     0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
     1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 1, 1, 1,
     0],
    [0, 0, 0, 0, 1, 1, 1, 1, 0, 0, 0, 0, 1, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0,
     0, 0, 0, 0, 1, 1, 1, 1, 0, 0, 0, 0, 0,
     0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 0, 1, 0, 1, 1, 1, 0, 0, 0, 0, 0, 0, 1, 0,
     0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
     1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0, 0, 1, 1, 1,
     0],
    [0, 0, 0, 0, 1, 1, 1, 1, 0, 0, 0, 0, 1, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0,
     0, 0, 0, 0, 1, 1, 1, 1, 0, 0, 0, 0, 0,
     0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 0, 1, 0, 0, 1, 1, 0, 0, 0, 0, 0, 0, 1, 0,
     0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
     1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0, 1, 1, 1,
     0],
    [0, 0, 0, 0, 1, 1, 1, 1, 0, 0, 0, 0, 1, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0,
     0, 0, 0, 0, 1, 1, 1, 1, 0, 0, 0, 0, 0,
     0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 0, 0, 0, 0, 1, 1, 0, 0, 0, 0, 0, 0, 1, 0,
     0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
     1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 0, 0, 0, 1, 1, 1,
     0],
    [0, 0, 0, 0, 1, 1, 1, 1, 0, 0, 0, 0, 1, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0,
     0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
     0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0,
     0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
     1, 1, 1, 1, 0, 0, 1, 1, 1, 1, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 0, 0, 1, 1, 1,
     0],
    [0, 0, 0, 0, 1, 1, 1, 1, 0, 0, 0, 0, 1, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0,
     0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
     0, 0, 0, 0, 0, 0, 0, 1, 1, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0,
     0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
     0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1,
     0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0,
     0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
     0, 0, 0, 0, 0, 0, 0, 1, 1, 0, 1, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0,
     0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
     0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1,
     0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0,
     0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
     1, 0, 0, 0, 0, 0, 0, 1, 1, 0, 1, 0, 0, 0, 0, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0,
     0, 0, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0,
     0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1,
     0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0,
     0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1,
     1, 1, 0, 0, 0, 0, 0, 1, 1, 0, 1, 0, 0, 0, 0, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0,
     0, 0, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0,
     0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1,
     0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 1, 1, 0, 0, 0, 0, 1, 1, 1, 1,
     0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1,
     1, 1, 0, 0, 0, 0, 0, 1, 1, 0, 1, 0, 0, 0, 0, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0,
     0, 0, 1, 1, 1, 1, 0, 0, 0, 1, 1, 1, 1,
     0, 0, 0, 0, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1,
     0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 1, 1, 0, 0, 0, 0, 1, 1, 1, 1,
     0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1,
     1, 1, 0, 0, 0, 0, 0, 1, 1, 0, 1, 0, 0, 0, 0, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0,
     0, 0, 1, 1, 1, 1, 0, 0, 0, 1, 1, 1, 1,
     0, 0, 0, 0, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 0, 0, 1, 1, 1,
     0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 1, 1, 1, 1, 0, 0, 1, 1, 1, 1,
     0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1,
     1, 1, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0,
     0, 0, 1, 1, 1, 1, 0, 0, 0, 1, 1, 1, 1,
     0, 0, 0, 0, 1, 1, 1, 1, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 0, 0, 0, 1, 1, 1,
     0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 1, 1, 1, 1, 0, 1, 1, 1, 1,
     0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
     0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1,
     1, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1,
     0, 0, 0, 0, 1, 1, 1, 1, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0, 1, 1, 1,
     0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1,
     0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
     0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1,
     1, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1,
     0, 0, 0, 0, 1, 1, 1, 1, 0, 0, 1, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0, 0, 1, 1, 1,
     0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 1, 1, 1, 0, 0, 0, 0,
     0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
     0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1,
     1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
     0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1,
     0],
    [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1,
     1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0,
     0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1,
     1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
     0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1,
     0],
    [1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1,
     1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0,
     0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1,
     1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
     0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1,
     0],
    [1, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
     0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0,
     0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
     0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1,
     1, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1,
     0],
    [0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 0, 1, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1,
     1, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0,
     0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
     0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1,
     1, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1,
     0],
    [0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
     0, 0, 0, 0, 0, 1, 1, 0, 0, 0, 0, 0, 0,
     0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
     0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1,
     1, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1,
     0],
    [0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
     0, 0, 0, 0, 0, 1, 1, 0, 0, 0, 0, 0, 0,
     0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
     0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1,
     0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1,
     0],
    [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1,
     0, 0, 0, 0, 0, 1, 1, 0, 1, 1, 0, 0, 0,
     0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0,
     0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1,
     0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1,
     0],
    [0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0,
     0, 0, 1, 1, 0, 1, 1, 0, 1, 1, 0, 0, 0,
     0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0,
     0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1,
     0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1,
     0],
    [0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0,
     1, 1, 1, 1, 1, 1, 1, 0, 1, 1, 1, 1, 1,
     1, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0,
     0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1,
     0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1,
     0],
    [0, 0, 0, 0, 0, 0, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0,
     1, 1, 1, 1, 1, 1, 0, 0, 0, 1, 1, 1, 1,
     1, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0,
     0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1,
     1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1,
     0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0,
     1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
     0, 0, 0, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 0, 0, 0, 0, 0, 1, 1, 1,
     1, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1,
     1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1,
     0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 0, 0, 0,
     1, 1, 1, 1, 1, 1, 1, 0, 0, 1, 1, 1, 1,
     1, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1,
     1, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1,
     1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1,
     0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0,
     1, 1, 1, 1, 1, 1, 1, 0, 0, 1, 1, 1, 1,
     1, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1,
     1, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1,
     1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1,
     0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0,
     1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
     0, 0, 0, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1,
     1, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1,
     1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1,
     0],
    [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0,
     1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
     0, 0, 0, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
     0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1,
     1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1,
     0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
     1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
     0, 0, 0, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
     0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1,
     1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1,
     0]]


class Quest1:
    def __init__(self, screen, game, phrases):
        self.screen = screen
        self.surface = pygame.Surface((230, 180), pygame.SRCALPHA)
        self.font = pygame.font.Font("fonts/freesansbold.ttf", 20)
        self.phrases = phrases
        self.pushed = None
        self.game = game

        pygame.mouse.set_visible(False)

        self.set_interface()

        running = True
        while running:
            self.events = pygame.event.get()
            for event in self.events:
                if event.type == pygame.QUIT:
                    self.pushed = 'exit'
                    running = False
                if event.type == pygame.MOUSEBUTTONDOWN:
                    x, y = event.pos
                    if self.close.collidepoint(x - 400, y - 200):
                        running = False
                    elif self.accept.collidepoint(x - 400, y - 200):
                        try:
                            if int(self.textbox.value) == 253:
                                self.pushed = 'valid'
                            else:
                                self.pushed = 'wrong'
                            running = False
                        except ValueError:
                            pass

            self.render()
            pygame.display.flip()

    def set_interface(self):
        self.close = pygame.Rect(115, 140, 100, 30)
        self.close_text = self.font.render("Закрыть", 1, (0, 0, 0))
        self.close_x, self.close_y = 125, 145

        self.accept = pygame.Rect(10, 140, 100, 30)
        self.accept_text = self.font.render("Принять", 1, (0, 0, 0))
        self.accept_x, self.accept_y = 20, 145

        self.input = pygame.Rect(96, 97, 40, 20)
        self.textbox = Input(maxlength=3, color=(0, 0, 0), prompt='',
                             font=self.font)
        self.textbox.set_pos(97, 100)

        self.win = pygame.Rect(0, 0, 229, 179)

        self.cursor = pygame.image.load('sprites/ForGUI/cursor1.png')

    def render(self):
        self.game.render()

        self.surface.fill((200, 220, 190))

        pygame.draw.rect(self.surface, (250, 175, 255), self.input)
        pygame.draw.rect(self.surface, (0, 0, 0), self.input, 2)
        self.textbox.update(self.events)
        self.textbox.draw(self.surface)

        pygame.draw.rect(self.surface, (0, 0, 0), self.win, 2)

        pygame.draw.rect(self.surface, (250, 175, 255), self.close)
        pygame.draw.rect(self.surface, (0, 0, 0), self.close, 2)
        self.surface.blit(self.close_text, (self.close_x, self.close_y))

        pygame.draw.rect(self.surface, (250, 175, 255), self.accept)
        pygame.draw.rect(self.surface, (0, 0, 0), self.accept, 2)
        self.surface.blit(self.accept_text, (self.accept_x, self.accept_y))

        for i in range(len(self.phrases)):
            self.surface.blit(self.phrases[i][0], self.phrases[i][1])

        self.screen.blit(self.surface, (400, 200))

        pos = pygame.mouse.get_pos()
        rect = self.cursor.get_rect(topleft=pos)
        self.screen.blit(self.cursor, rect)


def create_text_for_Quest_1():
    font = pygame.font.Font('fonts/comic.ttf', 19)

    return [(font.render("Введите значение,", 1, (0, 0, 0)), (10, 10)),
            (font.render("3-й ячейки", 1, (0, 0, 0)), (10, 30)),
            (font.render("", 1, (0, 0, 0)), (10, 40)),
            (font.render("КОД: ++>-><>++>+[<<->-]", 1, (0, 0, 0)), (10, 55)),
            (font.render("", 1, (0, 0, 0)), (10, 70)),
            (font.render("", 1, (0, 0, 0)), (10, 85)),
            (font.render("", 1, (0, 0, 0)), (10, 100)),
            (font.render("", 1, (0, 0, 0)), (10, 115))]


class Quest2:
    def __init__(self, screen, game, phrases):
        self.screen = screen
        self.surface = pygame.Surface((230, 240), pygame.SRCALPHA)
        self.font = pygame.font.Font("fonts/freesansbold.ttf", 20)
        self.phrases = phrases
        self.pushed = None
        self.game = game

        pygame.mouse.set_visible(False)

        self.set_interface()

        running = True
        while running:
            self.events = pygame.event.get()
            for event in self.events:
                if event.type == pygame.QUIT:
                    self.pushed = 'exit'
                    running = False
                if event.type == pygame.MOUSEBUTTONDOWN:
                    x, y = event.pos
                    if self.close.collidepoint(x - 400, y - 200):
                        running = False
                    elif self.accept.collidepoint(x - 400, y - 200):
                        if self.textbox.value.lower() == 'nos':
                            self.pushed = 'valid'
                        else:
                            self.pushed = 'wrong'
                        running = False

            self.render()
            pygame.display.flip()

    def set_interface(self):
        self.close = pygame.Rect(115, 200, 100, 30)
        self.close_text = self.font.render("Закрыть", 1, (0, 0, 0))
        self.close_x, self.close_y = 125, 207

        self.accept = pygame.Rect(10, 200, 100, 30)
        self.accept_text = self.font.render("Принять", 1, (0, 0, 0))
        self.accept_x, self.accept_y = 20, 207

        self.input = pygame.Rect(90, 170, 50, 25)
        self.textbox = Input(maxlength=3, color=(0, 0, 0), prompt='',
                             font=self.font)
        self.textbox.set_pos(97, 172)

        self.win = pygame.Rect(0, 0, 229, 239)

        self.cursor = pygame.image.load('sprites/ForGUI/cursor1.png')

    def render(self):
        self.game.render()

        self.surface.fill((200, 220, 190))

        pygame.draw.rect(self.surface, (250, 200, 255), self.input)
        pygame.draw.rect(self.surface, (0, 0, 0), self.input, 2)
        self.textbox.update(self.events)
        self.textbox.draw(self.surface)

        pygame.draw.rect(self.surface, (0, 0, 0), self.win, 2)

        pygame.draw.rect(self.surface, (250, 175, 255), self.close)
        pygame.draw.rect(self.surface, (0, 0, 0), self.close, 2)
        self.surface.blit(self.close_text, (self.close_x, self.close_y))

        pygame.draw.rect(self.surface, (250, 175, 255), self.accept)
        pygame.draw.rect(self.surface, (0, 0, 0), self.accept, 2)
        self.surface.blit(self.accept_text, (self.accept_x, self.accept_y))

        for i in range(len(self.phrases)):
            self.surface.blit(self.phrases[i][0], self.phrases[i][1])

        self.screen.blit(self.surface, (400, 200))

        pos = pygame.mouse.get_pos()
        rect = self.cursor.get_rect(topleft=pos)
        self.screen.blit(self.cursor, rect)


def create_text_for_Quest2():
    font = pygame.font.Font('fonts/comic.ttf', 16)

    return [(font.render("Надписи на латинице:", 1, (0, 0, 0)), (10, 10)),
            (font.render("Вот гора, а у горы", 1, (0, 0, 0)), (10, 40)),
            (font.render("Две глубокие норы.", 1, (0, 0, 0)), (10, 55)),
            (font.render("В этих норах воздух бродит", 1, (0, 0, 0)), (10, 70)),
            (font.render("То заходит, то выходит", 1, (0, 0, 0)), (10, 85)),
            (font.render("ПИШИТЕ ТРАНСЛИТОМ", 1, (0, 0, 0)), (10, 115)),
            (font.render("(вы забыли русские буквы)", 1, (0, 0, 0)), (10, 130))]


class Quest3:
    def __init__(self, screen, game, phrases):
        self.screen = screen
        self.surface = pygame.Surface((230, 240), pygame.SRCALPHA)
        self.font = pygame.font.Font("fonts/freesansbold.ttf", 20)
        self.phrases = phrases
        self.pushed = None
        self.game = game

        pygame.mouse.set_visible(False)

        self.set_interface()

        running = True
        while running:
            self.events = pygame.event.get()
            for event in self.events:
                if event.type == pygame.QUIT:
                    self.pushed = 'exit'
                    running = False
                if event.type == pygame.MOUSEBUTTONDOWN:
                    x, y = event.pos
                    if self.close.collidepoint(x - 400, y - 200):
                        running = False
                    elif self.accept.collidepoint(x - 400, y - 200):
                        if self.textbox.value.lower() == 'mars':
                            self.pushed = 'valid'
                        else:
                            self.pushed = 'wrong'
                        running = False

            self.render()
            pygame.display.flip()

    def set_interface(self):
        self.close = pygame.Rect(115, 200, 100, 30)
        self.close_text = self.font.render("Закрыть", 1, (0, 0, 0))
        self.close_x, self.close_y = 125, 207

        self.accept = pygame.Rect(10, 200, 100, 30)
        self.accept_text = self.font.render("Принять", 1, (0, 0, 0))
        self.accept_x, self.accept_y = 20, 207

        self.input = pygame.Rect(90, 170, 70, 25)
        self.textbox = Input(maxlength=4, color=(0, 0, 0), prompt='',
                             font=self.font)
        self.textbox.set_pos(97, 172)

        self.win = pygame.Rect(0, 0, 229, 239)

        self.cursor = pygame.image.load('sprites/ForGUI/cursor1.png')

    def render(self):
        self.game.render()

        self.surface.fill((200, 220, 190))

        pygame.draw.rect(self.surface, (250, 200, 255), self.input)
        pygame.draw.rect(self.surface, (0, 0, 0), self.input, 2)
        self.textbox.update(self.events)
        self.textbox.draw(self.surface)

        pygame.draw.rect(self.surface, (0, 0, 0), self.win, 2)

        pygame.draw.rect(self.surface, (250, 175, 255), self.close)
        pygame.draw.rect(self.surface, (0, 0, 0), self.close, 2)
        self.surface.blit(self.close_text, (self.close_x, self.close_y))

        pygame.draw.rect(self.surface, (250, 175, 255), self.accept)
        pygame.draw.rect(self.surface, (0, 0, 0), self.accept, 2)
        self.surface.blit(self.accept_text, (self.accept_x, self.accept_y))

        for i in range(len(self.phrases)):
            self.surface.blit(self.phrases[i][0], self.phrases[i][1])

        self.screen.blit(self.surface, (400, 200))

        pos = pygame.mouse.get_pos()
        rect = self.cursor.get_rect(topleft=pos)
        self.screen.blit(self.cursor, rect)


def create_text_for_Quest3():
    font = pygame.font.Font('fonts/comic.ttf', 16)

    return [(font.render("Да! Это он!", 1, (0, 0, 0)), (10, 0)),
            (font.render('Скажи теперь мне', 1, (0, 0, 0)), (10, 15)),
            (font.render("расшифровку этого кода.", 1, (0, 0, 0)), (10, 30))]


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
        mars2 = False
        mars3 = False

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
                        phrases = create_greeting_dialogue1()
                        di = Dialogue(self.screen, self, phrases)
                        if di.pushed == 'exit':
                            running = False
                        phrases = create_greeting_dialogue2()
                        di = Dialogue(self.screen, self, phrases)
                        if di.pushed == 'exit':
                            running = False
                        phrases = create_greeting_dialogue3()
                        di = Dialogue(self.screen, self, phrases)
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
                                phrases = create_dialogue_for_quest1()
                                di = Dialogue(self.screen, self,
                                              phrases)
                                if di.pushed == 'exit':
                                    running = False
                            else:
                                phrases = create_dialogue_for_quest1_3()
                                self.solved3 = True
                                di = Dialogue(self.screen, self,
                                              phrases)
                                if di.pushed == 'exit':
                                    running = False
                                phrases = create_dialogue20()
                                di = Dialogue(self.screen, self,
                                              phrases)
                                if di.pushed == 'exit':
                                    running = False

                        if (y // 36 == 4 and x // 36 == 93) or (
                                y // 36 == 5 and x // 36 == 93):
                            if mars2 and not mars3:
                                phrases = create_text_for_Quest3()
                                di = Quest3(self.screen, self, phrases)
                                if di.pushed == 'exit':
                                    self.pushed = 'exit'
                                    running = False
                                elif di.pushed == 'valid':
                                    mars3 = True
                                elif di.pushed == 'wrong':
                                    phrases = create_wrong_dialogue_for_quests()
                                if not (
                                        di.pushed is None) and di.pushed != 'exit':
                                    di = Dialogue(self.screen, self,
                                                  phrases)
                                    if di.pushed == 'exit':
                                        self.pushed = 'exit'
                                        running = False

                            if mars3:
                                # Когда разгадает шифр
                                phrases = create_dialogue_for_Ilon_4()
                                di = Dialogue(self.screen, self,
                                              phrases)
                                if di.pushed == 'exit':
                                    running = False
                                phrases = create_dialogue_for_Ilon_5()
                                di = Dialogue(self.screen, self,
                                              phrases)
                                if di.pushed == 'exit':
                                    running = False

                            if self.solved3 and not mars1:
                                phrases = create_dialogue21()
                                mars1 = True
                            if not self.solved1 or not self.solved2 or not self.solved3:
                                phrases = create_dialogue22()
                            di = Dialogue(self.screen, self, phrases)
                            if di.pushed == 'exit':
                                running = False

                        if (y // 36 == 4 and x // 36 == 6) or (
                                y // 36 == 5 and x // 36 == 6) or (
                                y // 36 == 6 and x // 36 == 6):
                            if mars1:
                                phrases = create_dialogue_for_Ilon_1()
                                di = Dialogue(self.screen, self,
                                              phrases)
                                if di.pushed == 'exit':
                                    running = False
                                phrases = create_dialogue_for_Ilon_2()
                                di = Dialogue(self.screen, self,
                                              phrases)
                                if di.pushed == 'exit':
                                    running = False
                                mars2 = True

                        if y // 36 == 32 and x // 36 == 83:
                            phrases = create_dialogue22()
                            di = Dialogue(self.screen, self, phrases)
                            if di.pushed == 'exit':
                                running = False
                        if 1130 >= self.winx >= 1030 and 2685 >= self.winy >= 2385 \
                                and not self.solved1:
                            phrases = create_dialogue_for_quest1_2()
                            di = Dialogue(self.screen, self, phrases)
                            if di.pushed == 'exit':
                                self.pushed = 'exit'
                                running = False
                            else:
                                phrases = create_text_for_Quest_1()
                                di = Quest1(self.screen, self, phrases)
                                if di.pushed == 'exit':
                                    self.pushed = 'exit'
                                    running = False
                                elif di.pushed == 'valid':
                                    self.solved1 = True
                                    phrases = create_win_dialogue_for_quest1()
                                elif di.pushed == 'wrong':
                                    phrases = create_wrong_dialogue_for_quests()
                                if not (
                                        di.pushed is None) and di.pushed != 'exit':
                                    di = Dialogue(self.screen, self,
                                                  phrases)
                                    if di.pushed == 'exit':
                                        self.pushed = 'exit'
                                        running = False
                        elif abs(self.npc2_x - 472) < 35 and abs(
                                self.npc2_y - 210) < 35:
                            if not self.solved2:
                                phrases = create_guide_dialogue1()
                                di = Dialogue(self.screen, self,
                                              phrases)
                                if di.pushed == 'exit':
                                    running = False
                            else:
                                if not self.show_info_flower:
                                    self.show_info_flower = True
                                    phrases = create_guide_dialogue2()
                                    di = Dialogue(self.screen, self,
                                                  phrases)
                                    if di.pushed == 'exit':
                                        running = False
                                phrases = create_guide_dialogue3()
                                di = Dialogue(self.screen, self,
                                              phrases)
                                if di.pushed == 'exit':
                                    running = False
                                phrases = create_guide_dialogue4()
                                di = Dialogue(self.screen, self,
                                              phrases)
                                if di.pushed == 'exit':
                                    running = False
                        elif 3737 >= self.winx >= 3507 and 835 >= self.winy >= 780 \
                                and not self.solved2:
                            phrases = create_dialogue_for_quest2()
                            di = Dialogue(self.screen, self, phrases)
                            if di.pushed == 'exit':
                                self.pushed = 'exit'
                                running = False
                            else:
                                phrases = create_text_for_Quest2()
                                di = Quest2(self.screen, self, phrases)
                                if di.pushed == 'exit':
                                    self.pushed = 'exit'
                                    running = False
                                elif di.pushed == 'valid':
                                    self.solved2 = True
                                    phrases = create_win_dialogue_for_quest2()
                                elif di.pushed == 'wrong':
                                    phrases = create_wrong_dialogue_for_quests()
                                if not (
                                        di.pushed is None) and di.pushed != 'exit':
                                    di = Dialogue(self.screen, self,
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

            if 'supergod' in self.textbox.value:
                self.solved1 = True
                self.solved2 = True
                self.solved3 = True
                self.speed = 10

            if 'falls' in self.textbox.value or 'gravity' in self.textbox.value:
                if self.falls:
                    self.eggs += 1
                    Egg(self.screen, self.directory + '/levels/px1.png',
                        self.directory + '/sounds/gravity.mp3')
                    self.textbox.value = ''
                    self.falls = False
                    if self.eggs != self.needEggs:
                        phrases = create_dialogue_for_eggs(
                            self.needEggs - self.eggs)
                        di = Dialogue(self.screen, self, phrases)
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
                        phrases = create_dialogue_for_eggs(
                            self.needEggs - self.eggs)
                        di = Dialogue(self.screen, self, phrases)
                        if di.pushed == 'exit':
                            running = False

            if 'sonic' in self.textbox.value:
                if self.sonic:
                    self.eggs += 1
                    Egg(self.screen, self.directory + '/levels/sonic.jpg',
                        self.directory + '/sounds/sonic.mp3')
                    self.textbox.value = ''
                    self.sonic = False
                    self.speed *= 2
                    if self.eggs != self.needEggs:
                        phrases = create_dialogue_for_eggs(
                            self.needEggs - self.eggs)
                        di = Dialogue(self.screen, self, phrases)
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
                        phrases = create_dialogue_for_eggs(
                            self.needEggs - self.eggs)
                        di = Dialogue(self.screen, self, phrases)
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
                        phrases = create_dialogue_for_eggs(
                            self.needEggs - self.eggs)
                        di = Dialogue(self.screen, self, phrases)
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
                        phrases = create_dialogue_for_eggs(
                            self.needEggs - self.eggs)
                        di = Dialogue(self.screen, self, phrases)
                        if di.pushed == 'exit':
                            running = False

            if self.eggs == self.needEggs and self.solved1 and self.solved2 and self.solved3 and mars3:
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

            if y // 36 == 48 and x // 36 == 13 and not self.music_played:
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
                    phrases = create_dialogue19()
                    di = Dialogue(self.screen, self, phrases)
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

        self.textbox = Input(maxlength=1000, color=(0, 0, 0), prompt='',
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

        pygame.draw.rect(self.screen, (250, 175, 255),
                         pygame.Rect(800, 515, 250, 43))
        pygame.draw.rect(self.screen, (0, 0, 0),
                         pygame.Rect(800, 515, 250, 43), 2)
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


class MainMenu:
    def __init__(self):
        pygame.init()

        self.winWidth = 1000
        self.winHeight = 600
        self.screen = pygame.display.set_mode((self.winWidth, self.winHeight))

        self.pushed = None
        self.y = 100

        self.motionButton = None

        self.directory = os.getcwd()

        pygame.mouse.set_visible(False)

        self.set_interface()
        surf = pygame.image.load('sprites/ForGUI/cursor1.png')

        running = True
        while running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.pushed = self.buttons[-1][1]
                    running = False
                if event.type == pygame.MOUSEBUTTONUP:
                    for i in range(len(self.buttons)):
                        if self.buttons[i][1].collidepoint(event.pos):
                            self.pushed = self.buttons[i][1]
                            running = False
                if event.type == pygame.MOUSEMOTION:
                    for i in range(len(self.buttons)):
                        if self.buttons[i][1].collidepoint(event.pos) and \
                                self.buttons[i][1] != self.motionButton:
                            self.motionButton = self.buttons[i][1]
                            self.i = i
                            self.status = 0
                    if not (self.motionButton is None):
                        if not self.motionButton.collidepoint(event.pos):
                            self.motionButton = None
            self.render()

            rect = surf.get_rect(topleft=pygame.mouse.get_pos())
            self.screen.blit(surf, rect)

            pygame.display.flip()

    def render(self):
        self.screen.blit(self.background_surf, self.background_rect)

        for button in self.buttons:
            if self.motionButton == button[1]:
                self.screen.blit(self.images[self.i][self.status], button[1])
                self.status += 1

                if self.status == 30:
                    self.status = 0
            else:
                self.screen.blit(button[0], button[1])

    def set_interface(self):
        directory = os.getcwd()

        # LOAD BACKGROUND
        self.background_surf = pygame.image.load(
            directory + '/backgrounds/quizFone.png')
        self.background_surf = pygame.transform.scale(self.background_surf,
                                                      (1000, 600))
        self.background_rect = self.background_surf.get_rect(
            bottomright=(1000, 600))

        self.continue_btn = load_image(
            'sprites/ForGUI/Blue buttons/Play blue button 300x80.png')
        self.continue_btn_Rect = self.continue_btn.get_rect(
            bottomright=(355, 205))

        self.options_btn = load_image(
            'sprites/ForGUI/Blue buttons/more blue button 300x80.png')
        self.options_btn_Rect = self.options_btn.get_rect(
            bottomright=(355, 305))

        self.quit_btn = load_image(
            'sprites/ForGUI/Blue buttons/Quit blue button 300x80.png')
        self.quit_btn_Rect = self.quit_btn.get_rect(bottomright=(355, 405))

        self.buttons = [(self.continue_btn, self.continue_btn_Rect),
                        (self.options_btn, self.options_btn_Rect),
                        (self.quit_btn, self.quit_btn_Rect)]

        self.images = [[]]
        for i in range(1, 31):
            self.images[-1].append(load_image(
                self.directory + '/sprites/ForGUI/Blue buttons/play blue button 300x80 hover/' +
                'play button blue 300x80 (' + str(i) + ').png'))

        self.images.append([])
        for i in range(1, 31):
            self.images[-1].append(load_image(
                self.directory + '/sprites/ForGUI\Blue buttons\more blue button 300x80 hover/' +
                'more blue button 300x80 (' + str(i) + ').png'))

        self.images.append([])
        for i in range(1, 31):
            self.images[-1].append(load_image(
                self.directory + '/sprites/ForGUI\Blue buttons\Quit blue button 300x80 hover/' +
                'quit blue button 300x80 (' + str(i) + ').png'))


def load_image(name):
    image = pygame.image.load(name)
    image = pygame.transform.scale(image, (300, 80))

    return image


class Information:
    def __init__(self):
        pygame.init()

        self.screen = pygame.display.set_mode((1000, 600))

        self.font_back = pygame.font.Font('fonts/freesansbold.ttf', 30)
        self.font_rules = pygame.font.Font('fonts/comic.ttf', 22)
        self.font_authors = pygame.font.Font('fonts/comic.ttf', 25)
        self.font_warning = pygame.font.Font('fonts/comic.ttf', 23)
        self.font_tittle1 = pygame.font.Font('fonts/freesansbold.ttf', 45)

        self.pushed = None

        pygame.mouse.set_visible(False)

        self.set_interface()

        running = True
        while running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.pushed = 'exit'
                    running = False
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if self.back.collidepoint(*event.pos):
                        running = False

            self.render()

            pygame.display.flip()

    def set_interface(self):
        directory = os.getcwd()

        # LOAD BACKGROUND
        self.background_surf = pygame.image.load(
            directory + '/backgrounds/quizFone.jpg')
        self.background_surf = pygame.transform.scale(self.background_surf,
                                                      (1000, 600))
        self.background_rect = self.background_surf.get_rect(
            bottomright=(1000, 600))

        # @@@@@@
        self.back = pygame.Rect(50, 515, 200, 35)
        self.text_back = self.font_back.render("Назад", 1, (100, 25, 100))
        self.text_x_1, self.text_y_1 = 150 - self.text_back.get_width() // 2, 550 - self.text_back.get_height()

        # @@@@@@
        self.rules1 = pygame.Rect(100, 45, 260, 60)
        self.text_rules1 = self.font_tittle1.render("Правила", 1, (60, 132, 45))
        self.text_rules1_x, self.text_rules1_y = 135, 54

        self.rules2 = pygame.Rect(50, 150, 360, 300)

        self.text_rules2 = self.font_rules.render("Цель игры заключается в", 1,
                                                  (0, 0, 0))
        self.text_rules2_x, self.text_rules2_y = 65, 150

        self.text_rules3 = self.font_rules.render("том, чтобы исследовать", 1,
                                                  (0, 0, 0))
        self.text_rules3_x, self.text_rules3_y = 65, 200

        self.text_rules4 = self.font_rules.render("карту и находить на ней", 1,
                                                  (0, 0, 0))
        self.text_rules4_x, self.text_rules4_y = 65, 250

        self.text_rules5 = self.font_rules.render(
            "загадки, при решении которых", 1, (0, 0, 0))
        self.text_rules5_x, self.text_rules5_y = 65, 300

        self.text_rules6 = self.font_rules.render("потребуются ваши смекалка и",
                                                  1, (0, 0, 0))
        self.text_rules6_x, self.text_rules6_y = 65, 350

        self.text_rules7 = self.font_rules.render("сообразительность", 1,
                                                  (0, 0, 0))
        self.text_rules7_x, self.text_rules7_y = 65, 400

        # @@@@@@
        self.authors1 = pygame.Rect(672, 420, 150, 40)
        self.text_authors1 = self.font_back.render("Авторы", 1, (60, 132, 45))
        self.text_authors1_x, self.text_authors1_y = 693, 426

        self.authors2 = pygame.Rect(600, 480, 300, 100)

        self.text_authors2 = self.font_authors.render("Дмитрий Кузнецов", 1,
                                                      (0, 0, 0))
        self.text_authors2_x, self.text_authors2_y = 640, 480

        self.text_authors3 = self.font_authors.render("Иван Чебыкин", 1,
                                                      (0, 0, 0))
        self.text_authors3_x, self.text_authors3_y = 640, 510

        self.text_authors4 = self.font_authors.render("Марк Шкут", 1, (0, 0, 0))
        self.text_authors4_x, self.text_authors4_y = 640, 540

        # @@@@@@
        self.warning = pygame.Rect(585, 40, 320, 100)

        self.text_warning1 = self.font_warning.render("ВНИМАНИЕ: В игру", 1,
                                                      (220, 30, 15))
        self.text_warning1_x, self.text_warning1_y = 625, 42

        self.text_warning2 = self.font_warning.render("необходимо играть", 1,
                                                      (220, 30, 15))
        self.text_warning2_x, self.text_warning2_y = 625, 67

        self.text_warning3 = self.font_warning.render("со ВКЛЮЧЕННЫМ звуком", 1,
                                                      (220, 30, 15))
        self.text_warning3_x, self.text_warning3_y = 598, 97

        # КУРСОР
        self.cursor = pygame.image.load('sprites/ForGUI/cursor1.png')

    def render(self):
        self.screen.fill(pygame.Color('white'))

        self.screen.blit(self.background_surf, self.background_rect)

        # НАЗАД
        pygame.draw.rect(self.screen, (250, 175, 255), self.back)
        pygame.draw.rect(self.screen, (0, 0, 0), self.back, 2)
        self.screen.blit(self.text_back, (self.text_x_1, self.text_y_1))

        # ПРАВИЛА
        pygame.draw.rect(self.screen, (250, 175, 255), self.rules1)
        pygame.draw.rect(self.screen, (0, 0, 0), self.rules1, 2)
        self.screen.blit(self.text_rules1,
                         (self.text_rules1_x, self.text_rules1_y))

        pygame.draw.rect(self.screen, (250, 175, 255), self.rules2)
        pygame.draw.rect(self.screen, (0, 0, 0), self.rules2, 2)

        self.screen.blit(self.text_rules2,
                         (self.text_rules2_x, self.text_rules2_y))
        self.screen.blit(self.text_rules3,
                         (self.text_rules3_x, self.text_rules3_y))
        self.screen.blit(self.text_rules4,
                         (self.text_rules4_x, self.text_rules4_y))
        self.screen.blit(self.text_rules5,
                         (self.text_rules5_x, self.text_rules5_y))
        self.screen.blit(self.text_rules6,
                         (self.text_rules6_x, self.text_rules6_y))
        self.screen.blit(self.text_rules7,
                         (self.text_rules7_x, self.text_rules7_y))

        # АВТОРЫ
        pygame.draw.rect(self.screen, (250, 175, 255), self.authors1)
        pygame.draw.rect(self.screen, (0, 0, 0), self.authors1, 2)
        self.screen.blit(self.text_authors1,
                         (self.text_authors1_x, self.text_authors1_y))

        pygame.draw.rect(self.screen, (250, 175, 255), self.authors2)
        pygame.draw.rect(self.screen, (0, 0, 0), self.authors2, 2)

        self.screen.blit(self.text_authors2,
                         (self.text_authors2_x, self.text_authors2_y))
        self.screen.blit(self.text_authors3,
                         (self.text_authors3_x, self.text_authors3_y))
        self.screen.blit(self.text_authors4,
                         (self.text_authors4_x, self.text_authors4_y))

        # СОВЕТ
        pygame.draw.rect(self.screen, (250, 175, 255), self.warning)
        pygame.draw.rect(self.screen, (0, 0, 0), self.warning, 2)
        self.screen.blit(self.text_warning1,
                         (self.text_warning1_x, self.text_warning1_y))
        self.screen.blit(self.text_warning2,
                         (self.text_warning2_x, self.text_warning2_y))
        self.screen.blit(self.text_warning3,
                         (self.text_warning3_x, self.text_warning3_y))

        # КУРСОР
        pos = pygame.mouse.get_pos()
        rect = self.cursor.get_rect(topleft=pos)
        self.screen.blit(self.cursor, rect)


class Greeting:
    def __init__(self):
        pygame.init()

        self.winWidth = 1000
        self.winHeight = 600
        self.screen = pygame.display.set_mode((self.winWidth, self.winHeight))
        self.directory = os.getcwd()

        self.surf = pygame.image.load(self.directory + '/levels/diskleimer.jpg')
        self.rect = self.surf.get_rect(bottomright=(1000, 600))

        self.screen.blit(self.surf, self.rect)
        pygame.mixer.music.load(self.directory + '/sounds/papapa.mp3')
        pygame.mixer.music.play(0)
        pygame.mixer.music.set_volume(1)
        start = time.monotonic()
        end = time.monotonic()
        pygame.display.flip()
        while end - start < 3:
            end = time.monotonic()

        self.x, self.y = 250, 445

        self.pushed = None

        self.set_interface()

        pygame.mouse.set_visible(False)
        surf = pygame.image.load('sprites/ForGUI/cursor1.png')

        push = False
        running = True
        while running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.pushed = 'exit'
                    running = False
                if event.type == pygame.MOUSEBUTTONDOWN:
                    x, y = event.pos
                    if self.coinRect.collidepoint((x, y)):
                        push = True
                        x_, y_ = event.pos[0] - self.x, event.pos[1] - self.y
                if event.type == pygame.MOUSEBUTTONUP:
                    push = False
                if event.type == pygame.MOUSEMOTION and push:
                    self.x, self.y = event.pos
                    self.x -= x_
                    self.y -= y_

            if self.buttons[0].collidepoint((self.x - 25, self.y - 30)):
                self.pushed = self.buttons[0]
                running = False

            self.render()

            pos = pygame.mouse.get_pos()
            rect = surf.get_rect(topleft=pos)
            self.screen.blit(surf, rect)

            pygame.display.flip()

    def render(self):
        self.screen.blit(self.background_surf, self.background_rect)

        pygame.draw.rect(self.screen, (0, 0, 0), self.buttons[0])

        self.screen.blit(self.text, (self.text_x, self.text_y))

        self.screen.blit(self.automat, self.automatRect)

        self.coinRect = self.coin.get_rect(bottomright=(self.x, self.y))
        self.screen.blit(self.coin, self.coinRect)

    def set_interface(self):
        directory = os.getcwd()

        self.background_surf = pygame.image.load(
            directory + '/backgrounds/main.jpg')
        self.background_surf = pygame.transform.scale(self.background_surf,
                                                      (1000, 600))
        self.background_rect = self.background_surf.get_rect(
            bottomright=(1000, 600))

        # LOAD MUSIC
        pygame.mixer.music.load(directory + '/sounds/radio/1.mp3')
        pygame.mixer.music.play(-1)
        pygame.mixer.music.set_volume(1)

        font = pygame.font.Font('fonts/freesansbold.ttf', 30)
        font = pygame.font.Font('fonts/freesansbold.ttf', 30)

        # КНОПКИ И НАДПИСИ
        self.buttons = [pygame.draw.rect(self.screen, (0, 0, 0),
                                         pygame.Rect(624, 392, 90, 40))]
        self.text = font.render('<<<------', 1, (218, 114, 3))
        self.text_x, self.text_y = 795 - self.text.get_width() // 2, 385 + 25 - self.text.get_height() // 2

        # АВТОМАТ
        self.automat = pygame.image.load('sprites/Game_building.jpg')
        self.automat = pygame.transform.scale(self.automat, (280, 70))
        self.automatRect = self.automat.get_rect(bottomright=(720, self.y))

        # МОНЕТКА
        self.coin = pygame.image.load('sprites/coin.png')
        self.coin = pygame.transform.scale(self.coin, (50, 60))
        self.coinRect = self.coin.get_rect(bottomright=(self.x, self.y))


mainWin0 = Greeting()

HEROES = ['1(Townfolk-Child-M-001)', '2(Townfolk-Child-M)',
          '3(Townfolk-Adult-M-006)',
          '4(coriander publish.)', '5(Mushroom-01)', '6(Cultist)']

while True:
    if mainWin0.pushed == pygame.Rect(624, 392, 90, 40):
        mainWin = MainMenu()
        if mainWin.pushed == pygame.Rect(55, 125, 300, 80):  # Продолжить
            chooseChar = ChooseCharacter()
            if chooseChar:
                if chooseChar.pushed == pygame.Rect(50, 515, 201, 36):  # Назад
                    continue
                elif chooseChar.pushed == pygame.Rect(750, 515, 200,
                                                      35):  # Старт
                    hero = HEROES[chooseChar.choosed]
                    gameWin = Game(hero, chooseChar.nick)
                    if gameWin.pushed == 'exit':
                        break
                    elif gameWin.pushed == 'exit_main':
                        input()

                elif chooseChar.pushed == 'exit':
                    break
            else:
                break

        elif mainWin.pushed == pygame.Rect(55, 225, 300, 80):  # Настройки
            inf = Information()
            if inf.pushed == 'exit':
                break
        elif mainWin.pushed == pygame.Rect(55, 325, 300, 80):  # Выход
            break
    elif mainWin0.pushed == 'exit':
        break
