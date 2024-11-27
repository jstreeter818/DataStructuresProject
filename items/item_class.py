import time

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
        self.looked_at = False

    def use_item(self):
        self.use_func()
        self.been_used = True
        time.sleep(1)


    def look_item(self):
        self.looked_at = True
        print("You look closely at the " + self.name)
        time.sleep(1)

        for line in self.description:
            print(line)
            time.sleep(1)