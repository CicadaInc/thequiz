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
        if mainWin.pushed == pygame.Rect(55, 125, 300, 80):  # Продолжить
            chooseChar = ChooseCharacter()
            if chooseChar:
                if chooseChar.pushed == pygame.Rect(50, 515, 201, 36):  # Назад
                    continue
                elif chooseChar.pushed == pygame.Rect(750, 515, 200, 35):  # Старт
                    hero = HEROES[chooseChar.choosed]
                    gameWin = Game('The Quiz', 468, 210, "MainLocation.png", field, hero, 2300, 1550)
                    if gameWin.pushed == 'exit':
                        break
                elif chooseChar.pushed == 'exit':
                    break
            else:
                break

        elif mainWin.pushed == pygame.Rect(58, 225, 300, 80):  # Настройки
            pass
        elif mainWin.pushed == pygame.Rect(55, 325, 300, 80):  # Выход
            break
    elif mainWin0.pushed == 'exit':
        break
