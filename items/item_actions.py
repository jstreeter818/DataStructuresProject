'''contains functions associated with using items'''
import time

def load_map():
    from objects.game_objects import secret_room
    if not secret_room.locked:
        with open('main\map_secret_room_unlocked.txt', 'r') as file:
            map_lines = file.readlines()
    else:
        with open('main\map_secret_room_locked.txt', 'r') as file:
            map_lines = file.readlines()
    return map_lines

def print_map():
    map_lines = load_map()
    for line in map_lines:
        print(line)

def use_lamp():
    print("You fiddle with the lamp a bit until you notice a large portrait on the west side of the room sliding to reveal a hidden door.")
    from objects.game_objects import secret_room
    secret_room.unlock()

def read_tome():
    from objects.game_objects import player, decoder
    if decoder in player.inventory:
        print("You use the decoder to translate the contents of the old tome.")
    else:
        print("You open the book and try to decipher the script, but it means absolutely nothing to you.")

def toss_coin():
    from objects.game_objects import player, coin
    if player.location.name == "Courtyard":
        print("You make a silent wish to yourself, then toss the coin into the water.")
        player.inventory.remove(coin)
    else:
        print("You flip the coin into the air, and it lands back in your palm, heads up.")

def fix_clock():
    from objects.game_objects import broken_clock
    from items.item_descriptions import fixed_clock
    print("There's something keeping the gears from turning right...")
    time.sleep(1)
    print("It's an old wad of gum stuck in the gears!")
    time.sleep(1)
    print("You remove the gum and fix the clock")
    broken_clock.use_func = None
    broken_clock.name = "Grandfather Clock"
    broken_clock.description = fixed_clock