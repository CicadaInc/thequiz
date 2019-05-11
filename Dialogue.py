import pygame


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
            (font.render("востоке. Отыщи её и принеси", 1, (0, 0, 0)), (10, 75)),
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