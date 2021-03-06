import pygame

from ChooseCharacter import ChooseCharacter
from Game import Game
from MainMenu import MainMenu
from MoreInformation import Information
from Greeting import Greeting

mainWin0 = Greeting()

HEROES = ['1(Townfolk-Child-M-001)', '2(Townfolk-Child-M)',
          '3(Townfolk-Adult-M-006)',
          '4(coriander publish.)', '5(Mushroom-01)', '6(Cultist)']
while True:
    if mainWin0.pushed == pygame.Rect(624, 392, 90, 40):
        mainWin = MainMenu()
        if mainWin.pushed == pygame.Rect(55, 125, 300, 80):  # Продолжить
            chooseChar = ChooseCharacter()
            if chooseChar:
                if chooseChar.pushed == pygame.Rect(50, 515, 201, 36):  # Назад
                    continue
                elif chooseChar.pushed == pygame.Rect(750, 515, 200,
                                                      35):  # Старт
                    hero = HEROES[chooseChar.choosed]
                    gameWin = Game(hero, chooseChar.nick)
                    if gameWin.pushed == 'exit':
                        break
                    elif gameWin.pushed == 'exit_main':
                        input()

                elif chooseChar.pushed == 'exit':
                    break
            else:
                break

        elif mainWin.pushed == pygame.Rect(55, 225, 300, 80):  # Настройки
            inf = Information()
            if inf.pushed == 'exit':
                break
        elif mainWin.pushed == pygame.Rect(55, 325, 300, 80):  # Выход
            break
    elif mainWin0.pushed == 'exit':
        break
