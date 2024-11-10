def load_map():
    from game_objects import secret_room
    if secret_room.visited:
        with open('map_secret_room_unlocked.txt', 'r') as file:
            map_lines = file.readlines()
    else:
        with open('map_secret_room_locked.txt', 'r') as file:
            map_lines = file.readlines()
    return map_lines

def print_map():
    map_lines = load_map()
    for line in map_lines:
        print(line)

