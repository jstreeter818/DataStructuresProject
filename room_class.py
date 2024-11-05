import time

# a Room class to make different room objects where the player can move to and from
class Room:
    def __init__(self, name, description):
        self.name = name
        self.description = description
        self.connections = {}
        self.characters = []
        self.items = []
        self.visited = False
        
    # connects the room to another by a certain cardinal direction
    def connect(self, direction, room):
        self.connections[direction] = room
        
    # prints a list of viable moves in the room
    def print_viable_moves(self):
        directions = []

        for direction in self.connections:
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