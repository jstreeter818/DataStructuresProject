'''contains initializations of character objects as well as player'''

import characters.player_class as player_class
import characters.character_class as character_class
import game_objects.rooms as rooms
import time

player = player_class.Player("Name", rooms.foyer)

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

import dialogue.dialogues as dialogues
characters = []

Duncan = character_class.Character("Duncan", "squeezly...?", rooms.foyer, dialogues.Duncan_Dialogue)
black_cat = character_class.Character("Black cat", "A lanky black cat, its eyes narrow as you gaze at it.", rooms.foyer, dialogues.BlackCat_Dialogue)

rooms.foyer.characters.append(black_cat)
rooms.foyer.characters.append(Duncan)

characters.append(black_cat)
characters.append(Duncan)
