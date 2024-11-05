class Item:
    def __init__(self, name, description, location, static = False, use_func = None):
        self.name = name
        self.description = description
        self.location = location
        self.picked_up = False
        self.use_func = use_func
        # static cannot be picked up
        self.static = static
        self.been_used = False

    def use_item(self):
        action = self.use_func
        action()

    def print_item_description(self):
        print("You look closely at the " + self.name)
        print(self.description)
