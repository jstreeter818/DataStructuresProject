'''contains initializations for all questlines'''
import quests.questlines as questlines
import quests.quest_conditions as quest_conditions
import quests.quest_actions as quest_actions
import items.item_descriptions as item_descriptions
from objects import game_objects

Main_Quest = questlines.QuestLine()
Main_Quest.add_checkpoint([lambda: quest_conditions.item_been_used(game_objects.broken_clock)], [])