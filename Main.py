from MainMenu import MainMenu
from ChooseCharacter import ChooseCharacter
import pygame

mainWin = MainMenu()

print(mainWin.pushed)

if mainWin.pushed == pygame.Rect(375, 150, 251, 51): #Играть
    ChooseCharacter()
elif mainWin.pushed == pygame.Rect(375, 250, 251, 51): #Мультиплеер
    ChooseCharacter()
elif mainWin.pushed == pygame.Rect(375, 350, 251, 51): #Настройки
    pass
