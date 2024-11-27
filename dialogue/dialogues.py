'''holds all initializations of character dialogue trees'''

import dialogue.dialogue_tree as dialogue_tree
from objects.game_objects import player
import characters.npc_actions as npc_actions
import quests.quests as quests

Duncan_Dialogue = dialogue_tree.Dialogue_Tree(quests.Main_Quest)
Duncan_Dialogue.add(None, ". . .", left_key="ring bell", right_key="clear throat", action=lambda: print("He's slumped over the desk... snoring."))
Duncan_Dialogue.add('0', "Goodness! My apologies for the lack of professionalism, that's quite embarrassing on my part. How silly to let myself fall asleep on the job.")
Duncan_Dialogue.add('1', "Goodness! My apologies for the lack of professionalism, that's quite embarrassing on my part. How silly to let myself fall asleep on the job.")
Duncan_Dialogue.add('00', "Welcome to Cairn's Keep. You don't look like you've been here before. It is really quite nice to see a new face stopping in.")
Duncan_Dialogue.add('10', "Welcome to Cairn's Keep. You don't look like you've been here before. It is really quite nice to see a new face stopping in.")
Duncan_Dialogue.add('000', "Oh, my name's Duncan. I'm the owner and founder, but I also help keep the place running. It's truly a pleasure to meet you...")
Duncan_Dialogue.add('100', "Oh, my name's Duncan. I'm the owner and founder, but I also help keep the place running. It's truly a pleasure to meet you...")
Duncan_Dialogue.add('0000', (player.name + "!"), action=lambda: npc_actions.handshake("Duncan"))
Duncan_Dialogue.add('1000', (player.name + "!"), action=lambda: npc_actions.handshake("Duncan"))
Duncan_Dialogue.add('00000', "Well I'll let you explore this place on your own. Here's a map of the building to help you get around.", action=npc_actions.give_map)
Duncan_Dialogue.add('10000', "Well I'll let you explore this place on your own. Here's a map of the building to help you get around.", action=npc_actions.give_map)
Duncan_Dialogue.add('000000', "I'm sure you'd like to take a look around. We have many items from faraway places, and pieces of great history.")
Duncan_Dialogue.add('100000', "I'm sure you'd like to take a look around. We have many items from faraway places, and pieces of great history.")
Duncan_Dialogue.add('0000000', "Why, that old clock over there is from the renaissance. Said to be designed by Da Vinci himself. It's a shame it hasn't been working since he--Nevermind that... \nTake a look around the place and come to me if you need anything.", checkpoint=True)
Duncan_Dialogue.add('1000000', "Why, that old clock over there is from the renaissance. Said to be designed by Da Vinci himself. It's a shame it hasn't been working since he--Nevermind that... \nTake a look around the place and come to me if you need anything.", checkpoint=True)
Duncan_Dialogue.add('00000000', "What's that? You got the clock working again? Normally it's considered rude to tamper with things that aren't yours..")
Duncan_Dialogue.add('10000000', "What's that? You got the clock working again? Normally it's considered rude to tamper with things that aren't yours..")
Duncan_Dialogue.add('000000000', "But I'll have to admit I'm impressed. That clock has been bugging me for ages, and you actually figured it out.")
Duncan_Dialogue.add('100000000', "But I'll have to admit I'm impressed. That clock has been bugging me for ages, and you actually figured it out.")
Duncan_Dialogue.add('0000000000', "Now that I think about it, there's quite a bit around this place that I could use some help in, and you've shown yourself to be useful--and very clever!")
Duncan_Dialogue.add('1000000000', "Now that I think about it, there's quite a bit around this place that I could use some help in, and you've shown yourself to be useful--and very clever!")
Duncan_Dialogue.add('00000000000', "Think you'd be up to a few more tasks around here?")
Duncan_Dialogue.add('10000000000', "Think you'd be up to a few more tasks around here?")

BlackCat_Dialogue = dialogue_tree.Dialogue_Tree()
BlackCat_Dialogue.add(None, 'Mrowww', checkpoint=True)
BlackCat_Dialogue.add('0', "*sniff sniff*", left_key="give treat", right_key="give all treats")
BlackCat_Dialogue.add('00', "Mrow! *crunch crunch*")
BlackCat_Dialogue.add('01', "Purrrr *crunch crunch*")
BlackCat_Dialogue.add('000', "Mrowww", checkpoint=True)
BlackCat_Dialogue.add('010', "Mrowww.", checkpoint=True)