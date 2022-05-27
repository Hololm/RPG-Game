from collections import Counter


class Item:
    def __init__(self, description, function):
        self.description = description
        self.function = function

    def item_function(self, enemy):

        inv_count = dict(sorted(dict(Counter(self.inv)).items()))

        item_name = input(f"\n{inv_count}\nWhat item?\n>> ").title()

        for item_choice in items_collection:
            if item_name in items_collection[item_choice]:
                if item_name in self.inv:
                    print("{} used the {}!".format(self.name, item_name))

                    if item_choice == 'healing items':
                        self.hp += items_collection[item_choice][item_name].function

                    elif item_choice == 'general items':
                        return items_collection[item_choice][item_name].function

                    elif item_choice == 'buff items':
                        self.dmg += items_collection[item_choice][item_name].function

                    self.inv.remove(item_name)

                else:
                    print("Could not find the item...".format(self.name))


items_collection = {
    # name, description, function
    'healing items': {

        'Estus Flask': Item('ill heal yer wounds, hyuck!', 5),
    },

    'general items': {
        'Golden Bag of Holding': Item('its golden and its a bag.', None),
    },

    'buff items': {

        'Beets': Item('your arms be big like UUUGHH YEAH.', 3),
    },
}
