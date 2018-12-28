import pygame
import os


class MainMenu:
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

        running = True
        while running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if self.startButton.collidepoint(event.pos):
                        self.pushed = self.startButton
                        running = False
                    if self.settingsButton.collidepoint(event.pos):
                        self.pushed = self.settingsButton
                        running = False
                    if self.myultyplayerButton.collidepoint(event.pos):
                        self.pushed = self.myultyplayerButton
                        running = False
                    if self.quitButton.collidepoint(event.pos):
                        self.pushed = self.quitButton
                        running = False

            self.render()

            pygame.display.flip()

    def render(self):
        self.draw_start_button()
        self.draw_settings_button()
        self.draw_myultyplayer_button()
        self.draw_quit_button()

    def draw_start_button(self):
        self.backbutton1 = pygame.draw.rect(self.screen, (250, 175, 255),
                                            pygame.Rect(375, 150, 250, 50))
        self.startButton = pygame.draw.rect(self.screen, pygame.Color('black'),
                                            pygame.Rect(375, 150, 250, 50), 2)
        text = self.font.render("Играть", 1, (100, 25, 100))
        text_x, text_y = 500 - text.get_width() // 2, 175 - text.get_height() // 2
        self.screen.blit(text, (text_x, text_y))

    def draw_myultyplayer_button(self):
        self.backbutton2 = pygame.draw.rect(self.screen, (250, 175, 255),
                                            pygame.Rect(375, 250, 250, 50))
        self.myultyplayerButton = pygame.draw.rect(self.screen, pygame.Color('black'),
                                                   pygame.Rect(375, 250, 250, 50), 2)
        text = self.font.render("Мультиплеер", 1, (100, 25, 100))
        text_x, text_y = 500 - text.get_width() // 2, 275 - text.get_height() // 2
        self.screen.blit(text, (text_x, text_y))

    def draw_settings_button(self):
        self.backbutton3 = pygame.draw.rect(self.screen, (250, 175, 255),
                                            pygame.Rect(375, 350, 250, 50))
        self.settingsButton = pygame.draw.rect(self.screen, pygame.Color('black'),
                                               pygame.Rect(375, 350, 250, 50), 2)
        text = self.font.render("Настройки", 1, (100, 25, 100))
        text_x, text_y = 500 - text.get_width() // 2, 375 - text.get_height() // 2
        self.screen.blit(text, (text_x, text_y))

    def draw_quit_button(self):
        self.backbutton4 = pygame.draw.rect(self.screen, (250, 175, 255),
                                            pygame.Rect(375, 450, 250, 50))
        self.quitButton = pygame.draw.rect(self.screen, pygame.Color('black'),
                                           pygame.Rect(375, 450, 250, 50), 2)
        text = self.font.render("Выход", 1, (100, 25, 100))
        text_x, text_y = 500 - text.get_width() // 2, 475 - text.get_height() // 2
        self.screen.blit(text, (text_x, text_y))


if __name__ == "__main__":
    def start():
        win = MainMenu()


    start()
