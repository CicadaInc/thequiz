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


def create_dialogue01():
    font = pygame.font.Font('fonts/comic.ttf', 16)

    return [(font.render("Таки прифетсфую тебя,", 1, (0, 0, 0)), (10, 10)),
            (font.render("молодой челофек.", 1, (0, 0, 0)), (10, 25)),
            (font.render("Добро пошалофать в", 1, (0, 0, 0)), (10, 40)),
            (font.render("Страну Недураков.", 1, (0, 0, 0)), (10, 55)),
            (font.render("Таки если принесешь", 1, (0, 0, 0)), (10, 70)),
            (font.render("мне шейкелей, шо Буратино", 1, (0, 0, 0)), (10, 85)),
            (font.render("у моста на западе зарыл,", 1, (0, 0, 0)), (10, 100)),
            (font.render("то таки узнаешь все про все.", 1, (0, 0, 0)), (10, 115))]


def create_dialogue02():
    font = pygame.font.Font('fonts/comic.ttf', 16)

    return [(font.render("Вы откопали сундук.", 1, (0, 0, 0)), (10, 10)),
            (font.render("Но он закрыт мегасекретным", 1, (0, 0, 0)), (10, 25)),
            (font.render("кодом. Также на сундуке", 1, (0, 0, 0)), (10, 40)),
            (font.render("вы находите надписи", 1, (0, 0, 0)), (10, 55)),
            (font.render("на латинице", 1, (0, 0, 0)), (10, 70)),
            (font.render("(Хорошо, что вы учились", 1, (0, 0, 0)), (10, 85)),
            (font.render("на медфаке, поэтому", 1, (0, 0, 0)), (10, 100)),
            (font.render("сможете их прочитать)", 1, (0, 0, 0)), (10, 115))]


def create_dialogue03():
    font = pygame.font.Font('fonts/comic.ttf', 20)

    return [(font.render("Хорошая работа ^_^", 1, (0, 0, 0)), (10, 10)),
            (font.render("Шейкели + 100", 1, (0, 0, 0)), (10, 40))]


def create_dialogue04():
    font = pygame.font.Font('fonts/comic.ttf', 16)

    return [(font.render("Таки ты не промах,", 1, (0, 0, 0)), (10, 10)),
            (font.render("как я погляжу.", 1, (0, 0, 0)), (10, 25)),
            (font.render("Как и договаривались,", 1, (0, 0, 0)), (10, 40)),
            (font.render("я расскажу тебе", 1, (0, 0, 0)), (10, 55)),
            (font.render("все, что происходит", 1, (0, 0, 0)), (10, 70)),
            (font.render("в нашей чудесной стране.", 1, (0, 0, 0)), (10, 85)),
            (font.render("", 1, (0, 0, 0)), (10, 100)),
            (font.render("ШЕЙКЕЛИ - 100", 1, (0, 0, 0)), (10, 115))]


def create_dialogue05():
    font = pygame.font.Font('fonts/comic.ttf', 16)

    return [(font.render("На калдбище к сеферу", 1, (0, 0, 0)), (10, 10)),
            (font.render("расположено феликое", 1, (0, 0, 0)), (10, 25)),
            (font.render("творение разработчиков.", 1, (0, 0, 0)), (10, 40)),
            (font.render("А на сеферо-западе", 1, (0, 0, 0)), (10, 55)),
            (font.render("кто-то кто-то", 1, (0, 0, 0)), (10, 70)),
            (font.render("кто-то кто-то", 1, (0, 0, 0)), (10, 85)),
            (font.render("кто-то кто-то", 1, (0, 0, 0)), (10, 100)),
            (font.render("кто-то кто-то", 1, (0, 0, 0)), (10, 115))]


def create_dialogue06():
    font = pygame.font.Font('fonts/comic.ttf', 16)

    return [(font.render("Могу сказать, что", 1, (0, 0, 0)), (10, 10)),
            (font.render("тут Майкл Джексон", 1, (0, 0, 0)), (10, 25)),
            (font.render("ф почете. И еще", 1, (0, 0, 0)), (10, 40)),
            (font.render("мы фсе фанатеем от", 1, (0, 0, 0)), (10, 55)),
            (font.render("Гравити Фолз.", 1, (0, 0, 0)), (10, 70)),
            (font.render("Таки это был очень прямой", 1, (0, 0, 0)), (10, 85)),
            (font.render("намек на использование", 1, (0, 0, 0)), (10, 100)),
            (font.render("устройства ввода.", 1, (0, 0, 0)), (10, 115))]


def create_dialogue11():
    font = pygame.font.Font('fonts/comic.ttf', 16)

    return [(font.render("Зравствуй, странник.", 1, (0, 0, 0)), (10, 10)),
            (font.render("Мое имя Brainfuck.", 1, (0, 0, 0)), (10, 25)),
            (font.render("Меня прозвали в честь", 1, (0, 0, 0)), (10, 40)),
            (font.render("одноименного ЯП.", 1, (0, 0, 0)), (10, 55)),
            (font.render("Найди компилятор", 1, (0, 0, 0)), (10, 70)),
            (font.render("у водопада", 1, (0, 0, 0)), (10, 85)),
            (font.render("мой верный, и да будет", 1, (0, 0, 0)), (10, 100)),
            (font.render("карма твоя чиста", 1, (0, 0, 0)), (10, 115))]


def create_dialogue12():
    font = pygame.font.Font('fonts/comic.ttf', 16)

    return [(font.render("Вы нашли компилятор,", 1, (0, 0, 0)), (10, 10)),
            (font.render("но все не может быть", 1, (0, 0, 0)), (10, 25)),
            (font.render("так просто - ", 1, (0, 0, 0)), (10, 40)),
            (font.render("компилятор зашифрован", 1, (0, 0, 0)), (10, 55)),
            (font.render("суперкодом, и вам", 1, (0, 0, 0)), (10, 70)),
            (font.render("придется решить эту задачу", 1, (0, 0, 0)), (10, 85)),
            (font.render("", 1, (0, 0, 0)), (10, 100)), ]


def create_dialogue13():
    font = pygame.font.Font('fonts/comic.ttf', 20)

    return [(font.render("Хорошая работа ^_^", 1, (0, 0, 0)), (10, 10)),
            (font.render("Карма + 100", 1, (0, 0, 0)), (10, 55)), ]


def create_dialogue14():
    font = pygame.font.Font('fonts/comic.ttf', 20)

    return [(font.render("Неверно", 1, (0, 0, 0)), (10, 10)),
            (font.render("Попробуйте еще :(", 1, (0, 0, 0)), (10, 40)), ]


def create_dialogue15():
    font = pygame.font.Font('fonts/comic.ttf', 16)

    return [(font.render("Благодарю тебя, странник.", 1, (0, 0, 0)), (10, 10)),
            (font.render("Теперь я могу снова", 1, (0, 0, 0)), (10, 25)),
            (font.render("выносить мозги.", 1, (0, 0, 0)), (10, 40)),
            (font.render("И да будет карма", 1, (0, 0, 0)), (10, 55)),
            (font.render("твоя чиста", 1, (0, 0, 0)), (10, 70))]
