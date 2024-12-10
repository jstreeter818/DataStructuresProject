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
    if look_at == 'room':
        look_at = player.location.name.casefold()

    if look_at == location.name.casefold():
        for line in location.long_description:
            print(line)
            time.sleep(1)
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
                item.look_item()
                return
    
    for item in player.inventory:
        if look_at == item.name.casefold():
            item.look_item()
            return
    
    print("There is no '" + look_at + "' to look at.")
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

def inventory(player):
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
                    item.look_item()
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

def commands():
    print("Here is an explanation on how to use commands.")
    time.sleep(1)
    print("Valid commands are: talk, look, move, use, get, inventory, quit, and commands.")
    time.sleep(1)
    print("You can also use just the first letter of each command. So 't' is the same as 'talk', for example.")
    time.sleep(1)
    print("Some commands can take additional arguments. Talk, look, move, use, and get all can take arguments.")
    time.sleep(1)
    print("For commands that take arguments, type the command followed by the argument, with no additional filler words.")
    time.sleep(1)
    print("For example, for move, you can type 'move north' or 'm n'. For directional arguments, you can also just enter the first letter of the direction.")
    time.sleep(1)
    print("For talk, look, use, and get, the argument is the name of the character, item, or room.")
    time.sleep(1)
    print("To look around a room, you can enter 'look [room name]', or just 'look room'.")
    time.sleep(1)
    print("Commands and arguments are NOT case sensitive, but you must spell them correctly, including spaces if an argument has spaces.")
    time.sleep(1)