import pygame
import os


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

        #ВЫХОД
        self.quit = pygame.Rect(5, 120, 190, 35)
        self.text_quit = self.font.render("Выход", 1, (100, 25, 100))
        self.text_x_2, self.text_y_2 = 100 - self.text_quit.get_width() // 2, 155 - self.text_quit.get_height()

        #НАДПИСЬ ПАУЗА
        self.inf = self.font.render("ПАУЗА", 2, (0, 0, 0))
        self.text_x_3, self.text_y_3 = 100 - self.inf.get_width() // 2, 50 - self.inf.get_height()

        #РАМКА
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
