'''contains action functions to be executed during quest nodes'''
from objects.game_objects import player

def give_item(character, item):
    print("*" + character.name + "hands you '" + item.name + "', and you place it in your inventory*")
    player.inventory.append(item)

def unlock_room(room):
    room.unlock()

def remove_from_inventory(item):
    player.inventory.remove(item)

def change_item_name(item, new_name):
    item.name = new_name

def change_item_description(item, new_description):
    item.description = new_description