# -*- coding: utf-8 -*-

# Создать прототип игры Алхимия: при соединении двух элементов получается новый.
# Реализовать следующие элементы: Вода, Воздух, Огонь, Земля, Шторм, Пар, Грязь, Молния, Пыль, Лава.
# Каждый элемент организовать как отдельный класс.
# Таблица преобразований:
#   Вода + Воздух = Шторм
#   Вода + Огонь = Пар
#   Вода + Земля = Грязь
#   Воздух + Огонь = Молния
#   Воздух + Земля = Пыль
#   Огонь + Земля = Лава

# Сложение элементов реализовывать через __add__
# Если результат не определен - то возвращать None
# Вывод элемента на консоль реализовывать через __str__
#
# Примеры преобразований:
#   print(Water(), '+', Air(), '=', Water() + Air())
#   print(Fire(), '+', Air(), '=', Fire() + Air())


class Water:
    def __str__(self):
        return 'Water'

    def __add__(self, other):
        if isinstance(other, Air):
            return Storm()
        elif isinstance(other, Fire):
            return Steam()
        elif isinstance(other, Ground):
            return Mud()
        else:
            return None


class Air:
    def __str__(self):
        return 'Air'

    def __add__(self, other):
        if isinstance(other, Fire):
            return Lightning()
        elif isinstance(other, Ground):
            return Dust()
        elif isinstance(other, Water):
            return Storm()
        else:
            return None


class Fire:
    def __str__(self):
        return 'Fire'

    def __add__(self, other):
        if isinstance(other, Ground):
            return Lava()
        elif isinstance(other, Air):
            return Lightning()
        elif isinstance(other, Water):
            return Steam()
        else:
            return None


class Ground:
    def __str__(self):
        return 'Ground'

    def __add__(self, other):
        if isinstance(other, Water):
            return Mud()
        elif isinstance(other, Air):
            return Dust()
        elif isinstance(other, Fire):
            return Lava()


class Storm:
    def __str__(self):
        return 'Storm'


class Steam:
    def __str__(self):
        return 'Steam'


class Mud:
    def __str__(self):
        return 'Mud'


class Lightning:
    def __str__(self):
        return 'Lightning'


class Dust:
    def __str__(self):
        return 'Dust'


class Lava:
    def __str__(self):
        return 'Lava'


print(Water(), '+', Air(), '=', Water() + Air())
print(Fire(), '+', Water(), '=', Fire() + Water())
print(Water(), '+', Ground(), '=', Water() + Ground())
print(Fire(), '+', Air(), '=', Fire() + Air())
print(Ground(), '+', Air(), '=', Ground() + Air())
print(Fire(), '+', Ground(), '=', Fire() + Ground())
# Усложненное задание (делать по желанию)
# Добавить еще элемент в игру.
# Придумать что будет при сложении существующих элементов с новым.

