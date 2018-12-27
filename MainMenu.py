import pygame


class MainMenu:
    def __init__(self):
        pygame.init()

        self.winWidth = 800
        self.winHeight = 600

        self.screen = pygame.display.set_mode((self.winWidth, self.winHeight))
        self.screen.fill(pygame.Color('white'))

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
                    if self.quitButton.collidepoint(event.pos):
                        self.pushed = self.quitButton
                        running = False

            self.render()

            pygame.display.flip()

    def render(self):
        self.draw_start_button()
        self.draw_quit_button()

    def draw_start_button(self):
        self.startButton = pygame.draw.rect(self.screen, pygame.Color('black'), pygame.Rect(500, 50, 200, 50), 3)
        text = self.font.render("Играть", 1, (100, 25, 100))
        text_x, text_y = 600 - text.get_width() // 2, 75 - text.get_height() // 2
        self.screen.blit(text, (text_x, text_y))

    def draw_quit_button(self):
        self.quitButton = pygame.draw.rect(self.screen, pygame.Color('black'), pygame.Rect(500, 150, 200, 50), 3)
        text = self.font.render("Выход", 1, (100, 25, 100))
        text_x, text_y = 600 - text.get_width() // 2, 175 - text.get_height() // 2
        self.screen.blit(text, (text_x, text_y))


if __name__ == "__main__":
    def test():
        win = MainMenu()


    test()
