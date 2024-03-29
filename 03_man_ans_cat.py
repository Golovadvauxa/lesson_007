# -*- coding: utf-8 -*-

from random import randint

# Доработать практическую часть урока lesson_007/python_snippets/08_practice.py

# Необходимо создать класс кота. У кота есть аттрибуты - сытость и дом (в котором он живет).
# Кот живет с человеком в доме.
# Для кота дом характеризируется - миской для еды и грязью.
# Изначально в доме нет еды для кота и нет грязи.

# Доработать класс человека, добавив методы
#   подобрать кота - у кота появляется дом.
#   купить коту еды - кошачья еда в доме увеличивается на 50, деньги уменьшаются на 50.
#   убраться в доме - степень грязи в доме уменьшается на 100, сытость у человека уменьшается на 20.
# Увеличить кол-во зарабатываемых человеком денег до 150 (он выучил пайтон и устроился на хорошую работу :)

# Кот может есть, спать и драть обои - необходимо реализовать соответствующие методы.
# Когда кот спит - сытость уменьшается на 10
# Когда кот ест - сытость увеличивается на 20, кошачья еда в доме уменьшается на 10.
# Когда кот дерет обои - сытость уменьшается на 10, степень грязи в доме увеличивается на 5
# Если степень сытости < 0, кот умирает.
# Так же надо реализовать метод "действуй" для кота, в котором он принимает решение
# что будет делать сегодня

# Человеку и коту надо вместе прожить 365 дней.

from termcolor import cprint


class Man:

    def __init__(self, name):
        self.name = name
        self.fullness = 50
        self.house = None

    def __str__(self):
        return 'Я - {}, сытость {}'.format(
            self.name, self.fullness)

    def eat(self):
        if self.house.food >= 10:
            cprint('{} поел'.format(self.name), color='yellow')
            self.fullness += 10
            self.house.food -= 10
        else:
            cprint('{} нет еды'.format(self.name), color='red')

    def work(self):
        cprint('{} сходил на работу'.format(self.name), color='blue')
        self.house.money += 150
        self.fullness -= 10

    def watch_MTV(self):
        cprint('{} смотрел MTV целый день'.format(self.name), color='green')
        self.fullness -= 10

    def shopping(self):
        if self.house.money >= 50:
            cprint('{} сходил в магазин за едой'.format(self.name), color='magenta')
            self.house.money -= 50
            self.house.food += 50
        else:
            cprint('{} деньги кончились!'.format(self.name), color='red')

    def cat_shopping(self):
        if self.house.money >= 50:
            cprint('{} сходил в магазин за едой котику'.format(self.name), color='magenta')
            self.house.money -= 50
            self.house.cat_food += 50

    def do_cleaning(self):
        if self.house.mess <= 50:
            cprint('{} убрал дома'.format(self.name), color='magenta')
            self.fullness -= 10
        else:
            cprint('{} убрал дикий срач дома'.format(self.name), color='magenta')
            self.fullness -= 10

    def feed_cat(self):
        if self.house.cat_food >= 20:
            cprint('{} насыпал корма котику'.format(self.name), color='magenta')
            self.house.cat_food -= 20
            self.house.cat_plate += 20

    def go_to_the_house(self, house):
        self.house = house
        self.fullness -= 10
        cprint('{} Вьехал в дом'.format(self.name), color='cyan')

    def act(self):
        if self.fullness <= 0:
            cprint('{} умер...'.format(self.name), color='red')
            return
        dice = randint(1, 6)
        if self.fullness < 20:
            self.eat()
        elif self.house.food <= 10:
            self.shopping()
        elif self.house.money < 50:
            self.work()
        elif self.house.cat_food <= 10:
            self.cat_shopping()
        elif self.house.mess > 50:
            self.do_cleaning()
        elif self.house.cat_plate <= 10:
            self.feed_cat()
        elif dice == 1:
            self.work()
        elif dice == 2:
            self.eat()
        elif dice == 3:
            self.do_cleaning()
        else:
            self.watch_MTV()


class House:

    def __init__(self):
        self.food = 50
        self.money = 0
        self.cat_food = 0
        self.mess = 0
        self.cat_plate = 0

    def __str__(self):
        return 'В доме еды осталось {},еды для котика {},в миске {}, денег осталось {}, степень срача {}'.format(
            self.food, self.cat_food,self.cat_plate, self.money, self.mess)


class Cat:

    def __init__(self, name):
        self.name = name
        self.fullness = 50
        self.house = None

    def __str__(self):
        return 'Я котик - {}, сытость - {}'.format(self.name, self.fullness)

    def eat(self):
        if self.house.cat_plate >= 10:
            cprint('Котик {} поел'.format(self.name), color='yellow')
            self.fullness += 20
            self.house.cat_plate -= 10
        elif self.house.food >= 10:
            cprint('Котик {} спиздил колбасу!'.format(self.name), color='cyan')
            self.fullness += 20
            self.house.food -= 10
        else:
            cprint('Котик {} нет еды'.format(self.name), color='red')

    def sleep(self):
        cprint('Котик {} спал весь день '.format(self.name), color='yellow')
        self.fullness -= 10

    def tear_wallpaper(self):
        cprint('Котик {} подрал обои'.format(self.name), color='blue')
        self.house.mess += 10

    def find_house(self, house):
        self.house = house
        cprint('Котик {} нашел дом'.format(self.name), color='cyan')

    def act(self):
        if self.fullness <= 0:
            cprint('Котик {} умер...'.format(self.name), color='red')
            return
        dice = randint(1, 6)
        if self.fullness < 20:
            self.eat()
        elif dice == 1:
            self.eat()
        elif 2 <= dice <= 3:
            self.tear_wallpaper()
        else:
            self.sleep()


house = House()
dude = Man(name='Чувак')
yakov = Cat(name='Яшка')
dude.go_to_the_house(house)
yakov.find_house(house)

for day in range(1, 366):
    print('================ день {} =================='.format(day))
    dude.act()
    yakov.act()
    print('--- в конце дня ---')
    print(dude)
    print('-------------------------------------------')
    print(yakov)
    print('-------------------------------------------')
    print(house)
# Усложненное задание (делать по желанию)
# Создать несколько (2-3) котов и подселить их в дом к человеку.
# Им всем вместе так же надо прожить 365 дней.

# (Можно определить критическое количество котов, которое может прокормить человек...)
