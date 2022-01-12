# -*- coding: utf-8 -*-

import simple_draw as sd
from random import randint

sd.set_screen_size(1200, 800)


# Шаг 1: Реализовать падение снежинки через класс. Внести в методы:
#  - создание снежинки с нужными параметрами
#  - отработку изменений координат
#  - отрисовку


class Snowflake:

    def __init__(self):
        self.x = randint(0, 1200)
        self.y = randint(750, 950)
        self.speed = randint(10, 55)
        self.point = sd.get_point(self.x, self.y)
        self.length = randint(10,60)


    def fall(self):
        self.point = sd.get_point(self.x, self.y)
        sd.snowflake(center=self.point,length=self.length)
        self.y -= self.speed
        self.x+= randint(-15,15)

    def stop(self):
        if self.y <= 0:
            return True


def create_snowflake(N):
    flakes_list = []
    for i in range(N):
        flakes_list.append(Snowflake())
    return flakes_list

# flake = Snowflake()
#
# while True:
#     sd.clear_screen()
#     flake.fall()
#     sd.sleep(0.1)
#     if flake.stop():
#         del flake
#         flake = Snowflake()

    # flake.clear_previous_picture()
    # flake.move()
    # flake.draw()
    # if not flake.can_fall():
    #     break
    # sd.sleep(0.1)
    # if sd.user_want_exit():
    #     break

# шаг 2: создать снегопад - список объектов Снежинка в отдельном списке, обработку примерно так:
# flakes = get_flakes(count=N)  # создать список снежинок
# while True:
#     for flake in flakes:
#         flake.clear_previous_picture()
#         flake.move()
#         flake.draw()
#     fallen_flakes = get_fallen_flakes()  # подчитать сколько снежинок уже упало
#     if fallen_flakes:
#         append_flakes(count=fallen_flakes)  # добавить еще сверху
#     sd.sleep(0.1)
#     if sd.user_want_exit():
#         break

flakes =create_snowflake(20)
while True:
    sd.clear_screen()
    for flake in flakes:
        flake.fall()
        if flake.stop():
            flake.__init__()

    if sd.user_want_exit():
        break
    sd.sleep(0.1)




sd.pause()
