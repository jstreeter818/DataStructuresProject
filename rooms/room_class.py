import time

# a Room class to make different room objects where the player can move to and from
class Room:
    def __init__(self, name, main_description, long_description):
        self.name = name
        self.main_description = main_description
        self.long_description = long_description
        self.connections = {}
        self.characters = []
        self.items = []
        self.visited = False
        self.looked_at = False
        self.locked = False
        
    # connects the room to another by a certain cardinal direction
    def connect(self, direction, room):
        self.connections[direction] = room

        if direction == "north":
            opposite_direction = "south"
        elif direction == "south":
            opposite_direction = "north"
        elif direction == "east":
            opposite_direction = "west"
        elif direction == "west":
            opposite_direction = "east"
        
        room.connections[opposite_direction] = self
        
    # prints a list of viable moves in the room
    def print_viable_moves(self):
        directions = []

        for direction in self.connections:
            room = self.connections[direction]
            if not room.locked:
                directions.append(direction)

        print("You can move", end = " ")

        for i in range(len(directions)):
            if i < len(directions) - 1:
                print(directions[i], end = ", ")
            else:
                print(directions[i] + ".")

    # prints a list of all characters in the room
    def print_all_characters(self):
        print("In the room you see:", end = " ")

        if len(self.characters) == 0:
            print("nobody.")

        for i in range(len(self.characters)):
            if i < len(self.characters) - 1:
                print(str(self.characters[i].name), end = ", ")
            else:
                print(str(self.characters[i].name) + ".")

    def print_items_in_room(self):
        self.looked_at = True
        
        print("You look around the " + self.name + " and spot:", end = " ")

        if len(self.items) == 0:
            print("the complete lack of anything interesting.")

        else:
            for i in range(len(self.items)):
                if i < len(self.items) - 1:
                    print(str(self.items[i].name), end = ", ")
                else:
                    print(str(self.items[i].name) + ".")
            time.sleep(1)
    
    def unlock(self):
        self.locked = False