import pygame
import time


class Egg:
    def __init__(self, screen, img_path, sound_path):
        self.screen = screen

        self.surf = pygame.image.load(img_path)
        self.rect = self.surf.get_rect(bottomright=(1000, 600))

        pygame.mixer.music.load(sound_path)
        pygame.mixer.music.play(-1)
        pygame.mixer.music.set_volume(1)

        start = time.monotonic()
        end = time.monotonic()
        stop = False
        while end - start <= 240:
            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    if event.key == 27:
                        stop = True
                if event.type == pygame.QUIT:
                    stop = True
                    self.pushed = 'exit'
            if stop:
                pygame.mixer.music.stop()
                break

            end = time.monotonic()

            self.render()

            pygame.display.flip()

    def render(self):
        self.screen.blit(self.surf, self.rect)
