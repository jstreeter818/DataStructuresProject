'''contains functions associated with using items'''
import items.item_descriptions as item_descriptions
import rooms.room_descriptions as room_descriptions
import time

def load_map():
    from game_objects.rooms import secret_room
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
    from game_objects.rooms import secret_room
    secret_room.unlock()

def read_tome():
    from game_objects.characters import player
    from game_objects.items import decoder
    if decoder in player.inventory:
        print("You use the decoder to translate the contents of the old tome.")
    else:
        print("You open the book and try to decipher the script, but it means absolutely nothing to you.")

def toss_coin():
    from game_objects.characters import player
    from game_objects.items import coin
    if player.location.name == "Courtyard":
        print("You make a silent wish to yourself, then toss the coin into the water.")
        player.inventory.remove(coin)
    else:
        print("You flip the coin into the air, and it lands back in your palm, heads up.")

def fix_clock():
    from game_objects.items import broken_clock
    from items.item_descriptions import fixed_clock
    print("There's something keeping the gears from turning right...")
    time.sleep(1)
    print("It's an old wad of gum stuck in the gears!")
    time.sleep(1)
    print("You remove the gum and fix the clock")
    broken_clock.use_func = None
    broken_clock.name = "Grandfather Clock"
    broken_clock.description = fixed_clock

def open_box():
    from game_objects.items import stool, lock_box
    from game_objects.characters import player
    from game_objects.rooms import mail_room
    if stool.location == mail_room:
        print("You step up onto the stool and reach for the box.")
        time.sleep(1)
        print("A plume of dust erupts from the disturbance. You cough, dropping the crate, where a letter slips out.")
        time.sleep(1)
        print("You take a closer look at the letter. 'Lawsuit' is written in big letters at the top...")
        time.sleep(1)
        print("A quick scan reveals the phrases 'wrongful death', and 'safety violations'...")
        time.sleep(1)
        print("You quickly put the letter back in the box and take it with you.")
        player.inventory.append(lock_box)
        lock_box.picked_up = True
        lock_box.location = None
        mail_room.items.remove(lock_box)

        # change item description
        lock_box.description = item_descriptions.lock_box_2
        # change room description
        mail_room.long_description = room_descriptions.mail_room_2

    else:
        print("You reach for the box, but it's too high up.")

def place_stool():
    from game_objects.characters import player
    from game_objects.items import stool
    stool.location = player.location
    player.location.items.append(stool)
    player.inventory.remove(stool)
    print("You place the stool and pray the old wood holds.")