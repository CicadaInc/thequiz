import pygame
import os


class Information:
    def __init__(self):
        pygame.init()

        self.screen = pygame.display.set_mode((1000, 600))

        self.font_back = pygame.font.Font('sprites/freesansbold.ttf', 30)
        self.font_tittle1 = pygame.font.Font('sprites/freesansbold.ttf', 45)

        pygame.mouse.set_visible(False)

        self.set_interface()

        running = True
        while running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if self.back.collidepoint(*event.pos):
                        running = False

            self.render()

            pygame.display.flip()

    def set_interface(self):
        directory = os.getcwd()

        # LOAD BACKGROUND
        self.background_surf = pygame.image.load(directory + '/backgrounds/quizFone.jpg')
        self.background_surf = pygame.transform.scale(self.background_surf, (1000, 600))
        self.background_rect = self.background_surf.get_rect(bottomright=(1000, 600))

        self.back = pygame.Rect(50, 515, 200, 35)
        self.text_back = self.font_back.render("Назад", 1, (100, 25, 100))
        self.text_x_1, self.text_y_1 = 150 - self.text_back.get_width() // 2, 550 - self.text_back.get_height()

        self.rules1 = pygame.Rect(70, 45, 260, 60)
        self.text_rules1 = self.font_tittle1.render("Правила", 1, (60, 132, 45))
        self.text_rules1_x, self.text_rules1_y = 200 - self.text_rules1.get_width() // 2, 100 - self.text_rules1.get_height()

        self.rules2 = pygame.Rect(50, 150, 300, 300)

        self.authors1 = pygame.Rect(672, 420, 150, 40)
        self.text_authors1 = self.font_back.render("Авторы", 1, (60, 132, 45))
        self.text_authors1_x ,self.text_authors1_y = 750 - self.text_authors1.get_width() // 2, 457 - self.text_authors1.get_height()

        self.authors2 = pygame.Rect(600, 480, 300, 100)

        self.warning = pygame.Rect(600, 40, 300, 100)

        # КУРСОР
        self.cursor = pygame.image.load('sprites/ForGUI/cursor1.png')

    def render(self):
        self.screen.fill(pygame.Color('white'))

        self.screen.blit(self.background_surf, self.background_rect)

        # НАЗАД
        pygame.draw.rect(self.screen, (250, 175, 255), self.back)
        pygame.draw.rect(self.screen, (0, 0, 0), self.back, 2)
        self.screen.blit(self.text_back, (self.text_x_1, self.text_y_1))

        #ПРАВИЛА
        pygame.draw.rect(self.screen, (250, 175, 255), self.rules1)
        pygame.draw.rect(self.screen, (0, 0, 0), self.rules1, 2)
        self.screen.blit(self.text_rules1, (self.text_rules1_x, self.text_rules1_y))

        pygame.draw.rect(self.screen, (250, 175, 255), self.rules2)
        pygame.draw.rect(self.screen, (0, 0, 0), self.rules2, 2)

        #АВТОРЫ
        pygame.draw.rect(self.screen, (250, 175, 255), self.authors1)
        pygame.draw.rect(self.screen, (0, 0, 0), self.authors1, 2)
        self.screen.blit(self.text_authors1, (self.text_authors1_x, self.text_authors1_y))

        pygame.draw.rect(self.screen, (250, 175, 255), self.authors2)
        pygame.draw.rect(self.screen, (0, 0, 0), self.authors2, 2)

        #СОВЕТ
        pygame.draw.rect(self.screen, (250, 175, 255), self.warning)
        pygame.draw.rect(self.screen, (0, 0, 0), self.warning, 2)

        # КУРСОР
        pos = pygame.mouse.get_pos()
        rect = self.cursor.get_rect(topleft=pos)
        self.screen.blit(self.cursor, rect)


if __name__ == "__main__":
    Information()
