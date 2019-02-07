import pygame
import eztext
import os


class ChooseCharacter:
    def __init__(self, choosed=0):
        pygame.init()

        pygame.mouse.set_visible(False)
        surf = pygame.image.load('sprites/ForGUI/cursor1.png')

        self.screen = pygame.display.set_mode((1000, 600))
        self.text = ''
        self.font = pygame.font.Font('sprites/freesansbold.ttf', 30)
        self.choosed = choosed

        self.pushed = None

        textbox = eztext.Input(maxlength=10, color=(0, 0, 0), prompt='',
                               font=pygame.font.Font('sprites/freesansbold.ttf', 30))
        textbox.set_pos(670, 155)

        self.set_interface()

        running = True
        while running:
            events = pygame.event.get()
            for event in events:
                if event.type == pygame.QUIT:
                    running = False

                if event.type == pygame.MOUSEBUTTONDOWN:
                    for i in range(len(self.chooseButtons)):
                        if self.chooseButtons[i].collidepoint(event.pos):
                            pygame.draw.rect(self.screen, pygame.Color('black'),
                                             self.chooseButtons[self.choosed], 2)
                            pygame.draw.rect(self.screen, pygame.Color('red'),
                                             self.chooseButtons[i], 2)
                            self.choosed = i

                        elif self.back.collidepoint(event.pos):
                            self.pushed = self.back
                            running = False
                        elif self.start.collidepoint(event.pos):
                            self.pushed = self.start
                            running = False

            # ПОЛЕ ВВОДА НИКА
            pygame.draw.rect(self.screen, (250, 175, 255),
                             pygame.Rect(665, 150, self.inp_width, self.inp_height))
            pygame.draw.rect(self.screen, (0, 0, 0),
                             pygame.Rect(665, 150, self.inp_width, self.inp_height), 2)
            textbox.update(events)
            textbox.draw(self.screen)

            self.render()

            pos = pygame.mouse.get_pos()
            rect = surf.get_rect(topleft=pos)
            self.screen.blit(surf, rect)

            pygame.display.flip()

    def render(self):

        self.screen.blit(self.background_surf, self.background_rect)
        pygame.draw.rect(self.screen, (250, 175, 255), pygame.Rect(50, 515, 200, 35))
        self.back = pygame.draw.rect(self.screen, (0, 0, 0), pygame.Rect(50, 515, 200, 35), 2)
        self.screen.blit(self.text_back, (self.text_x_1, self.text_y_1))
        self.chooseButtons = []
        i = 0
        for y in range(150, 301, 150):
            for x in range(50, 351, 150):
                i += 1
                pygame.draw.rect(self.screen, (250, 175, 255), pygame.Rect(x, y, 100, 100))
                self.chooseButtons.append(pygame.draw.rect(self.screen, pygame.Color('black'),
                                                           pygame.Rect(x, y, 100, 100), 2))

                character = pygame.image.load('sprites/characters/' + str(i) + '.png')
                character = pygame.transform.scale(character, (97, 97))
                self.screen.blit(character, (x + 2, y + 2))
        pygame.draw.rect(self.screen, pygame.Color('red'), self.chooseButtons[self.choosed], 2)
        pygame.draw.rect(self.screen, (250, 175, 255), pygame.Rect(750, 515, 200, 35))
        self.start = pygame.draw.rect(self.screen, (0, 0, 0), pygame.Rect(750, 515, 200, 35), 2)

        self.screen.blit(self.text_start, (self.text_x_2, self.text_y_2))
        self.screen.blit(self.text_view, (self.text_x_3, self.text_y_3))
        self.screen.blit(self.text_name, (self.text_x_4, self.text_y_4))
        self.inp_width, self.inp_height = self.text_name.get_width(), self.text_name.get_height()

    def set_interface(self):
        directory = os.getcwd()

        # LOAD BACKGROUND
        self.background_surf = pygame.image.load(directory + '/backgrounds/quizFone.jpg')
        self.background_surf = pygame.transform.scale(self.background_surf, (1000, 600))
        self.background_rect = self.background_surf.get_rect(bottomright=(1000, 600))
        self.screen.blit(self.background_surf, self.background_rect)

        # BUTTON BACK
        pygame.draw.rect(self.screen, (250, 175, 255), pygame.Rect(50, 515, 200, 35))
        self.back = pygame.draw.rect(self.screen, (0, 0, 0), pygame.Rect(50, 515, 200, 35), 2)
        self.text_back = self.font.render("Назад", 1, (100, 25, 100))
        self.text_x_1, self.text_y_1 = 150 - self.text_back.get_width() // 2, 550 - self.text_back.get_height()
        self.screen.blit(self.text_back, (self.text_x_1, self.text_y_1))

        # ОКНА ПЕРСОНАЖЕЙ
        self.chooseButtons = []
        i = 0
        for y in range(150, 301, 150):
            for x in range(50, 351, 150):
                i += 1
                pygame.draw.rect(self.screen, (250, 175, 255), pygame.Rect(x, y, 100, 100))
                self.chooseButtons.append(pygame.draw.rect(self.screen, pygame.Color('black'),
                                                           pygame.Rect(x, y, 100, 100), 2))

                character = pygame.image.load('sprites/characters/' + str(i) + '.png')
                character = pygame.transform.scale(character, (97, 97))
                self.screen.blit(character, (x + 2, y + 2))
        pygame.draw.rect(self.screen, pygame.Color('red'), self.chooseButtons[self.choosed], 2)

        # КНОПКА СТАРТА
        pygame.draw.rect(self.screen, (250, 175, 255), pygame.Rect(750, 515, 200, 35))
        self.start = pygame.draw.rect(self.screen, (0, 0, 0), pygame.Rect(750, 515, 200, 35), 2)
        self.text_start = self.font.render("Старт", 1, (100, 25, 100))
        self.text_x_2, self.text_y_2 = 850 - self.text_start.get_width() // 2, 550 - self.text_start.get_height()
        self.screen.blit(self.text_start, (self.text_x_2, self.text_y_2))

        # НАДПИСИ
        self.text_view = self.font.render("Выберите персонажа", 1, (100, 25, 100))
        self.text_x_3, self.text_y_3 = 65, 60
        self.screen.blit(self.text_view, (self.text_x_3, self.text_y_3))

        self.text_name = self.font.render("Введите имя", 1, (100, 25, 100))
        self.text_x_4, self.text_y_4 = 665, 60
        self.screen.blit(self.text_name, (self.text_x_4, self.text_y_4))

        self.inp_width, self.inp_height = self.text_name.get_width(), self.text_name.get_height()


if __name__ == "__main__":
    def start():
        win = ChooseCharacter()


    start()
