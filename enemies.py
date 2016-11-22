# coding: utf-8
# license: GPLv3
from gameunit import *
from random import randint, choice

class Enemy(Attacker):
    pass


def generate_random_enemy():
    RandomEnemyType = choice(enemy_types)
    enemy = RandomEnemyType()
    return enemy


def generate_dragon_list(enemy_number):
    enemy_list = [generate_random_enemy() for i in range(enemy_number)]
    return enemy_list


class Dragon(Enemy):
    def set_answer(self, answer):
        self.__answer = answer

    def check_answer(self, answer):
        return answer == self.__answer


class GreenDragon(Dragon):
    _health = 20
    _attack = 10
    _color = 'зелёный'

    def question(self):
        x = randint(1,20)
        y = randint(1,20)
        self.__quest = str(x) + '+' + str(y)
        self.set_answer(x + y)
        return self.__quest

#FIXME здесь также должны быть описаны классы RedDragon и BlackDragon
# красный дракон учит вычитанию, а чёрный -- умножению.
class RedDragon(Dragon):
    _health = 20
    _attack = 10
    _color = 'красный'

    def question(self):
        x = randint(1,20)
        y = randint(1,20)
        self.__quest = str(x) + '-' + str(y)
        self.set_answer(x - y)
        return self.__quest

class BlackDragon(Dragon):
    _health = 20
    _attack = 10
    _color = 'зелёный'

    def question(self):
        x = randint(1,10)
        y = randint(1,10)
        self.__quest = str(x) + '*' + str(y)
        self.set_answer(x * y)
        return self.__quest

class Troll1(Dragon):
    _health = 20
    _attack = 10
    _color = 'угадайка-тролль'
    def question(self):
        x = randint(1, 5)
        self.__quest = "угадай число от 1 до 5"
        self.set_answer(x)
        return self.__quest

class Troll2(Dragon):
    _health = 20
    _attack = 10
    _color = 'простой-тролль'
    def question(self):
        x = randint(1, 30)
        self.__quest = "простое ли число" + str(x) + '? (1/0)'
        if IsPrime(x):
            self.set_answer(1)
        else: self.set_answer(0)
        return self.__quest



enemy_types = [GreenDragon, RedDragon, BlackDragon, Troll1, Troll2]



def IsPrime(n):

    d = 2

    while n % d != 0:

        d += 1

    return d == n