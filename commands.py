import time

# all the commands
def talk(location, character_name):
    if 'to' in character_name.split():
        print("Make sure when using the talk command to just type 'talk' or 't' followed directly by the character's name, rather than 'talk to [character name]'")
        time.sleep(1)

    # find character to talk to    
    for character in location.characters:
        if character.name.lower() == character_name:
            character.print_dialogue()
            time.sleep(1)
            return
    print(character_name + " is not here.")
    time.sleep(1)
    

def look(player, location, look_at):
    if look_at == location.name.casefold():
        location.print_items_in_room()
        return

    for character in location.characters:
        if look_at == character.name.casefold():
            character.print_character_description()
            return
    
    # player must have looked at the room first before looking at items in room
    if location.looked_at:
        for item in location.items:
            if look_at == item.name.casefold():
                item.print_item_description()
                return
    
    print("There is no '" + look_at + "' to look at.")
    time.sleep(1)
    print("To 'look' at something or someone, use the command 'look' or 'l' followed by the item, room, or character's name.")
    time.sleep(1)

def move(player, location, direction):
    if direction == 'n':
        direction = 'north'
    if direction == 's':
        direction = 'south'
    if direction == 'e':
        direction = 'east'
    if direction == 'w':
        direction = 'west'

    while direction not in location.connections:
        print("You cannot move " + direction + " from here.")
        time.sleep(1)
        location.print_viable_moves()
        time.sleep(1)
        direction = input("Which direction do you want to move? ").strip().casefold()

        if direction == 'n':
            direction = 'north'
        if direction == 's':
            direction = 'south'
        if direction == 'e':
            direction = 'east'
        if direction == 'w':
            direction = 'west'

    if direction in location.connections:
        new_location = location.connections[direction]
        print("You move " + direction + " into the " + new_location.name)
        new_location.visited = True
        player.location = new_location

        # add room to set of rooms visited
        player.rooms_visited.add(new_location)
    time.sleep(1)

def inventory(player, location):
    player.print_inventory()
    time.sleep(1)

def get(player, location, to_get):
    # player must have looked at room before getting items from room
    if location.looked_at:

        for item in location.items:

            if item.name.casefold() == to_get:
                if not item.static:
                    player.inventory.append(item)
                    item.picked_up = True
                    item.location = None
                    location.items.remove(item)
                    item.print_item_description()
                    time.sleep(1)
                    print("You pick up " + item.name + " and put it in your inventory.")
                    time.sleep(1)
                    return
                else:
                    print(item.name + " cannot be picked up.")
                    time.sleep(1)
                    return
        
        print("You cannot get '" + to_get + "'.")
        time.sleep(1)
                
    else:
        print("You must first look around the room before getting anything.")
        time.sleep(1)
            

def use(player, location, object):
    for item in player.inventory:
        if item.name.casefold() == object:
            if item.use_func:
                print("You use " + item.name + ".")
                time.sleep(1)
                item.use_item()
                time.sleep(1)
                return
            else:
                print(item.name + " cannot be used.")
                time.sleep(1)
                return
    
    for item in location.items:
        if item.name.casefold() == object:

            # player must have looked at item first to be able to use it
            if item.looked_at:
                if item.use_func:
                    print("You use " + item.name + ".")
                    time.sleep(1)
                    item.use_item()
                    time.sleep(1)
                    return
                else:
                    print(item.name + " cannot be used.")
                    time.sleep(1)
                    return

    print("'" + object + "' is not in your inventory.")
    time.sleep(1)