import pygame
import os


class MainMenu:
    def __init__(self):
        pygame.init()

        self.winWidth = 1000
        self.winHeight = 600
        self.screen = pygame.display.set_mode((self.winWidth, self.winHeight))

        self.pushed = None
        self.y = 100

        self.motionButton = None

        self.directory = os.getcwd()

        pygame.mouse.set_visible(False)

        self.set_interface()
        surf = pygame.image.load('sprites/ForGUI/cursor1.png')

        running = True
        while running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.pushed = self.buttons[-1][1]
                    running = False
                if event.type == pygame.MOUSEBUTTONUP:
                    for i in range(len(self.buttons)):
                        if self.buttons[i][1].collidepoint(event.pos):
                            self.pushed = self.buttons[i][1]
                            running = False
                if event.type == pygame.MOUSEMOTION:
                    for i in range(len(self.buttons)):
                        if self.buttons[i][1].collidepoint(event.pos) and self.buttons[i][1] != self.motionButton:
                            self.motionButton = self.buttons[i][1]
                            self.i = i
                            self.status = 0
                    if not (self.motionButton is None):
                        if not self.motionButton.collidepoint(event.pos):
                            self.motionButton = None
            self.render()

            rect = surf.get_rect(topleft=pygame.mouse.get_pos())
            self.screen.blit(surf, rect)

            pygame.display.flip()

    def render(self):
        self.screen.blit(self.background_surf, self.background_rect)

        for button in self.buttons:
            if self.motionButton == button[1]:
                self.screen.blit(self.images[self.i][self.status], button[1])
                self.status += 1

                if self.status == 30:
                    self.status = 0
            else:
                self.screen.blit(button[0], button[1])

    def set_interface(self):
        directory = os.getcwd()

        # LOAD BACKGROUND
        self.background_surf = pygame.image.load(directory + '/backgrounds/quizFone.jpg')
        self.background_surf = pygame.transform.scale(self.background_surf, (1000, 600))
        self.background_rect = self.background_surf.get_rect(bottomright=(1000, 600))

        # LOAD MUSIC
        # pygame.mixer.music.load(directory + '/sounds/loading.mp3')
        # pygame.mixer.music.play(-1)
        # pygame.mixer.music.set_volume(0.3)

        self.continue_btn = load_image('sprites/ForGUI/Blue buttons/Play blue button 300x80.png')
        self.continue_btn_Rect = self.continue_btn.get_rect(bottomright=(355, 205))

        self.options_btn = load_image('sprites/ForGUI/Blue buttons/options blue button 300x80.png')
        self.options_btn_Rect = self.options_btn.get_rect(bottomright=(355, 305))

        self.quit_btn = load_image('sprites/ForGUI/Blue buttons/Quit blue button 300x80.png')
        self.quit_btn_Rect = self.quit_btn.get_rect(bottomright=(355, 405))

        self.buttons = [(self.continue_btn, self.continue_btn_Rect),
                        (self.options_btn, self.options_btn_Rect),
                        (self.quit_btn, self.quit_btn_Rect)]

        self.images = [[]]
        for i in range(1, 31):
            self.images[-1].append(load_image(
                self.directory + '/sprites/ForGUI/Blue buttons/play blue button 300x80 hover/' +
                'play button blue 300x80 (' + str(i) + ').png'))

        self.images.append([])
        for i in range(1, 31):
            self.images[-1].append(load_image(
                self.directory + '/sprites/ForGUI\Blue buttons\options blue button 300x80 hover/' +
                'option blue button 300x80 (' + str(i) + ').png'))

        self.images.append([])
        for i in range(1, 31):
            self.images[-1].append(load_image(
                self.directory + '/sprites/ForGUI\Blue buttons\Quit blue button 300x80 hover/' +
                'quit blue button 300x80 (' + str(i) + ').png'))

def load_image(name):
    image = pygame.image.load(name)
    image = pygame.transform.scale(image, (300, 80))

    return image


if __name__ == "__main__":
    MainMenu()
