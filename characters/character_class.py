import time
import dialogue.dialogue_tree as dialogue_tree
# Character class to make NPC's
class Character:
    def __init__(self, name, description, location, dialogue):
        self.name = name
        self.description = description
        self.location = location
        self.dialogue = dialogue

    # Move character to a new room
    def move_rooms(self, room):
        self.location.characters.remove(self)
        self.location = room
        self.location.characters.append(self)
    
    # print character dialogue
    def print_dialogue(self):
        if self.dialogue.head == None:
            print(self.name + " has nothing to say to you.")
        else:
            print("You talk to " + self.name)
            time.sleep(1)
            self.dialogue.traverse_dialogue(self.dialogue.head, self.name)

    def print_character_description(self):
        print("You take a close look at " + self.name)
        print(self.description)
        time.sleep(1)