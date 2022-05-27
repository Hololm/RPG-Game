import sys
import random
import time
import options
import enemies
import items
import os


class Character:
    def __init__(self, name, hp, maxhp, inv):
        self.name = name
        self.hp = hp
        self.maxhp = maxhp
        self.inv = inv


def start():
    name = input('What is your name\n>>').title()
    global char
    char = Character(name, 20, 20, [random.choice(list(items.itemlist['lgweapons'])), random.choice(list(items.itemlist['lghealing']))])


start()


# where the player is currently and where they are going
def playerchoice(current, combat):

    clear = lambda: print('\n' * 150)
    clear()
    for l in options.choices:
        if current in options.choices[l]:
            option = options.choices[l][current]
            break
        else:
            continue

    #creates the options for the available locations
    locOptions = [random.choice(list(options.choices[option.option1])), random.choice(list(options.choices[option.option2]))]

    time.sleep(0.5)

    # gives user loot if current location has loot
    for loot in option.loot:
        if loot == None:
            continue
        char.inv.append(random.choice([loot, None]))
        if None in char.inv:
            char.inv.remove(None)
        else:
            print(f'You picked up {loot}.\n')

    time.sleep(1)

    print(option.desc)

    time.sleep(3)

    #let the player retype if they make a typing error
    def typingError():
        print('You may have mistyped your destination.\n')
        choice = input('Where does {} wish to go?\n{} or {}\n>>'.format(char.name, locOptions[0], locOptions[1])).title()
        if choice not in locOptions:
            typingError()
        playerchoice(choice.title(), 1)

    # combat turns for the player and enemy
    def turns(enemy, hp, eCount, eDmg):

        # ends combat if no enemies are left
        if eCount == 0:
            playerchoice(current, 0)

        if eCount > 1:
            print('\nThere are {} {}s left!'.format(eCount, enemy))
        else:
            print('\nThere is {} {} left!'.format(eCount, enemy))

        for enemytype in enemies.enemylist:
            if enemy in enemytype:
                break
            else:
                continue
        curEnemy = enemies.enemylist[enemytype]

        # current enemy hp
        if hp == None:
            hp = random.randint(curEnemy[option.enemies].hpmin, curEnemy[option.enemies].hpmax)

        # for testing
        #print(eDmg)
        #print(hp)

        time.sleep(2)

        combatoptions = ['Inventory', 'Run']
        print('\n{}\'s Health - {}'.format(char.name, char.hp))
        combatchoice = input('What does {} want to do?\nInventory    Run\n>>'.format(char.name, str(char.inv))).title()

        # avoids errors if the user mistypes their combat decision
        while combatchoice not in combatoptions:
            print('You may have mistyped your decision.')
            time.sleep(1)
            print('\n{}\'s Health - {}'.format(char.name, char.hp))
            combatchoice = input('What does {} want to do?\nInventory    Run\n>>'.format(char.name, str(char.inv))).title()

        # the player can chooce to try and run away from combat, if they fail they will be attacked
        if combatchoice == 'Run':
            run = random.randint(1, 3)
            if run == 1:
                time.sleep(1)
                print('\nyou succeed in running away')
                time.sleep(1)
                playerchoice(current, 0)
            else:
                time.sleep(1)
                print('\nYou failed to run away.')
                time.sleep(1)
                while eDmg < eCount:
                    enemyattack = random.randint(curEnemy[option.enemies].dmgmin, curEnemy[option.enemies].dmgmax)
                    print('\n{} deals {} damage to {}!'.format(enemy, enemyattack, char.name))
                    char.hp -= enemyattack
                    eDmg += 1
                    time.sleep(1)
                print('{} has {} hp left!'.format(char.name, char.hp))

                time.sleep(2)
                turns(enemy, hp, eCount, 0)

        # the player can choose to open their inventory to view the items they can use for combat
        elif combatchoice == 'Inventory':
            print(char.inv)
            itemchoice = input('What item does {} want to use?\n>>'.format(char.name)).title()

            # avoids errors if the user mistypes an item name
            while itemchoice not in char.inv:
                print('You may have mistyped the item name.')
                time.sleep(1)
                print(f'\n{char.inv}')
                itemchoice = input('What item does {} want to use?\n>>'.format(char.name)).title()

            for item in items.itemlist:
                if itemchoice in items.itemlist[item]:
                    break
                else:
                    continue

            # if the enemy is faster than the player, the enemy attacks first
            if curEnemy[enemy].spd > items.itemlist[item][itemchoice].spd:

                # enemy attacks the player
                time.sleep(1)
                while eDmg < eCount:
                    enemyattack = random.randint(curEnemy[option.enemies].dmgmin, curEnemy[option.enemies].dmgmax)
                    print('\n{} deals {} damage to {}!'.format(enemy, enemyattack, char.name))
                    char.hp -= enemyattack
                    eDmg += 1
                    time.sleep(1)
                print('{} has {} hp left!'.format(char.name, char.hp))

                # attacks the enemy if the player used a weapon
                if items.itemlist[item][itemchoice].type == 'attack':

                    # player attacks the enemy
                    time.sleep(2)
                    # gets a dmg number from the selected items range
                    playerattack = random.randint(items.itemlist[item][itemchoice].minvalue, items.itemlist[item][itemchoice].maxvalue)
                    print('\n{} deals {} damage to {}!'.format(char.name, playerattack, enemy))
                    time.sleep(1)

                    hp -= playerattack
                    print('{} has {} hp left!'.format(enemy, hp))
                    time.sleep(1)

                # heals the player if they used a healing item
                elif items.itemlist[item][itemchoice].type == 'heal':
                    time.sleep(1)
                    playerheal = random.randint(items.itemlist[item][itemchoice].minvalue, items.itemlist[item][itemchoice].maxvalue)
                    while char.hp + playerheal > char.maxhp:
                        playerheal -= 1
                    char.hp += playerheal
                    print('{} healed themself for {} hp'.format(char.name, playerheal))
                    char.inv.remove(itemchoice)

                    # if the enemy has no hp, get a new target
                    if hp < 1:
                        print('\n{} has defeated {}!'.format(char.name, enemy))
                        hp = random.randint(curEnemy[option.enemies].hpmin, curEnemy[option.enemies].hpmax)
                        eCount -= 1
                        time.sleep(1)
                        turns(enemy, hp, eCount, 0)

                    time.sleep(2)
                    turns(enemy, hp, eCount, 0)

            # if the player is faster than the enemy, the player attacks first
            else:
                # attacks the enemy if the player used a weapon
                if items.itemlist[item][itemchoice].type == 'attack':
                    # player attacks the enemy
                    time.sleep(1)
                    # gets a dmg number from the selected items range
                    playerattack = random.randint(items.itemlist[item][itemchoice].minvalue, items.itemlist[item][itemchoice].maxvalue)
                    print('\n{} deals {} damage to {}!'.format(char.name, playerattack, enemy))
                    time.sleep(1)

                    hp -= playerattack
                    print('{} has {} hp left!'.format(enemy, hp))
                    time.sleep(1)

                    # if the enemy has no hp, get a new target
                    if hp < 1:
                        print('\n{} has defeated {}!'.format(char.name, enemy))
                        hp = random.randint(curEnemy[option.enemies].hpmin, curEnemy[option.enemies].hpmax)
                        eCount -= 1
                        time.sleep(1)

                # heals the player if they used a healing item
                elif items.itemlist[item][itemchoice].type == 'heal':
                    time.sleep(1)
                    playerheal = random.randint(items.itemlist[item][itemchoice].minvalue, items.itemlist[item][itemchoice].maxvalue)
                    while char.hp + playerheal > char.maxhp:
                        playerheal -= 1
                    char.hp += playerheal
                    print('{} healed themself for {} hp'.format(char.name, playerheal))
                    char.inv.remove(itemchoice)

                # enemy attacks the player
                time.sleep(1)
                while eDmg < eCount:
                    enemyattack = random.randint(curEnemy[option.enemies].dmgmin, curEnemy[option.enemies].dmgmax)
                    print('\n{} deals {} damage to {}!'.format(enemy, enemyattack, char.name))
                    char.hp -= enemyattack
                    eDmg += 1
                    time.sleep(1)
                if eCount > 0:
                    print('{} has {} hp left!'.format(char.name, char.hp))

                time.sleep(2)
                turns(enemy, hp, eCount, 0)


    #starts combat if there are enemies in the location, otherwise you choose a new location to go to
    locEnemyCount = random.randint(0, option.count)
    if locEnemyCount > 0 and combat == 1:
        if locEnemyCount > 1:
            print('\n{} has been attacked by a group of {} {}s!'.format(char.name, locEnemyCount, option.enemies))
        else:
            print('\n{} has been attacked by {}!'.format(char.name, option.enemies))
        time.sleep(1)
        turns(option.enemies, None, locEnemyCount, 0)
    else:
        choice = input('\nWhere does {} wish to go?\n{} or {}\n>>'.format(char.name, locOptions[0], locOptions[1])).title()
        if choice not in locOptions:
            typingError()
        if char.hp < char.maxhp:
            char.hp += 1
        playerchoice(choice, 1)

playerchoice(random.choice(list(options.choices['start'])), 1)