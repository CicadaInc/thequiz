from MainMenu import MainMenu
from LevelMenu import LevelMenu
from ChooseCharacter import ChooseCharacter
from Game import Game
from Multiplayer import play_multiplayer
import pygame

mainWin = MainMenu()

while True:
    if mainWin.pushed == mainWin.buttons[0]:  # Играть
        chooseChar = ChooseCharacter()
        if chooseChar.pushed == chooseChar.back:  # Назад
            mainWin = MainMenu()
        elif chooseChar.pushed == chooseChar.start:  # Старт
            lvlWin = LevelMenu()
            if lvlWin.pushed == lvlWin.start:
                gameWin = play_multiplayer()  # Вместо этого должен быть запуск первого ур-ня
                break
            elif lvlWin.pushed == lvlWin.back:
                chooseChar = ChooseCharacter()
            else:
                break
        else:
            break

    elif mainWin.pushed == mainWin.buttons[1]:  # Мультиплеер
        chooseChar = ChooseCharacter()
        if chooseChar.pushed:
            if chooseChar.pushed == chooseChar.back:
                mainWin = MainMenu()
            elif chooseChar.pushed == chooseChar.start:
                gameWin = play_multiplayer()
                break
            else:
                break
        else:
            break

    elif mainWin.pushed == mainWin.buttons[2]:  # Настройки
        pass
    elif mainWin.pushed == mainWin.buttons[3]:  # Выход
        break
