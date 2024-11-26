'''containts initializations of all characters, rooms, items'''

import characters.player_class as player_class
import rooms.room_class as room_class
import characters.character_class as character_class
import items.item_class as item_class
import items.item_actions as item_actions
import characters.npc_actions as npc_actions
import time
import items.item_descriptions as item_descriptions

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
hallway.connect("east", library)
hallway.connect("west", main_gallery)
hallway.connect("north", courtyard)
mail_room.connect("south", closet)
main_gallery.connect("north", portrait_gallery)
portrait_gallery.connect("north", bathrooms)
library.connect("east", storage)
courtyard.connect("east", cafe)
cafe.connect("north", sculpture_garden)

foyer.visited = True

player = player_class.Player("Name", foyer)

# prompt user for their name and confirm    
player_name = input("Enter your name: ")
confirm = input("Confirm '" + player_name + "'? (y/n) ").strip().casefold()

# allows user to re-enter a name until they confirm
while confirm not in ['y', 'yes']:
    if confirm not in ['n', 'no']:
        print("'" + confirm + "' is not a valid command.")
        time.sleep(0.5)
        confirm = input("Confirm '" + player_name + "'? (y/n) ").strip().casefold()
    if confirm in ['n', 'no']:
        player_name = input("Enter your name: ")
        confirm = input("Confirm '" + player_name + "'? (y/n) ").strip().casefold()
    
# welcomes player by name and initializes player object
if confirm in ['y', 'yes']:
    print("Welcome, " + player_name)
    player.set_name(player_name)
    time.sleep(1)

# items
chandelier = item_class.Item("Chandelier", item_descriptions.chandelier, foyer, True)
foyer.items.append(chandelier)

painting = item_class.Item("Landscape Painting", item_descriptions.landscape_painting, main_gallery, True)
main_gallery.items.append(painting)

old_tome = item_class.Item("Old tome", item_descriptions.old_tome, library, use_func=item_actions.read_tome)
library.items.append(old_tome)

map = item_class.Item("Map", ["A map of the museum"], location=None, use_func=item_actions.print_map)

lamp = item_class.Item("Strange lamp", item_descriptions.lamp, portrait_gallery, static=True, use_func=item_actions.use_lamp)
portrait_gallery.items.append(lamp)

cat_treats = item_class.Item("Cat treats", item_descriptions.cat_treats, cafe)
cafe.items.append(cat_treats)

decoder = item_class.Item("Decoder", item_descriptions.decoder, secret_room)
secret_room.items.append(decoder)

stone_statue = item_class.Item("Stone statue", item_descriptions.stone_statue, sculpture_garden, static=True)
sculpture_garden.items.append(stone_statue)

water_fountain = item_class.Item("Water fountain", item_descriptions.water_fountain, courtyard, static=True)
courtyard.items.append(water_fountain)

coin = item_class.Item("Coin", item_descriptions.coin, mail_room, use_func=item_actions.toss_coin)
mail_room.items.append(coin)

# characters
characters = []

Duncan = character_class.Character("Duncan", "squeezly...?", foyer) # Duncan Akins
Duncan.dialogues.add(None, ". . .", left_key="ring bell", right_key="clear throat", action=lambda: print("He's slumped over the desk... snoring."))
Duncan.dialogues.add('0', "Goodness! My apologies for the lack of professionalism, that's quite embarrassing on my part. How silly to let myself fall asleep on the job.")
Duncan.dialogues.add('1', "Goodness! My apologies for the lack of professionalism, that's quite embarrassing on my part. How silly to let myself fall asleep on the job.")
Duncan.dialogues.add('00', "Welcome to Cairn's Keep. You don't look like you've been here before. It is really quite nice to see a new face stopping in.")
Duncan.dialogues.add('10', "Welcome to Cairn's Keep. You don't look like you've been here before. It is really quite nice to see a new face stopping in.")
Duncan.dialogues.add('000', "Oh, my name's Duncan. I'm the owner and founder, but I also help keep the place running. It's truly a pleasure to meet you...")
Duncan.dialogues.add('100', "Oh, my name's Duncan. I'm the owner and founder, but I also help keep the place running. It's truly a pleasure to meet you...")
Duncan.dialogues.add('0000', (player.name + "!"), action=lambda: npc_actions.handshake(Duncan))
Duncan.dialogues.add('1000', (player.name + "!"), action=lambda: npc_actions.handshake(Duncan))
Duncan.dialogues.add('00000', "Well I'll let you explore this place on your own. Here's a map of the building to help you get around.", action=npc_actions.give_map)
Duncan.dialogues.add('10000', "Well I'll let you explore this place on your own. Here's a map of the building to help you get around.", action=npc_actions.give_map)
Duncan.dialogues.add('000000', "If you have any questions, I'll be around, so don't be afraid to ask. Enjoy your visit at Cairn's Keep!", pause=True)
Duncan.dialogues.add('100000', "If you have any questions, I'll be around, so don't be afraid to ask. Enjoy your visit at Cairn's Keep!", pause=True)
Duncan.dialogues.add('0000000', "The stone used to construct Cairn's Keep was actually sourced locally from the area when it was built. There's a lot of history to this place.", checkpoint=True)
Duncan.dialogues.add('1000000', "The stone used to construct Cairn's Keep was actually sourced locally from the area when it was built. There's a lot of history to this place.", checkpoint=True)

Eugene = character_class.Character("Eugene", "A short stout man wearing a security uniform.", foyer)
Eugene.dialogues.add(None, "My, it's been a while since I've seen a new face around here. Welcome to Cairn's Keep, historic museum.")
Eugene.dialogues.add('0', "My name is Eugene. I'm the security around here, though there's not much need for security when people don't come around here like they used to...")
Eugene.dialogues.add('00', "But anyways, you are...?")
Eugene.dialogues.add('000', ("Pleasure to meet you, " + player.name + ". Here, take this."), action=npc_actions.give_map)
Eugene.dialogues.add('0000', "Well, enjoy your visit, and if you have any questions, don't be afriad to ask, I'll be around.", action=lambda: Eugene.move_rooms(main_gallery))

#Eugene.dialogues.add('00', "May I ask a favor of you...?")
#Eugene.dialogues.add('000', "Well... there's a library somewhere around here... and a certain book I'm looking for. Think you can find it and bring it to me?", left_key="yes", right_key="no")
#Eugene.dialogues.add('0000', "Magnificent! Return to me here once you've found the book.", checkpoint=True, checkpoint_condition=lambda: old_tome in player.inventory) # checkpoint condition as lambda to check during runtime
#Eugene.dialogues.add('0001', "I didn't think you'd actually refuse...", checkpoint=True, checkpoint_condition=lambda: old_tome in player.inventory)
#Eugene.dialogues.add('00000', "You found the book! Brilliant! Let me take a look...")
#Eugene.dialogues.add('00010', "Ah, you went and found it anyways. Well let me take a look, will you?")
#Eugene.dialogues.add('000000', "Ah, just as I thought. I must go check something now, excuse me.", checkpoint=True, checkpoint_condition=lambda: player.location is courtyard, action=lambda: Eugene.move_rooms(courtyard))
#Eugene.dialogues.add('000100', "Ah, just as I thought. I must go check something now, excuse me.", checkpoint=True, checkpoint_condition=lambda: player.location is courtyard, action=lambda: Eugene.move_rooms(courtyard))
#Eugene.dialogues.add('0000000', ("Hello, " + player.name + ". This book you found, it has secrets about this museum..."))
#Eugene.dialogues.add('0001000', ("Hello, " + player.name + ". This book you found, it has secrets about this museum..."))
#Eugene.dialogues.add('00000000', "You may have noticed the contents of the book are written in an obscure script. I'm not sure what it is, but I swear I've seen these symbols somewhere.")
#Eugene.dialogues.add('00010000', "You may have noticed the contents of the book are written in an obscure script. I'm not sure what it is, but I swear I've seen these symbols somewhere.")
#Eugene.dialogues.add('000000000', "There must be some way to decipher this code. I believe there is something important written here.", True, checkpoint_condition=lambda: decoder in player.inventory)
#Eugene.dialogues.add('000100000', "There must be some way to decipher this code. I believe there is something important written here.", True, checkpoint_condition=lambda: decoder in player.inventory)
#Eugene.dialogues.add('0000000000', ("What's that? You found a decoder for the tome? How marvelous. You, " + player.name + ", are quite the clever nut aren't you!"))
#Eugene.dialogues.add('0001000000', ("What's that? You found a decoder for the tome? How marvelous. You, " + player.name + ", are quite the clever nut aren't you!"))

black_cat = character_class.Character("Black cat", "A lanky black cat, its eyes narrow as you gaze at it.", foyer)
black_cat.dialogues.add(None, 'Mrowww', checkpoint=True, checkpoint_condition=lambda: cat_treats in player.inventory)
black_cat.dialogues.add('0', "*sniff sniff*", left_key="give treat", right_key="give all treats")
black_cat.dialogues.add('00', "Mrow! *crunch crunch*")
black_cat.dialogues.add('01', "Purrrr *crunch crunch*", action=lambda: player.inventory.remove(cat_treats))
black_cat.dialogues.add('000', "Mrowww", checkpoint=True)
black_cat.dialogues.add('010', "Mrowww.", checkpoint=True)

librarian = character_class.Character("Librarian", "The museum librarian", library)
librarian.dialogues.add(None, "Hello there, you've found historic Cairn's library.")

foyer.characters.append(Eugene)
foyer.characters.append(black_cat)
foyer.characters.append(Duncan)

library.characters.append(librarian)

characters.append(Eugene)
characters.append(black_cat)
characters.append(librarian)
characters.append(Duncan)
