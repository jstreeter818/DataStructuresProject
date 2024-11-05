def load_map():
    with open('map.txt', 'r') as file:
        map_lines = file.readlines()
    return map_lines

def print_map():
    map_lines = load_map()
    for line in map_lines:
        print(line)

