import pygame
import os


class Game:
    def __init__(self):
        pygame.init()

        self.screen = pygame.display.set_mode((1000, 600))

        self.pushed = None

        self.set_interface()

        running = True
        while running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False

            pygame.display.flip()

    def set_interface(self):
        # SET BACKGROUND
        directory = os.getcwd()
        background_surf = pygame.image.load(directory + '/levels/level.png')
        background_surf = pygame.transform.scale(background_surf, (1000, 600))
        background_rect = background_surf.get_rect(bottomright=(1000, 600))
        self.screen.blit(background_surf, background_rect)


if __name__ == "__main__":
    def test():
        game = Game()


    test()
