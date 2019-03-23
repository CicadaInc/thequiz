import pygame

import eztext


class Quest:
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
        self.textbox = eztext.Input(maxlength=3, color=(0, 0, 0), prompt='',
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


def create_text():
    font = pygame.font.Font('fonts/comic.ttf', 19)

    return [(font.render("Введите значение,", 1, (0, 0, 0)), (10, 10)),
            (font.render("3-й ячейки", 1, (0, 0, 0)), (10, 30)),
            (font.render("", 1, (0, 0, 0)), (10, 40)),
            (font.render("КОД: ++>-><>++>+[<<->-]", 1, (0, 0, 0)), (10, 55)),
            (font.render("", 1, (0, 0, 0)), (10, 70)),
            (font.render("", 1, (0, 0, 0)), (10, 85)),
            (font.render("", 1, (0, 0, 0)), (10, 100)),
            (font.render("", 1, (0, 0, 0)), (10, 115))]
