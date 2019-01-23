import pygame
import eztext
import os


class ChooseCharacter:
    def __init__(self):
        pygame.init()

        self.screen = pygame.display.set_mode((1000, 600))
        self.text = ''
        self.font = pygame.font.Font('sprites/freesansbold.ttf', 30)
        self.choosed = 0

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

            pygame.display.flip()

    def set_interface(self):
        directory = os.getcwd()

        # LOAD BACKGROUND
        background_surf = pygame.image.load(directory + '/backgrounds/quizFone.jpg')
        background_surf = pygame.transform.scale(background_surf, (1000, 600))
        background_rect = background_surf.get_rect(bottomright=(1000, 600))
        self.screen.blit(background_surf, background_rect)

        # BUTTON BACK
        pygame.draw.rect(self.screen, (250, 175, 255), pygame.Rect(50, 515, 200, 35))
        self.back = pygame.draw.rect(self.screen, (0, 0, 0), pygame.Rect(50, 515, 200, 35), 2)
        text_back = self.font.render("Назад", 1, (100, 25, 100))
        text_x, text_y = 150 - text_back.get_width() // 2, 550 - text_back.get_height()
        self.screen.blit(text_back, (text_x, text_y))

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
        text_start = self.font.render("Старт", 1, (100, 25, 100))
        text_x, text_y = 850 - text_start.get_width() // 2, 550 - text_start.get_height()
        self.screen.blit(text_start, (text_x, text_y))

        # НАДПИСИ
        text_view = self.font.render("Выберите персонажа", 1, (100, 25, 100))
        text_x, text_y = 65, 60
        self.screen.blit(text_view, (text_x, text_y))

        text_name = self.font.render("Введите имя", 1, (100, 25, 100))
        text_x, text_y = 665, 60
        self.screen.blit(text_name, (text_x, text_y))

        self.inp_width, self.inp_height = text_name.get_width(), text_name.get_height()


if __name__ == "__main__":
    def start():
        win = ChooseCharacter()


    start()
