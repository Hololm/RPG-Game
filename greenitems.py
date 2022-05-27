class item():
    def __init__(self, type, minvalue, maxvalue, spd):
        self.type = type
        self.minvalue = minvalue
        self.maxvalue = maxvalue
        self.spd = spd

itemlist = {
    'lgweapons': {
        'Damaged Shortsword': item('attack', 2, 4, 6),
        #'Cracked Broadsword': item('attack', 3, 5, 5),
        #'Broken Claymore': item('attack', 5, 7, 3)
    },
    'mgweapons': {
        'Shortsword': item('attack', 5, 7, 6),
        'Broadsword': item('attack', 7, 9, 5),
        'Claymore': item('attack', 10, 12, 3)
    },
    'hgweapons': {
        'Engraved Shortsword': item('attack', 8, 10, 6),
        'Royal Broadsword': item('attack', 11, 13, 5),
        'Highland Claymore': item('attack', 15, 17, 3)
    },
    'lghealing': {
        'Bandage': item('heal', 7, 9, 10)
    },
    'mghealing': {
        'Small Health Flask': item('heal', 11, 13, 10)
    },
    'hghealing': {
        'Health Potion': item('heal', 15, 17, 10)
    },
    'lggeneral': {

    },
    'mggeneral': {

    },
    'hggeneral': {

    },
}