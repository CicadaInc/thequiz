import pygame
import os


class MyultyplayerMode:
    def __init__(self):
        pygame.init()

        self.winWidth = 1000
        self.winHeight = 600
        self.screen = pygame.display.set_mode((self.winWidth, self.winHeight))
        pygame.display.set_caption("the quiz")

        # LOAD BACKGROUND
        directory = os.getcwd()
        background_surf = pygame.image.load(directory + '/backgrounds/main.jpg')
        background_surf = pygame.transform.scale(background_surf, (1000, 600))
        background_rect = background_surf.get_rect(bottomright=(1000, 600))
        self.screen.blit(background_surf, background_rect)

        running = True
        while running:
            pygame.time.delay(100)

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                if event.type == pygame.MOUSEBUTTONDOWN:


if __name__ == "__main__":
    def start():
        win = MyultyplayerMode()


    start()
