'''contains initialization of room objects'''

import rooms.room_descriptions as room_descriptions
import rooms.room_class as room_class

rooms = []

foyer = room_class.Room("Foyer", "(Dust and shadows fill the grand foyer, where a tarnished chandelier barely glimmers above, hinting at an elegance lost to time.)", room_descriptions.foyer)
hallway = room_class.Room("Hallway", "(Flickering sconces illuminate this hallway's faded mahogany floors.)", room_descriptions.hallway)
closet = room_class.Room("Closet", "(The coats in this closet smell like woodrot...)", room_descriptions.closet)
mail_room = room_class.Room("Mail room", "(This old mail room reeks of silverfish, and stacks of upopened letters are scattered everywhere.)", room_descriptions.mail_room)
main_gallery = room_class.Room("Main Gallery", "(Great wandering landscapes fill the large ornate frames on these walls.)", room_descriptions.main_gallery)
library = room_class.Room("Library", "(A fair sized library full of ancient tomes and historical documents.)", room_descriptions.library)
study = room_class.Room("Study", "(A room full of cobwebs, tools, and old display pieces.)", room_descriptions.study)
courtyard = room_class.Room("Courtyard", "(Overgrown vines and cracked stones surround a worn fountain, filling the courtyard with an eerie tranquility that echoes in the silence.)", room_descriptions.courtyard)
portrait_gallery = room_class.Room("Portrait gallery", "(Old yellowed wallpaper peels at the edges of the room, filled with portraits that give you an uneasy feeling...)", room_descriptions.portrait_gallery)
cafe = room_class.Room("Cafe", "(The cafe sits unsettlingly pristine, every table perfectly set as if expecting visitors, despite the emptiness all around.)", room_descriptions.cafe)
secret_room = room_class.Room("Secret Room", "(Secret room)", room_descriptions.secret_room)
bathrooms = room_class.Room("Bathrooms", "(It doesn't look like anyone's been in here in a while... aside from some mice heard in the walls.)", room_descriptions.bathrooms)
sculpture_garden = room_class.Room("Sculpture Garden", "(The sculpture garden looms in silence, and something about these statues make you feel like you're being watched...)", room_descriptions.sculpture_garden)

rooms.append(foyer)
rooms.append(hallway)
rooms.append(closet)
rooms.append(mail_room)
rooms.append(main_gallery)
rooms.append(library)
rooms.append(study)
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
library.connect("east", study)
courtyard.connect("east", cafe)
cafe.connect("north", sculpture_garden)
portrait_gallery.connect("west", secret_room)

foyer.visited = True
secret_room.locked = True