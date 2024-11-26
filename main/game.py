import time
import objects.game_objects as game_objects
from main.commands import talk, look, move, use, inventory, get, commands

def main():

    # library mapping valid command strings to command
    valid_commands = {"talk": talk,
                      "t": talk,
                      "look": look,
                      "l": look,
                      "move": move,
                      "m": move,
                      "quit": quit,
                      "q": quit,
                      "inventory": inventory,
                      "i": inventory,
                      "use": use,
                      "u": use,
                      "get": get,
                      "g": get,
                      "commands": commands,
                      "c": commands
                    }

    # Print game intro/story/objective
    """
    start_game = input("Venture forth? (y/n) ").strip().casefold()
    if start_game == "n":
        print("You decide to turn back, yet can't help but wonder what mysteries could be found inside...")
        time.sleep(0.5)
        quit_game = True
    else:
        quit_game = False
        print("You open the door and step inside...")
        time.sleep(1)
    """

    quit_game = False
    # game loop
    while quit_game == False:

        # description of the current room
        print(game_objects.player.location.description)
        time.sleep(1)

        # characters in the current room
        game_objects.player.location.print_all_characters() 
        time.sleep(1)

        # valid exits in current room
        game_objects.player.location.print_viable_moves()
        time.sleep(1)
        
        # prompts user for an action
        print("Valid commands: talk, look, move, use, get, inventory, commands, quit")
        time.sleep(1)
        player_action = input("What would you like to do? ").strip().casefold()

        # split compound commands
        command_parts = player_action.split(maxsplit=1)
        main_command = command_parts[0]

        # if player action is not a command, continue asking for a command
        while main_command not in valid_commands:
            print("'" + player_action + "' is not a recognized command.")
            time.sleep(1)
            print("Valid commands: talk, look, move, use, get, inventory, commands, quit")
            time.sleep(1)
            player_action = input("What would you like to do? ").strip().casefold()

            command_parts = player_action.split(maxsplit=1) # make at most one split, allows for multi-word arguments
            main_command = command_parts[0]
        
        # set command argument if compound
        argument = command_parts[1] if len(command_parts) > 1 else None

        # handle commands
        if main_command in ["quit", "q"]:
            quit_game = True

        else:
            if main_command in ["move", "m"]:
                if not argument:
                    argument = input("Which direction do you want to move? ").strip().casefold()
                valid_commands[main_command](game_objects.player, game_objects.player.location, argument)
                
            elif main_command in ["talk", "t"]:
                if len(game_objects.player.location.characters) > 0:
                    if not argument:
                        argument = input("Who do you want to talk to? ").strip().casefold()
                    valid_commands[main_command](game_objects.player.location, argument)

                else:
                    print("There is no one here to talk to.")
                    time.sleep(1)
            
            elif main_command in ["look", "l"]:
                if not argument:
                    argument = input("What do you want to look at? ").strip().casefold()
                valid_commands[main_command](game_objects.player, game_objects.player.location, argument)
            
            elif main_command in ["use", "u"]:
                if not argument:
                    argument = input("What do you want to use? ").strip().casefold()
                valid_commands[main_command](game_objects.player, game_objects.player.location, argument)
            
            elif main_command in ["get", "g"]:
                if not argument:
                    argument = input("What do you want to pick up? ").strip().casefold()
                valid_commands[main_command](game_objects.player, game_objects.player.location, argument)

            elif main_command in ["commands", "c"]:
                valid_commands[main_command]()

            else:
                valid_commands[main_command](game_objects.player, game_objects.player.location)
        
main()
