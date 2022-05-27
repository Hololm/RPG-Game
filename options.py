import random
import items
import enemies
class option():
    def __init__(self, description, option1, option2, enemies, count, loot):
        self.desc = description
        self.option1 = option1
        self.option2 = option2
        self.enemies = enemies
        self.count = count
        self.loot = loot

randomEnemy = lambda: random.choice(list(enemies.enemylist[random.choice(list(enemies.enemylist))]))

lgweapons = random.choice(list(items.itemlist['lgweapons']))
mgweapons = random.choice(list(items.itemlist['mgweapons']))
hgweapons = random.choice(list(items.itemlist['hgweapons']))

lghealing = random.choice(list(items.itemlist['lghealing']))
mghealing = random.choice(list(items.itemlist['mghealing']))
hghealing = random.choice(list(items.itemlist['hghealing']))

#lggeneral = random.choice(list(items.itemlist['lggeneral']))
#mggeneral = random.choice(list(items.itemlist['mggeneral']))
#hggeneral = random.choice(list(items.itemlist['hggeneral']))


town = random.choice(list(['towns', 'location']))
castle = random.choice(list(['castles', 'castles']))

choices = {
    'start': {
        'Old Cabin': option('You wake up in a dusty old cabin filled with cobwebs.', 'location', 'location', None, 0, []),
        #'Destroyed Camp': option('You awake to the sound of thunder in your ransacked camp.', 'towns', 'location', None, 0, []),
        #'Cathedral': option('You wake up in a bed inside of a cathedral within a castle.', 'castles', 'location', None, 0, []),
        #'castle': option('in a castle', 'ruinedcastle', 'location', None, 0, []),
    },
    'location': {
        'Grassy Plains': option('Mostly flat grassy plains all around.', town, 'location', None, 0, []),
        'Flower Field': option('Open grassy field with colorful flowers dotting the land.', 'location', 'location', None, 0, []),
        'Grassy Hills': option('Grassy hills as far as the eye can see.', town, 'location', None, 0, []),
        'Large River': option('A large river in terms of both depth, and length.', castle, 'location', None, 0, []),
        'Sparse Forest': option('A sparse forest containing mostly oak trees.', castle, 'location', None, 0, []),
        'Dense Forest': option('A dense forest containing mostly oak trees.', town, 'location', None, 0, []),
        'Sparse Forest': option('A sparse forest containing mostly birch trees.', castle, 'location', None, 0, []),
        'Dense Forest': option('A dense forest containing mostly birch trees.', town, 'location', None, 0, []),
    },
    'castles': {
        'Ruined Castle Gate': option('An old castle gate with crumbling mossy bricks.', 'ruinedcastle', 'location', None, 0, []),
        #'Abandoned Castle Gate': option('A seemingly empty castle, it doesnt look too old.', 'abandoncastle', 'location', None, 0, []),
    },
    'ruinedcastle': {
        'Ruined Castle Hall': option('A long old hall with armor stands to the sides', 'ruinedcastle', 'location', randomEnemy(), 1, []),
    },
    'abandoncastle': {

    },
    'populatedcastle': {

    },
    'towns': {
        'Mining Town': option('A mining town with smoke clouding the sky above.', 'miningtown', 'location', None, 0, []),
    },
    'miningtown': {

    },
    'livestocktown': {

    },
    'farmingtown': {

    }
}











