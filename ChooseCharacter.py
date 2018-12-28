import pygame
import os


class ChooseCharacter:
    def __init__(self):
        pygame.init()

        self.screen = pygame.display.set_mode((1000, 600))

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

            pygame.display.flip()

    def set_interface(self):
        directory = os.getcwd()
        background_surf = pygame.image.load(directory + '/backgrounds/main.jpg')
        background_surf = pygame.transform.scale(background_surf, (1000, 600))
        background_rect = background_surf.get_rect(bottomright=(1000, 600))
        self.screen.blit(background_surf, background_rect)

        self.chooseButtons = []
        for y in range(150, 451, 150):
            for x in range(50, 351, 150):
                pygame.draw.rect(self.screen, (250, 175, 255), pygame.Rect(x, y, 100, 100))
                self.chooseButtons.append(pygame.draw.rect(self.screen, pygame.Color('black'),
                                                           pygame.Rect(x, y, 100, 100), 2))

        font = pygame.font.Font(None, 50)

        text_view = font.render("Выберите персонажа", 1, (100, 25, 100))
        text_view_x, text_view_y = 65, 60
        self.screen.blit(text_view, (text_view_x, text_view_y))

        text_name = font.render("Введите имя", 1, (100, 25, 100))
        text_name_x, text_name_y = 665, 60
        self.screen.blit(text_name, (text_name_x, text_name_y))


if __name__ == "__main__":
    def start():
        win = ChooseCharacter()


    start()
