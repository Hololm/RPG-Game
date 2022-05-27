import items
import random
class enemy():
    def __init__(self, hpmin, hpmax, dmgmin, dmgmax, spd, inv):
        self.hpmin = hpmin
        self.hpmax = hpmax
        self.dmgmin = dmgmin
        self.dmgmax = dmgmax
        self.spd = spd
        self.inv = inv

enemylist = {
    'undead': {
        'Skeleton': enemy(4, 6, 1, 2, 3, ['Bone']),
    },
    'nature': {
        'Bear': enemy(10, 20, 6, 12, 6, [])
    }
}
