def handshake(character):
    print("*" + character.name + " shakes your hand*")

def give_map():
    from game_objects import player, map
    player.inventory.append(map)
    map.picked_up = True
    print("*Duncan hands you a map of the museum, and you place it in your inventory*")