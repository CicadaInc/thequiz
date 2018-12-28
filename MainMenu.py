import pygame
import os


class MainMenu:
    def __init__(self):
        pygame.init()

        self.winWidth = 1000
        self.winHeight = 600
        self.screen = pygame.display.set_mode((self.winWidth, self.winHeight))

        self.pushed = None

        self.set_interface()

        running = True
        while running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.pushed = self.buttons[3]
                    running = False
                if event.type == pygame.MOUSEBUTTONDOWN:
                    for i in range(len(self.buttons)):
                        if self.buttons[i].collidepoint(event.pos):
                            self.pushed = self.buttons[i]
                            running = False

            pygame.display.flip()

    def set_interface(self):
        directory = os.getcwd()

        # LOAD BACKGROUND
        background_surf = pygame.image.load(directory + '/backgrounds/main.jpg')
        background_surf = pygame.transform.scale(background_surf, (1000, 600))
        background_rect = background_surf.get_rect(bottomright=(1000, 600))
        self.screen.blit(background_surf, background_rect)

        # LOAD MUSIC
        pygame.mixer.music.load(directory + '/sounds/loading.mp3')
        pygame.mixer.music.play(-1)
        pygame.mixer.music.set_volume(0.3)

        self.buttons, names = [], ['Играть', 'Мультиплеер', 'Настройки', 'Выход']
        font = pygame.font.Font(None, 50)
        for y in range(150, 451, 100):
            pygame.draw.rect(self.screen, (250, 175, 255),
                             pygame.Rect(375, y, 250, 50))
            self.buttons.append(pygame.draw.rect(self.screen, pygame.Color('black'),
                                                 pygame.Rect(375, y, 250, 50), 2))
            text = font.render(names[y // 100 - 1], 1, (100, 25, 100))
            text_x, text_y = 500 - text.get_width() // 2, y + 25 - text.get_height() // 2
            self.screen.blit(text, (text_x, text_y))


if __name__ == "__main__":
    def start():
        win = MainMenu()


    start()
