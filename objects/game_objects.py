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
portrait_gallery.connect("west", secret_room)

foyer.visited = True
secret_room.locked = True

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
broken_clock = item_class.Item("Broken Clock", item_descriptions.broken_clock, foyer, True, item_actions.fix_clock)
foyer.items.append(broken_clock)

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
import dialogue.dialogues as dialogues
characters = []

Duncan = character_class.Character("Duncan", "squeezly...?", foyer, dialogues.Duncan_Dialogue) # Duncan Akins
black_cat = character_class.Character("Black cat", "A lanky black cat, its eyes narrow as you gaze at it.", foyer, dialogues.BlackCat_Dialogue)

foyer.characters.append(black_cat)
foyer.characters.append(Duncan)

characters.append(black_cat)
characters.append(Duncan)
