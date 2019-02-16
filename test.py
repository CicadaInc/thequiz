import pygame
import os


class Pause:
    def __init__(self):
        pygame.init()

        self.screen = pygame.display.set_mode((1000, 600))

        running = True
        while running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False

            self.screen.fill(pygame.Color('white'))

            pygame.display.flip()


if __name__ == "__main__":
    Pause()
