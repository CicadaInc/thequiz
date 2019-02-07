import pygame
import os

def load_image(name):
    image = pygame.image.load(name)
    return image

class MainMenu:
    def __init__(self):
        pygame.init()

        self.winWidth = 1000
        self.winHeight = 600
        self.screen = pygame.display.set_mode((self.winWidth, self.winHeight))

        self.pushed = None
        self.y = 100

        self.directory = os.getcwd()

        # self.images = []
        # for i in range(1, 30):
        #     self.images.append(load_image(
        #         self.directory + '/sprites/ForGUI/Blue buttons/level select blue button 300x80 hover/' +
        #         'level select button blue 300x80 (' + str(i) + ').png'))
        # выше спрайты
        # self.index = 0
        # self.image = self.images[self.index]
        # self.rect = pygame.Rect(5, 5, 300, 80)

        pygame.mouse.set_visible(False)

        self.set_interface()
        surf = pygame.image.load('sprites/ForGUI/cursor1.png')

        running = True
        while running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    # self.pushed = self.buttons[-1]
                    running = False
                if event.type == pygame.MOUSEBUTTONDOWN:
                    for i in range(len(self.buttons)):
                        if self.buttons[i].collidepoint(event.pos):
                            self.pushed = self.buttons[i]
                            running = False
            self.render()

            pos = pygame.mouse.get_pos()
            rect = surf.get_rect(topleft=pos)
            self.screen.blit(surf, rect)

            pygame.display.flip()

    def render(self):
        self.screen.blit(self.background_surf, self.background_rect)
        self.screen.blit(self.continue_btn, self.continue_btn_Rect)
        self.screen.blit(self.options_btn, self.options_btn_Rect)
        self.screen.blit(self.quit_btn, self.quit_btn_Rect)
        # pygame.draw.rect(self.screen, (0, 0, 0), self.buttons[0])
        # pygame.draw.rect(self.screen, (0, 0, 0), self.buttons[1])
        # pygame.draw.rect(self.screen, (0, 0, 0), self.buttons[2])
        # выше черные размещения кнопок
    def set_interface(self):
        directory = os.getcwd()

        # LOAD BACKGROUND
        self.background_surf = pygame.image.load(directory + '/backgrounds/quizFone.jpg')
        self.background_surf = pygame.transform.scale(self.background_surf, (1000, 600))
        self.background_rect = self.background_surf.get_rect(bottomright=(1000, 600))
        self.screen.blit(self.background_surf, self.background_rect)

        # LOAD MUSIC
        # pygame.mixer.music.load(directory + '/sounds/loading.mp3')
        # pygame.mixer.music.play(-1)
        # pygame.mixer.music.set_volume(0.3)

        self.buttons = []

        self.continue_btn = pygame.image.load('sprites/ForGUI/Blue buttons/Play blue button 300x80.png')
        self.continue_btn = pygame.transform.scale(self.continue_btn, (300, 80))
        self.continue_btn_Rect = self.continue_btn.get_rect(bottomright=(355, 205))
        self.screen.blit(self.continue_btn, self.continue_btn_Rect)

        self.options_btn = pygame.image.load('sprites/ForGUI/Blue buttons/options blue button 300x80.png')
        self.options_btn = pygame.transform.scale(self.options_btn, (300, 80))
        self.options_btn_Rect = self.options_btn.get_rect(bottomright=(355, 305))
        self.screen.blit(self.options_btn, self.options_btn_Rect)

        self.quit_btn = pygame.image.load('sprites/ForGUI/Blue buttons/Quit blue button 300x80.png')
        self.quit_btn = pygame.transform.scale(self.quit_btn, (300, 80))
        self.quit_btn_Rect = self.quit_btn.get_rect(bottomright=(355, 405))
        self.screen.blit(self.quit_btn, self.quit_btn_Rect)

        for y in range(50, 351, 100):
            pygame.draw.rect(self.screen, (250, 175, 255),
                             pygame.Rect(200, y + 50, 250, 200))
            self.buttons.append(pygame.draw.rect(self.screen, pygame.Color('black'),
                                                 pygame.Rect(58, y + 75, 300, 80), 2))
        # print(self.buttons)

if __name__ == "__main__":
    MainMenu()

