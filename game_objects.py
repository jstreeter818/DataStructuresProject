import player_class
import room_class
import character_class
import item_class
import item_actions as actions
import time

# Rooms
rooms = []

foyer = room_class.Room("Foyer", "(Dust and shadows fill the grand foyer, where a tarnished chandelier barely glimmers above, hinting at an elegance lost to time.)")
hallway = room_class.Room("Hallway", "(Flickering sconces illuminate this hallway's faded mahogany floors.)")
closet = room_class.Room("Closet", "(The coats in this closet smell like woodrot...)")
mail_room = room_class.Room("Mail room", "(This old mail room reeks of silverfish, and stacks of upopened letters are scattered everywhere.)")
main_gallery = room_class.Room("Main Gallery", "(Great wandering landscapes fill the large ornate frames on these walls.)")
library = room_class.Room("Library", "(A fair sized library full of ancient tomes and historical documents.)")
storage = room_class.Room("Storage", "(A room full of cobwebs, tools, and old display pieces.)")
courtyard = room_class.Room("Courtyard", "(Overgrown vines and cracked stones surround a worn fountain, filling the courtyard with an eerie tranquility that echoes in the silence.)")
portrait_gallery = room_class.Room("Portrait gallery", "(Old yellowed wallpaper peels at the edges of the room, filled with portraits that give you an uneasy feeling...)")
cafe = room_class.Room("Cafe", "(The cafe sits unsettlingly pristine, every table perfectly set as if expecting visitors, despite the emptiness all around.)")
secret_room = room_class.Room("Secret Room", "(Secret room)")
bathrooms = room_class.Room("Bathrooms", "(It doesn't look like anyone's been in here in a while... aside from some mice heard in the walls.)")
sculpture_garden = room_class.Room("Sculpture Garden", "(The sculpture garden looms in silence, and something about these statues make you feel like you're being watched...)")

rooms.append(foyer)
rooms.append(hallway)
rooms.append(closet)
rooms.append(mail_room)
rooms.append(main_gallery)
rooms.append(library)
rooms.append(storage)
rooms.append(courtyard)
rooms.append(portrait_gallery)
rooms.append(cafe)
rooms.append(secret_room)
rooms.append(bathrooms)
rooms.append(sculpture_garden)

foyer.connect("north", hallway)
foyer.connect("east", mail_room)

hallway.connect("south", foyer)
hallway.connect("east", library)
hallway.connect("west", main_gallery)
hallway.connect("north", courtyard)

mail_room.connect("west", foyer)
mail_room.connect("south", closet)

closet.connect("north", mail_room)   

main_gallery.connect("east", hallway)
main_gallery.connect("north", portrait_gallery)

portrait_gallery.connect("south", main_gallery)
portrait_gallery.connect("west", secret_room)
portrait_gallery.connect("north", bathrooms)

secret_room.connect("east", portrait_gallery)

bathrooms.connect("south", portrait_gallery)

library.connect("west", hallway)
library.connect("east", storage)

storage.connect("west", library)

courtyard.connect("south", hallway)
courtyard.connect("east", cafe)

cafe.connect("west", courtyard)
cafe.connect("north", sculpture_garden)

sculpture_garden.connect("south", cafe)

foyer.visited = True

# player
player = player_class.Player("Name", foyer)

#"""

# prompt user for their name and confirm    
player_name = input("Enter your name: ")
confirm = input("Confirm '" + player_name + "'? (y/n) ").strip().casefold()

# allows user to re-enter a name until they confirm
while confirm != "y":
    if confirm != "n":
        print("'" + confirm + "' is not a valid command.")
        time.sleep(0.5)
        confirm = input("Confirm '" + player_name + "'? (y/n) ").strip().casefold()
    if confirm == "n":
        player_name = input("Enter your name: ")
        confirm = input("Confirm '" + player_name + "'? (y/n) ").strip().casefold()
    
# welcomes player by name and initializes player object
if confirm == "y":
    print("Welcome, " + player_name)
    player.set_name(player_name)
    time.sleep(1)

#"""

# items
old_tome = item_class.Item("Old tome", "A tattered leather tome with pages full of a mysterious script.", library)
library.items.append(old_tome)

map = item_class.Item("Map", "A map of the museum", location=None, use_func=actions.print_map)
map.picked_up = True
player.inventory.append(map)

lamp = item_class.Item("Strange lamp", "There's something off about this lamp...", portrait_gallery, static=True)
portrait_gallery.items.append(lamp)

cat_treats = item_class.Item("Cat treats", "An opened bag of cat treats,", cafe)
cafe.items.append(cat_treats)

# characters
characters = []

old_man = character_class.Character("Old man", "An old man lurks in the shadows... he's holding a small bag.", foyer)
old_man.dialogues.add(None, "Hello, traveler. What shall I call you?")
old_man.dialogues.add('0', ('Ahh, ' + player.name + ', welcome to the museum.'))
old_man.dialogues.add('00', "May I ask a favor of you...?")
old_man.dialogues.add('000', "Well... there's a library somewhere around here... and a certain book I'm looking for. Think you can find it and bring it to me?", left_key="yes", right_key="no")
old_man.dialogues.add('0000', "Magnificent! Return to me here once you've found the book.", checkpoint=True, checkpoint_condition=lambda: old_tome in player.inventory) # checkpoint condition as lambda to check during runtime
old_man.dialogues.add('0001', "I didn't think you'd actually refuse...", checkpoint=True, checkpoint_condition=lambda: old_tome in player.inventory)
old_man.dialogues.add('00000', "You found the book! Brilliant! Let me take a look...")
old_man.dialogues.add('00010', "Ah, you went and found it anyways. Well let me take a look, will you?")
old_man.dialogues.add('000000', "Ah, just as I thought. I must go check something now, excuse me.", checkpoint=True, checkpoint_condition=lambda: player.location is courtyard, action=lambda: old_man.move_rooms(courtyard))
old_man.dialogues.add('000100', "Ah, just as I thought. I must go check something now, excuse me.", checkpoint=True, checkpoint_condition=lambda: player.location is courtyard, action=lambda: old_man.move_rooms(courtyard))
old_man.dialogues.add('0000000', ("Hello, " + player.name + ". This book you found, it has secrets about this museum..."), True)
old_man.dialogues.add('0001000', ("Hello, " + player.name + ". This book you found, it has secrets about this museum..."), True)

black_cat = character_class.Character("Black cat", "A lanky black cat, its eyes narrow as you gaze at it.", foyer)
black_cat.dialogues.add(None, 'Mrowww', checkpoint=True, checkpoint_condition=lambda: cat_treats in player.inventory)
black_cat.dialogues.add('0', "The cat sniffs your bag that holds the cat treats. It obviously wants some.", left_key="give treat", right_key="give all treats")
black_cat.dialogues.add('00', "You give the cat a treat and purrs immediately follow")
black_cat.dialogues.add('01', "You dump out the entire bag of treats for the cat who appears very happy because of this", action=lambda: player.inventory.remove(cat_treats))
black_cat.dialogues.add('000', "Mrowww", checkpoint=True)
black_cat.dialogues.add('010', "Mrowww.", checkpoint=True)

foyer.characters.append(old_man)
foyer.characters.append(black_cat)

characters.append(old_man)
characters.append(black_cat)

