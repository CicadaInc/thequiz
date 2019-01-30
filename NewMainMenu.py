import pygame
import os


class NewMainMenu:
    def __init__(self):
        pygame.init()

        self.winWidth = 1000
        self.winHeight = 600
        self.screen = pygame.display.set_mode((self.winWidth, self.winHeight))

        self.x, self.y = 250, 445

        self.pushed = None

        self.set_interface()

        pygame.mouse.set_visible(False)
        surf = pygame.image.load('sprites/ForGUI/cursor1.png')

        push = False
        running = True
        while running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.pushed = 'exit'
                    running = False
                if event.type == pygame.MOUSEBUTTONDOWN:
                    x, y = event.pos
                    x += 12
                    if self.coinRect.collidepoint((x, y)):
                        push = True
                        x_, y_ = event.pos[0] - self.x, event.pos[1] - self.y
                if event.type == pygame.MOUSEBUTTONUP:
                    push = False
                if event.type == pygame.MOUSEMOTION and push:
                    self.x, self.y = event.pos
                    self.x -= x_
                    self.y -= y_

            if self.buttons[0].collidepoint((self.x - 25, self.y - 30)):
                self.pushed = self.buttons[0]
                running = False

            self.render()

            pos = pygame.mouse.get_pos()
            rect = surf.get_rect(topleft=pos)
            self.screen.blit(surf, rect)

            pygame.display.flip()

    def render(self):
        self.screen.blit(self.background_surf, self.background_rect)

        pygame.draw.rect(self.screen, (0, 0, 0), self.buttons[0])

        self.screen.blit(self.text, (self.text_x, self.text_y))

        self.screen.blit(self.automat, self.automatRect)

        self.coinRect = self.coin.get_rect(bottomright=(self.x, self.y))
        self.screen.blit(self.coin, self.coinRect)

    def set_interface(self):
        directory = os.getcwd()

        self.background_surf = pygame.image.load(directory + '/backgrounds/main.jpg')
        self.background_surf = pygame.transform.scale(self.background_surf, (1000, 600))
        self.background_rect = self.background_surf.get_rect(bottomright=(1000, 600))
        self.screen.blit(self.background_surf, self.background_rect)

        # LOAD MUSIC
        pygame.mixer.music.load(directory + '/sounds/loading.mp3')
        pygame.mixer.music.play(-1)
        pygame.mixer.music.set_volume(0.3)

        font = pygame.font.Font('sprites/freesansbold.ttf', 30)

        # КНОПКИ И НАДПИСИ
        self.buttons = [pygame.draw.rect(self.screen, (0, 0, 0),
                                         pygame.Rect(624, 392, 90, 40))]
        self.text = font.render('<<<------', 1, (218, 114, 3))
        self.text_x, self.text_y = 795 - self.text.get_width() // 2, 385 + 25 - self.text.get_height() // 2
        self.screen.blit(self.text, (self.text_x, self.text_y))

        # АВТОМАТ
        self.automat = pygame.image.load('sprites/Game_building.jpg')
        self.automat = pygame.transform.scale(self.automat, (280, 70))
        self.automatRect = self.automat.get_rect(bottomright=(720, self.y))
        self.screen.blit(self.automat, self.automatRect)

        # МОНЕТКА
        self.coin = pygame.image.load('sprites/coin.png')
        self.coin = pygame.transform.scale(self.coin, (50, 60))
        self.coinRect = self.coin.get_rect(bottomright=(self.x, self.y))
        self.screen.blit(self.coin, self.coinRect)


if __name__ == "__main__":
    def start():
        win = NewMainMenu()


    start()
