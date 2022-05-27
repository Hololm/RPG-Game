import math
import os
import random
import sys
import time

from colorama import Fore, init

import items
import spell_module


class Entity:
    def __init__(self, name, hp, dmg, level, xp, inv):
        self.name = name
        self.hp = hp
        self.dmg = dmg
        self.level = level
        self.xp = xp
        self.inv = inv


class Enemy(Entity):
    def __init__(self, name, hp, dmg, level, xp, inv):
        super().__init__(name, hp, dmg, level, xp, inv)

    def attack(self):
        damage_range = random.randint(self.dmg + self.level, int(self.dmg * 1.2) + int(self.level * 1.2))
        print("{} did {} dmg!".format(self.name, damage_range))
        return damage_range

    def __str__(self):
        return f"Name: {Fore.LIGHTGREEN_EX + self.name + Fore.RESET} HP: {Fore.LIGHTRED_EX + str(self.hp) + Fore.RESET} Lvl. {Fore.LIGHTMAGENTA_EX + str(self.level) + Fore.RESET} "

class Character(Entity):
    def __init__(self, name, hp, dmg, level, xp, inv, mana, max_mana, spell_inv):
        super().__init__(name, hp, dmg, level, xp, inv)
        self.max_hp = self.hp
        self.max_dmg = self.dmg
        self.mana = mana
        self.max_mana = max_mana
        self.win = False
        self.spell_inv = spell_inv

    def attack(self, enemy, atk_spell=1):
        damage_range = random.randint(self.dmg + self.level, self.dmg * 2 + self.level * 2)
        crit_roll = random.randint(1, 16)
        if crit_roll == 16:
            print("It was a critical hit!")
            damage_range *= 2
        print("{} did {} dmg!".format(self.name, math.ceil(damage_range * atk_spell)))
        enemy.hp -= math.ceil(damage_range * atk_spell)
        print('{} is down to {} hp!'.format(enemy.name, enemy.hp if enemy.hp >= 0 else 0))

    def inventory(self, p2):
        items.Item.item_function(self, p2)

    def magic(self, enemy):
        return spell_module.Magic.magic_function(self, enemy)

    def flee(self):
        flee_chance = random.randint(1, 10)
        if flee_chance != 10:
            print("{} failed to flee!".format(self.name))
        else:
            print("{} successfully escaped...".format(self.name))
            self.win = True

    def lvl_xp(self, enemy):
        xp_total = (self.xp + enemy.xp) + (self.level * 100)  # (75 + 375) + (3*100) = 750
        self.level = math.floor(xp_total / 100)  # level = 750 / 100 = floor(7.5) => 7
        self.xp = xp_total % 100  # xp = 750 % 100 = 50

    def player_turn(self, p2):

        print('{}\n{}'.format(self.__str__(), p2.__str__()))

        choice = input(
            f'\nWhat do you want to do?\n' + Fore.LIGHTRED_EX + 'Attack' + Fore.LIGHTBLUE_EX + '       Magic\n' +
            Fore.LIGHTYELLOW_EX + 'Flee' + Fore.LIGHTMAGENTA_EX + '         Item\n' + Fore.RESET + '>> ').lower()

        if choice == 'atk' or choice == "attack":
            self.attack(p2)

        elif choice == 'item' or choice == 'inventory':
            self.inventory(p2)

        elif choice == 'magic':
            self.magic(p2)

        elif choice == 'flee':
            self.flee()

        time.sleep(2)

        if not self.win:
            self.enemy_turn(p2)

    def enemy_turn(self, p2):

        if p2.hp <= 0:
            print("{} defeated the {}".format(self.name, p2.name))
            self.lvl_xp(p2)
            print("{0} gained {1} xp! {0} is level {2}.".format(self.name, p2.xp, self.level))
            time.sleep(3)

        else:
            self.hp -= p2.attack()
            print('{} is down to {} hp'.format(self.name, self.hp if self.hp >= 0 else 0))
            time.sleep(3)

            if self.hp <= 0:
                sys.exit("{} died...".format(self.name))

    def battle(self, *enemy):

        self.win = False
        queue = [enemy[i] for i in range(len(enemy))]  # [skeleton, moon lord, rugged skeleton, xqc]

        name_list = [x.name for x in queue]

        if len(name_list) == 1:
            print("{} encountered a {}".format(self.name, ''.join(name_list)))
        else:
            print("{} encountered {}".format(self.name, ', '.join(name_list)))
        time.sleep(3)

        while not self.win:
            for current_enemy in queue:  # starts with skeleton first 0, 1, 2
                self.player_turn(current_enemy)
                if self.win:
                    break
                self.mana += 1
                if self.mana > self.max_mana:
                    self.mana = self.max_mana
                if current_enemy.hp <= 0:
                    queue.remove(current_enemy)
                if not queue:
                    self.win = True
        print(f"{self.name} Won!")
        self.win = False
        self.mana, self.hp, self.dmg = math.ceil(self.max_mana / 2), self.max_hp, self.max_dmg
        time.sleep(3)
        input("Press Enter to continue...")

    def __str__(self):
        return f'Name: {Fore.LIGHTGREEN_EX + self.name + Fore.RESET} HP: {Fore.LIGHTRED_EX + str(self.hp) + Fore.RESET} Mana: {Fore.LIGHTBLUE_EX + str(self.mana) + Fore.RESET} Lvl. {Fore.LIGHTMAGENTA_EX + str(self.level) + Fore.RESET} '


init(autoreset=True)

name = input("What is your name?\n>> ")

char = Character(name, 20, 5, 1, 0, ["Estus Flask", "Estus Flask", "Golden Bag of Holding", "Beets"], 2, 4,
                 ['Ice Block', 'Vengeful Spirit', 'Death Pact'])

char.battle(Enemy('Rugged Skeleton', 12, 1, 2, 50, []), Enemy('Moon Lord', 10, 3, 1, 300, []))
