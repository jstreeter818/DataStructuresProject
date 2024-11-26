'''Contains QuestLine and QuestNode classes for character quests'''

class QuestNode:
    def __init__(self, condition, actions):
        self.condition = condition
        self.actions = actions
        self.next = None
        self.visited = False

class QuestLine:
    def __init__(self):
        self.current_node = None

    def add(self, condition, actions):
        new_node = QuestNode(condition, actions)

        if self.current_node is None:
            self.current_node = new_node
        else:
            # Go to the end of the list
            current_node = self.current_node
            while current_node.next:
                current_node = current_node.next
            current_node.next = new_node

    def check_and_progress(self):
        if self.current_node is None:
            print("No quests active.")
            return
        
        # if node has not been visited yet, execute actions
        if not self.current_node.visited:
            for action in self.current_node.actions:
                action()
            self.current_node.visted = True

        # if quest condition is met, go to next quest node
        if self.current_node.condition():
            self.current_node = self.current_node.next
