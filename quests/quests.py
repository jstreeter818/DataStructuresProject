'''contains initializations for all questlines'''
import quests.questlines as questlines
import quests.quest_conditions as quest_conditions
import quests.quest_actions as quest_actions
import items.item_descriptions as item_descriptions
from game_objects import characters, items, rooms

Main_Quest = questlines.QuestLine()
Main_Quest.add_checkpoint([lambda: quest_conditions.item_been_used(items.broken_clock)], [])
Main_Quest.add_checkpoint([lambda: quest_conditions.item_in_inventory(items.lock_box)], [])