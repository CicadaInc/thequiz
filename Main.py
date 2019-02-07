from MainMenu import MainMenu
from NewMainMenu import NewMainMenu
from ChooseCharacter import ChooseCharacter
from Game import Game
from field import field
import pygame

mainWin0 = NewMainMenu()

HEROES = ['1(Townfolk-Child-M-001)', '2(Townfolk-Child-M)', '3(Townfolk-Adult-M-006)',
          '4(coriander publish.)', '5(Mushroom-01)', '6(Cultist)']
while True:
    if mainWin0.pushed == pygame.Rect(624, 392, 90, 40):
        mainWin = MainMenu()
        if mainWin.pushed == pygame.Rect(58, 125, 301, 81):  # Продолжить
            chooseChar = ChooseCharacter()
            if chooseChar:
                if chooseChar.pushed == pygame.Rect(50, 515, 201, 36):  # Назад
                    continue
                elif chooseChar.pushed == pygame.Rect(750, 515, 201, 36):  # Старт
                    hero = HEROES[chooseChar.choosed]
                    gameWin = Game(1000, 600, 'The Quiz', 50, 100, "level.png", field, hero)
                    if gameWin.pushed == 'exit':
                        break
            else:
                break

        elif mainWin.pushed == pygame.Rect(58, 225, 301, 81):  # Настройки
            pass
        elif mainWin.pushed == pygame.Rect(58, 325, 301, 81):  # Выход
            break
    elif mainWin0.pushed == 'exit':
        break
