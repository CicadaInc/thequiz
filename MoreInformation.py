import pygame
import os


class Information:
    def __init__(self):
        pygame.init()

        self.screen = pygame.display.set_mode((1000, 600))

        self.font_back = pygame.font.Font('fonts/freesansbold.ttf', 30)
        self.font_rules = pygame.font.Font('fonts/comic.ttf', 22)
        self.font_authors = pygame.font.Font('fonts/comic.ttf', 25)
        self.font_warning = pygame.font.Font('fonts/comic.ttf', 23)
        self.font_tittle1 = pygame.font.Font('fonts/freesansbold.ttf', 45)

        self.pushed = None

        pygame.mouse.set_visible(False)

        self.set_interface()

        running = True
        while running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.pushed = 'exit'
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

        #@@@@@@
        self.back = pygame.Rect(50, 515, 200, 35)
        self.text_back = self.font_back.render("Назад", 1, (100, 25, 100))
        self.text_x_1, self.text_y_1 = 150 - self.text_back.get_width() // 2, 550 - self.text_back.get_height()

        #@@@@@@
        self.rules1 = pygame.Rect(100, 45, 260, 60)
        self.text_rules1 = self.font_tittle1.render("Правила", 1, (60, 132, 45))
        self.text_rules1_x, self.text_rules1_y = 135, 54

        self.rules2 = pygame.Rect(50, 150, 360, 300)

        self.text_rules2 = self.font_rules.render("Цель игры заключается в", 1, (0, 0, 0))
        self.text_rules2_x, self.text_rules2_y = 65, 150

        self.text_rules3 = self.font_rules.render("том, чтобы исследовать", 1, (0, 0, 0))
        self.text_rules3_x, self.text_rules3_y = 65, 200

        self.text_rules4 = self.font_rules.render("карту и находить на ней", 1, (0, 0, 0))
        self.text_rules4_x, self.text_rules4_y = 65, 250

        self.text_rules5 = self.font_rules.render("загадки, при решении которых", 1, (0, 0, 0))
        self.text_rules5_x, self.text_rules5_y = 65, 300

        self.text_rules6 = self.font_rules.render("потребуются ваши смекалка и", 1, (0, 0, 0))
        self.text_rules6_x, self.text_rules6_y = 65, 350

        self.text_rules7 = self.font_rules.render("сообразительность", 1, (0, 0, 0))
        self.text_rules7_x, self.text_rules7_y = 65, 400

        #@@@@@@
        self.authors1 = pygame.Rect(672, 420, 150, 40)
        self.text_authors1 = self.font_back.render("Авторы", 1, (60, 132, 45))
        self.text_authors1_x ,self.text_authors1_y = 693, 426

        self.authors2 = pygame.Rect(600, 480, 300, 100)

        self.text_authors2 = self.font_authors.render("Дмитрий Кузнецов", 1, (0, 0, 0))
        self.text_authors2_x, self.text_authors2_y = 640, 480

        self.text_authors3 = self.font_authors.render("Иван Чебыкин", 1, (0, 0, 0))
        self.text_authors3_x, self.text_authors3_y = 640, 510

        self.text_authors4 = self.font_authors.render("Марк Шкут", 1, (0, 0, 0))
        self.text_authors4_x, self.text_authors4_y = 640, 540

        #@@@@@@
        self.warning = pygame.Rect(585, 40, 320, 100)

        self.text_warning1 = self.font_warning.render("ВНИМАНИЕ: В игру", 1, (220, 30, 15))
        self.text_warning1_x, self.text_warning1_y = 625, 42

        self.text_warning2 = self.font_warning.render("необходимо играть", 1, (220, 30, 15))
        self.text_warning2_x, self.text_warning2_y = 625, 67

        self.text_warning3 = self.font_warning.render("со ВКЛЮЧЕННЫМ звуком", 1, (220, 30, 15))
        self.text_warning3_x, self.text_warning3_y = 598, 97

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

        self.screen.blit(self.text_rules2, (self.text_rules2_x, self.text_rules2_y))
        self.screen.blit(self.text_rules3, (self.text_rules3_x, self.text_rules3_y))
        self.screen.blit(self.text_rules4, (self.text_rules4_x, self.text_rules4_y))
        self.screen.blit(self.text_rules5, (self.text_rules5_x, self.text_rules5_y))
        self.screen.blit(self.text_rules6, (self.text_rules6_x, self.text_rules6_y))
        self.screen.blit(self.text_rules7, (self.text_rules7_x, self.text_rules7_y))

        #АВТОРЫ
        pygame.draw.rect(self.screen, (250, 175, 255), self.authors1)
        pygame.draw.rect(self.screen, (0, 0, 0), self.authors1, 2)
        self.screen.blit(self.text_authors1, (self.text_authors1_x, self.text_authors1_y))

        pygame.draw.rect(self.screen, (250, 175, 255), self.authors2)
        pygame.draw.rect(self.screen, (0, 0, 0), self.authors2, 2)

        self.screen.blit(self.text_authors2, (self.text_authors2_x, self.text_authors2_y))
        self.screen.blit(self.text_authors3, (self.text_authors3_x, self.text_authors3_y))
        self.screen.blit(self.text_authors4, (self.text_authors4_x, self.text_authors4_y))

        #СОВЕТ
        pygame.draw.rect(self.screen, (250, 175, 255), self.warning)
        pygame.draw.rect(self.screen, (0, 0, 0), self.warning, 2)
        self.screen.blit(self.text_warning1, (self.text_warning1_x, self.text_warning1_y))
        self.screen.blit(self.text_warning2, (self.text_warning2_x, self.text_warning2_y))
        self.screen.blit(self.text_warning3, (self.text_warning3_x, self.text_warning3_y))

        # КУРСОР
        pos = pygame.mouse.get_pos()
        rect = self.cursor.get_rect(topleft=pos)
        self.screen.blit(self.cursor, rect)


if __name__ == "__main__":
    Information()
