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


def create_dialogue1():
    font = pygame.font.Font('fonts/comic.ttf', 16)

    return [(font.render("Зравствуй, странник.", 1, (0, 0, 0)), (10, 10)),
            (font.render("Мое имя Brainfuck.", 1, (0, 0, 0)), (10, 25)),
            (font.render("Меня прозвали в честь", 1, (0, 0, 0)), (10, 40)),
            (font.render("соимённого ЯП.", 1, (0, 0, 0)), (10, 55)),
            (font.render("Найди компилятор", 1, (0, 0, 0)), (10, 70)),
            (font.render("у водопада", 1, (0, 0, 0)), (10, 85)),
            (font.render("мой верный, и да будет", 1, (0, 0, 0)), (10, 100)),
            (font.render("карма твоя чиста", 1, (0, 0, 0)), (10, 115))]


def create_dialogue2():
    font = pygame.font.Font('fonts/comic.ttf', 16)

    return [(font.render("Вы нашли компилятор,", 1, (0, 0, 0)), (10, 10)),
            (font.render("но все не может быть", 1, (0, 0, 0)), (10, 25)),
            (font.render("так просто - ", 1, (0, 0, 0)), (10, 40)),
            (font.render("компилятор зашифрован", 1, (0, 0, 0)), (10, 55)),
            (font.render("супер кодом и вам", 1, (0, 0, 0)), (10, 70)),
            (font.render("придется решить эту задачу", 1, (0, 0, 0)), (10, 85)),
            (font.render("ибо нефиг", 1, (0, 0, 0)), (10, 100)),]


def create_dialogue3():
    font = pygame.font.Font('fonts/comic.ttf', 20)

    return [(font.render("Хорошая работа ^_^", 1, (0, 0, 0)), (10, 10)),
            (font.render("Карма + 100", 1, (0, 0, 0)), (10, 55)),]


def create_dialogue4():
    font = pygame.font.Font('fonts/comic.ttf', 20)

    return [(font.render("Неверно", 1, (0, 0, 0)), (10, 10)),
            (font.render("Попробуйте еще :(", 1, (0, 0, 0)), (10, 40)),]


def create_dialogue5():
    font = pygame.font.Font('fonts/comic.ttf', 16)

    return [(font.render("Благодарю тебя, странник.", 1, (0, 0, 0)), (10, 10)),
            (font.render("Теперь я могу снова", 1, (0, 0, 0)), (10, 25)),
            (font.render("выносить мозги.", 1, (0, 0, 0)), (10, 40)),
            (font.render("И да будет карма", 1, (0, 0, 0)), (10, 55)),
            (font.render("твоя чиста", 1, (0, 0, 0)), (10, 70))]
def create_dialogue6():
    font = pygame.font.Font('fonts/comic.ttf', 16)
    return [(font.render("Благодарю тебя, странник.", 1, (0, 0, 0)), (10, 10))]
