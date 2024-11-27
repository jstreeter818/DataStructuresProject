'''contains functions for evaluating quest advancement'''
from objects.game_objects import player

def item_in_inventory(item):
    return item in player.inventory

def room_visited(room):
    return room.visited

def item_been_used(item):
    return item.been_used
