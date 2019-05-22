### _TheQuiz_ – ролевая компьютерная игра в жанре головоломки с видом сверху. 
****
#### Авторы:
* [kuzdman](https://github.com/kuzdman) (Дмитрий Кузнецов)
* [Glander13](https://github.com/Glander13) (Иван Чебыкин)
* [SophIren](https://github.com/SophIren) (Марк Шкут)
****
Рекомендуется запускать thequiz.exe.

Также вы можете скачать версию содержащую только exe и необходимые файлы 
с [Яндекс.Диска](https://yadi.sk/d/evW-uGjwyp3d1Q)
****
#### Видео
Чтобы примерно представить себе наш проект в действии вы можете посмотреть тизер-трейлер на youtube:
[![здесь должен быть ролик](https://upload.wikimedia.org/wikipedia/commons/thumb/b/b8/YouTube_Logo_2017.svg/512px-YouTube_Logo_2017.svg.png)](https://youtu.be/VA0tBxHlNO4)
****
#### Идея игры
Идея игры заключается в развитии у человека мыслительных способностей, путём 
решения головоломок и разгадывания задач, требующих максимальной концентрации.
****
Некоторые уровни в игре могут казаться слишком сложными и требующими особой подготовки в 
программировании, но это не так. Практически каждый человек, игравший в эту игру прошёл её без 
особой подготовки, но нужно заметить что эти люди в неё играли очень внимательно.
****
#### Структура игры
Карта представляет собой одно большое изображение([levels/MainLocation.png](https://github.com/CicadaInc/thequiz/blob/master/levels/MainLocation.png)), к которому 
подкрепляется файл([create_field.py](https://github.com/CicadaInc/thequiz/blob/master/create_field.py)), содержащий двумерный массив со всеми объектами на карте. 
Это сделано для оптимизации игры, 
ведь карта довольно большая и обработать её тяжело.

Код игры распределён по разным файлам(например: Game.py, Quest1.py и др.), которые подключаются к одному [главному файлу](https://github.com/CicadaInc/thequiz/blob/master/Main.py).

Остальную информацию можно найти в [презентации](https://github.com/CicadaInc/thequiz/blob/master/presentation.pptx).
****
Использованные технологии:
* IDE Pycharm
* Adobe Photoshop CC 2018
* Paint
****
Язык разработки - _[Python 3](https://www.python.org)_
****
Использованные фреймоврки:
* pygame
* os
* time
* math
****
Общая схема проекта:
![здесь должна быть картинка...](https://image.prntscr.com/image/Y7pQkjVVTLmsT_hG2Gi7Gw.png)
****
Скриншоты из игры:
![здесь должна быть картинка...](https://image.prntscr.com/image/Lh2wJ0b6QmOeVLTyfsNcyA.png)

![здесь должна быть картинка...](https://image.prntscr.com/image/oDgSOvrdQAO-QkU4P5Mfjw.png)

![здесь должна быть картинка...](https://image.prntscr.com/image/AaaynEYDTAygs9Z74P78Ig.png)
****
Остальную информацию можно найти в [презентации](https://github.com/CicadaInc/thequiz/blob/master/presentation.pptx).

