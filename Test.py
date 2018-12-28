import pygame
import os


class ChooseCharacter:
    def __init__(self):
        pygame.init()

        self.screen = pygame.display.set_mode((1000, 600))
        self.text = ''
        self.font = pygame.font.Font(None, 50)

        shift = False

        self.set_interface()

        running = True
        while running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False

                if event.type == pygame.MOUSEBUTTONDOWN:
                    for i in range(len(self.chooseButtons)):
                        if self.chooseButtons[i].collidepoint(event.pos):
                            print(i)

                if event.type == pygame.KEYDOWN:
                    print(event.key)
                    if event.key == 8:
                        self.text = self.text[:-1]
                    elif event.key != 304:
                        if shift:
                            self.text += chr(event.key).upper()
                        else:
                            self.text += chr(event.key)

                    if event.key == 304:
                        shift = True
                    else:
                        pygame.draw.rect(self.screen, (250, 175, 255),
                                         pygame.Rect(665, 100, self.inp_width, self.inp_height))
                        pygame.draw.rect(self.screen, (0, 0, 0), pygame.Rect(665, 100, self.inp_width, self.inp_height), 2)

                        self.input_name = self.font.render(self.text, 1, (100, 25, 100))
                        text_x, text_y = 670, 100

                        if self.input_name.get_width() < self.inp_width and self.text.isalnum():
                            self.screen.blit(self.input_name, (text_x, text_y))
                        else:
                            self.text = self.text[:-1]
                            self.input_name = self.font.render(self.text, 1, (100, 25, 100))
                            self.screen.blit(self.input_name, (text_x, text_y))

                if event.type == pygame.KEYUP:
                    if event.key == 304:
                        shift = False

            pygame.display.flip()

    def set_interface(self):
        directory = os.getcwd()  # Фон
        background_surf = pygame.image.load(directory + '/backgrounds/main.jpg')
        background_surf = pygame.transform.scale(background_surf, (1000, 600))
        background_rect = background_surf.get_rect(bottomright=(1000, 600))
        self.screen.blit(background_surf, background_rect)

        self.chooseButtons = []  # Выбор персонажа
        for y in range(150, 451, 150):
            for x in range(50, 351, 150):
                pygame.draw.rect(self.screen, (250, 175, 255), pygame.Rect(x, y, 100, 100))
                self.chooseButtons.append(pygame.draw.rect(self.screen, pygame.Color('black'),
                                                           pygame.Rect(x, y, 100, 100), 2))

        text_view = self.font.render("Выберите персонажа", 1, (100, 25, 100))  # Надписи
        text_x, text_y = 65, 60
        self.screen.blit(text_view, (text_x, text_y))

        text_name = self.font.render("Введите имя", 1, (100, 25, 100))
        text_x, text_y = 665, 60
        self.screen.blit(text_name, (text_x, text_y))

        self.inp_width, self.inp_height = text_name.get_width(), text_name.get_height()
        pygame.draw.rect(self.screen, (250, 175, 255), pygame.Rect(665, 100, self.inp_width, self.inp_height))
        pygame.draw.rect(self.screen, (0, 0, 0), pygame.Rect(665, 100, self.inp_width, self.inp_height), 2)


if __name__ == "__main__":
    def start():
        win = ChooseCharacter()


    start()
