def handshake(character_name):
    print("*" + character_name + " shakes your hand*")

def give_map():
    from game_objects.characters import player
    from game_objects.items import map
    player.inventory.append(map)
    map.picked_up = True
    print("*Duncan hands you a map of the museum, and you place it in your inventory*")