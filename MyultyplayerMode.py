import pygame
import os


class MyultyplayerMode:
    def __init__(self):
        pygame.init()

        self.winWidth = 1000
        self.winHeight = 600
        self.screen = pygame.display.set_mode((self.winWidth, self.winHeight))

        # LOAD BACKGROUND
        directory = os.getcwd()
        BACKGROUND_SURF = pygame.image.load(directory + '/backgrounds/main.jpg')
        BACKGROUND_SURF = pygame.transform.scale(BACKGROUND_SURF, (1000, 600))
        BACKGROUND_RECT = BACKGROUND_SURF.get_rect(bottomright=(1000, 600))
        self.screen.blit(BACKGROUND_SURF, BACKGROUND_RECT)

        self.font = pygame.font.Font(None, 50)

        text_view = self.font.render("Выберите персонажа", 1, (100, 25, 100))
        text_view_x, text_view_y = 65, 60
        self.screen.blit(text_view, (text_view_x, text_view_y))

        text_name = self.font.render("Введите имя", 1, (100, 25, 100))
        text_name_x, text_name_y = 665, 60
        self.screen.blit(text_name, (text_name_x, text_name_y))

        running = True
        while running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if self.chooseWin1.collidepoint(event.pos):
                        self.pushed = self.chooseWin1
                        running = False
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if self.chooseWin2.collidepoint(event.pos):
                        self.pushed = self.chooseWin2
                        running = False
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if self.chooseWin3.collidepoint(event.pos):
                        self.pushed = self.chooseWin3
                        running = False
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if self.chooseWin4.collidepoint(event.pos):
                        self.pushed = self.chooseWin4
                        running = False
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if self.chooseWin5.collidepoint(event.pos):
                        self.pushed = self.chooseWin5
                        running = False
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if self.chooseWin6.collidepoint(event.pos):
                        self.pushed = self.chooseWin6
                        running = False
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if self.chooseWin7.collidepoint(event.pos):
                        self.pushed = self.chooseWin7
                        running = False
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if self.chooseWin8.collidepoint(event.pos):
                        self.pushed = self.chooseWin8
                        running = False
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if self.chooseWin9.collidepoint(event.pos):
                        self.pushed = self.chooseWin9
                        running = False

            self.render()

            pygame.display.flip()

    def render(self):
        self.draw_win1()
        self.draw_win2()
        self.draw_win3()
        self.draw_win4()
        self.draw_win5()
        self.draw_win6()
        self.draw_win7()
        self.draw_win8()
        self.draw_win9()

    def draw_win1(self):
        self.backgroundbutton1 = pygame.draw.rect(self.screen, (250, 175, 255),
                                                  pygame.Rect(50, 150, 100, 100))
        self.chooseWin1 = pygame.draw.rect(self.screen, pygame.Color('black'),
                                           pygame.Rect(50, 150, 100, 100), 2)

    def draw_win2(self):
        self.backgroundbutton2 = pygame.draw.rect(self.screen, (250, 175, 255),
                                                  pygame.Rect(200, 150, 100, 100))
        self.chooseWin2 = pygame.draw.rect(self.screen, pygame.Color('black'),
                                           pygame.Rect(200, 150, 100, 100), 2)

    def draw_win3(self):
        self.backgroundbutton3 = pygame.draw.rect(self.screen, (250, 175, 255),
                                                  pygame.Rect(350, 150, 100, 100))
        self.chooseWin3 = pygame.draw.rect(self.screen, pygame.Color('black'),
                                           pygame.Rect(350, 150, 100, 100), 2)

    def draw_win4(self):
        self.backgroundbutton4 = pygame.draw.rect(self.screen, (250, 175, 255),
                                                  pygame.Rect(50, 300, 100, 100))
        self.chooseWin4 = pygame.draw.rect(self.screen, pygame.Color('black'),
                                           pygame.Rect(50, 300, 100, 100), 2)

    def draw_win5(self):
        self.backgroundbutton5 = pygame.draw.rect(self.screen, (250, 175, 255),
                                                  pygame.Rect(200, 300, 100, 100))
        self.chooseWin5 = pygame.draw.rect(self.screen, pygame.Color('black'),
                                           pygame.Rect(200, 300, 100, 100), 2)

    def draw_win6(self):
        self.backgroundbutton6 = pygame.draw.rect(self.screen, (250, 175, 255),
                                                  pygame.Rect(350, 300, 100, 100))
        self.chooseWin6 = pygame.draw.rect(self.screen, pygame.Color('black'),
                                           pygame.Rect(350, 300, 100, 100), 2)

    def draw_win7(self):
        self.backgroundbutton7 = pygame.draw.rect(self.screen, (250, 175, 255),
                                                  pygame.Rect(50, 450, 100, 100))
        self.chooseWin7 = pygame.draw.rect(self.screen, pygame.Color('black'),
                                           pygame.Rect(50, 450, 100, 100), 2)

    def draw_win8(self):
        self.backgroundbutton8 = pygame.draw.rect(self.screen, (250, 175, 255),
                                                  pygame.Rect(200, 450, 100, 100))
        self.chooseWin8 = pygame.draw.rect(self.screen, pygame.Color('black'),
                                           pygame.Rect(200, 450, 100, 100), 2)

    def draw_win9(self):
        self.backgroundbutton9 = pygame.draw.rect(self.screen, (250, 175, 255),
                                                  pygame.Rect(350, 450, 100, 100))
        self.chooseWin9 = pygame.draw.rect(self.screen, pygame.Color('black'),
                                           pygame.Rect(350, 450, 100, 100), 2)


if __name__ == "__main__":
    def start():
        win = MyultyplayerMode()


    start()
