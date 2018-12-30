from MainMenu import MainMenu
from LevelMenu import LevelMenu
from ChooseCharacter import ChooseCharacter
from Multiplayer import Multiplayer
import pygame
import os

mainWin = MainMenu()

print(mainWin.pushed)

while True:
    if mainWin.pushed == pygame.Rect(375, 150, 251, 51):  # Играть
        chooseChar = ChooseCharacter()
        print(chooseChar.pushed)
        if chooseChar.pushed:
            if chooseChar.pushed == pygame.Rect(50, 515, 201, 36):  # Назад
                mainWin = MainMenu()

            elif chooseChar.pushed == pygame.Rect(750, 515, 201, 36):  # Старт
                lvlWin = LevelMenu()
                if lvlWin.pushed == pygame.Rect(750, 515, 200, 36):
                    gameWin = Multiplayer()
                    try:
                        if gameWin.pushed:
                            pass
                        else:
                            break
                    except Exception:
                        print("Come back")
                else:
                    break
        else:
            break

    elif mainWin.pushed == pygame.Rect(375, 250, 251, 51):  # Мультиплеер
        chooseChar = ChooseCharacter()
        print(chooseChar.pushed)
        if chooseChar.pushed:
            if chooseChar.pushed == pygame.Rect(50, 515, 201, 36):
                mainWin = MainMenu()
            if chooseChar.pushed == pygame.Rect(750, 515, 200, 36):
                    gameWin = Multiplayer()
                    try:
                        if gameWin.pushed:
                            pass
                        else:
                            break
                    except Exception:
                        print("Come back")
            else:
                break

        else:
            break

    elif mainWin.pushed == pygame.Rect(375, 350, 251, 51):  # Настройки
        pass
    elif mainWin.pushed == pygame.Rect(375, 450, 251, 51):  # Выход
        break

