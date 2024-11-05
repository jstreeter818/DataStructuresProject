class Player:
    def __init__(self, name, location):
        self.name = name
        self.location = location
        self.rooms_visited = set()
        self.inventory = []

    def set_name(self, name):
        self.name = name
    
    def print_inventory(self):
        if len(self.inventory) == 0:
            print("Your inventory is empty.")
        else:    
            print("Items in your inventory:", end = " ")
            for i in range(len(self.inventory)):
                if i < len(self.inventory) - 1:
                    print(str(self.inventory[i].name), end = ", ")
                else:
                    print(str(self.inventory[i].name) + ".")
