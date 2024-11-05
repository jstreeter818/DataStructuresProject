import time

# all the commands
def talk(location, character_name):
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
    
    for item in location.items:
        if look_at == item.name:
            item.print_item_description()
            return
    
    print("There is no '" + look_at + "' to look at.")
    time.sleep(1)

def move(player, location, direction):
    while direction not in location.connections:
        print("You cannot move " + direction + " from here.")
        time.sleep(1)
        location.print_viable_moves()
        time.sleep(1)
        direction = input("Which direction do you want to move? ").strip().casefold()

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
    for item in location.items:
        if item.name.casefold() == to_get:
            if not item.static:
                player.inventory.append(item)
                item.picked_up = True
                item.location = None
                location.items.remove(item)
                print("You pick up " + item.name + " and put it in your inventory.")
                time.sleep(1)
                return
            else:
                print(item.name + " cannot be picked up.")
                time.sleep(1)
                return
    print("There is no '" + to_get + "' to get here.")
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
    print("'" + object + "' is not in your inventory.")
    time.sleep(1)