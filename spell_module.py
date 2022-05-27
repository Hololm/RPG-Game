import math
from colorama import Fore, Back, init


class Magic:
    def __init__(self, description, mana_cost, turns, level):
        self.description = description
        self.mana_cost = mana_cost
        self.turns = turns
        self.level = level

    def magic_function(self, enemy):
        
        print('Mana:' + Fore.LIGHTBLUE_EX + ' {}'.format(self.mana) + Fore.RESET)
        for (i, spell) in enumerate(sorted(self.spell_inv), start=1):
            print(i, spell)
        
        magic = input("\nWhat spell?\n>> ").title()
        
        for spell_choice in magics:
            if magic in magics[spell_choice]:
                if magic in self.spell_inv and self.level >= magics[spell_choice][magic].level:
                    if self.mana >= magics[spell_choice][magic].mana_cost:
                        print("{} casted {}!".format(self.name, magic))
                        
                        if spell_choice == 'offensive magic':
                            self.attack(enemy, magics[spell_choice][magic].dmg)
                        elif spell_choice == 'healing magic':
                            self.hp += magics[spell_choice][magic].hp
                        elif spell_choice == 'defensive magic':
                            pass
                        elif spell_choice == 'buffing magic':
                            pass
                        self.mana -= magics[spell_choice][magic].mana_cost
                        
                    else:
                        print("{} does not have enough mana to cast.".format(self.name))
                else:
                    print("{} is too low level to cast.".format(self.name))

                   
class Offensive(Magic):
    def __init__(self, description, mana_cost, turns, level, dmg):
        super().__init__(description, mana_cost, turns, level)
        self.dmg = dmg
        
        
class Defensive(Magic):
    def __init__(self, description, mana_cost, turns, level, armor):
        super().__init__(description, mana_cost, turns, level)
        self.armor = armor


class Healing(Magic):
    def __init__(self, description, mana_cost, turns, level, hp):
        super().__init__(description, mana_cost, turns, level)
        self.hp = hp


class Buffing(Magic):
    def __init__(self, description, mana_cost, turns, level):
        super().__init__(description, mana_cost, turns, level)


magics = {
    
    'defensive magic': {
        'Ice Block': Defensive('Human ic- ..wait...', 4, 2, 1, 5),
    },
    
    'offensive magic': {
        'Vengeful Spirit': Offensive('Seal the blinding light that plagues their dreams.', 2, 0, 1, 1.2),
        'Descending Dark': Offensive('The void is yours to command. You are the Vessel. You... are the Hollow Knight.', 4, 0, 5, 4),
    },
    
    'healing magic': {
        'Death Pact': Healing('You make a pact with death so you dont... ya know.', 4, 2, 3, 2),
    },
    
    'buffing magic': {
        'Runic Empowerment': Buffing('Empower your weapon with unfamiliar runes.', 2, 3, 0),
    },
    
}