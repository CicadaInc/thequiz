import pygame
import os

# LEVEL MENU
class LevelMenu:
    def __init__(self):

        pygame.init()

        self.winWidth = 1000
        self.winHeight = 600
        self.screen = pygame.display.set_mode((self.winWidth, self.winHeight))

        self.font = pygame.font.Font(None, 50)

        self.set_interface()

        self.choosed = 0
        running = True
        while running:
            events = pygame.event.get()
            for event in events:
                if event.type == pygame.QUIT:
                    running = False

                if event.type == pygame.MOUSEBUTTONDOWN:
                    for i in range(len(self.buttons)):
                        if self.buttons[i].collidepoint(event.pos):
                            pygame.draw.rect(self.screen, pygame.Color('black'),
                                             self.buttons[self.choosed], 2)
                            pygame.draw.rect(self.screen, pygame.Color('red'),
                                             self.buttons[i], 2)
                            self.choosed = i
                        
                        elif self.back.collidepoint(event.pos):
                            self.pushed = self.back
                            running = False

                        elif self.start.collidepoint(event.pos):
                            self.pushed = self.start
                            running = False

            pygame.display.flip()


    def set_interface(self):
        directory = os.getcwd()

        # LOAD BACKGROUND
        background_surf = pygame.image.load(directory + '/backgrounds/main.jpg')
        background_surf = pygame.transform.scale(background_surf, (1000, 600))
        background_rect = background_surf.get_rect(bottomright=(1000, 600))
        self.screen.blit(background_surf, background_rect)

        self.buttons, names = [], ['Sonata','...', '...']
        font = pygame.font.Font(None, 50)

        # BUTTON BACK
        pygame.draw.rect(self.screen, (250, 175, 255), pygame.Rect(50, 515, 200, 35))
        self.back = pygame.draw.rect(self.screen, (0, 0, 0), pygame.Rect(50, 515, 200, 35), 2)
        text_back = self.font.render("Назад", 1, (100, 25, 100))
        text_x, text_y = 150 - text_back.get_width() // 2, 550 - text_back.get_height()
        self.screen.blit(text_back, (text_x, text_y))

        # LEVEL BUTTONS
        for y in range(150, 450, 100):
            pygame.draw.rect(self.screen, (250, 175, 255),
                             pygame.Rect(375, y, 250, 50))
            self.buttons.append(pygame.draw.rect(self.screen, pygame.Color('black'),
                                                 pygame.Rect(375, y, 250, 50), 2))
            text = font.render(names[y // 100 - 1], 1, (100, 25, 100))
            text_x, text_y = 500 - text.get_width() // 2, y + 25 - text.get_height() // 2
            self.screen.blit(text, (text_x, text_y))

        # START BUTTON
        pygame.draw.rect(self.screen, (250, 175, 255), pygame.Rect(750, 515, 200, 35))
        self.start = pygame.draw.rect(self.screen, (0, 0, 0), pygame.Rect(750, 515, 200, 35), 2)
        text_start = self.font.render("Старт", 1, (100, 25, 100))
        text_x, text_y = 850 - text_start.get_width() // 2, 550 - text_start.get_height()
        self.screen.blit(text_start, (text_x, text_y))


if __name__ == "__main__":
    def start():
        win = LevelMenu()


    start()
