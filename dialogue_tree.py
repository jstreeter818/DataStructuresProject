import time

class Node:
    def __init__(self, value, left_key, right_key, checkpoint, checkpoint_condition, action, path = None):
        # the dialogue
        self.value = value
        # path of the node position, a string of binary numbers
        # 0 = left
        # 1 = right
        self.path = path
        self.left = None
        self.right = None
        # key word for child nodes
        self.left_key = left_key
        self.right_key = right_key
        # Dialogue checkpoint - defaults False
        self.checkpoint = checkpoint
        # checkpoint condition is a lambda function
        self.checkpoint_condition = checkpoint_condition
        # additional action to be executed with dialogue - defaults None
        self.action = action

class Dialogue_Tree:
    def __init__(self):
        self.head = None
    
    def add(self, path, value, checkpoint = False, checkpoint_condition = None, left_key = None, right_key = None, action = None):
        self.head = self.add_recurse(self.head, path, value, left_key, right_key, '', checkpoint, checkpoint_condition, action)
        return self
    
    def add_recurse(self, node, path, value, left_key, right_key, current_path, checkpoint, checkpoint_condition, action):
        # path is empty, correct position found, add node
        if not path:
            return Node(value, left_key, right_key, checkpoint, checkpoint_condition, action, current_path)
        # path continues beyond existing nodes
        if node is None:
            node = Node(None)
        
        # recursively traverse path
        if path[0] == '0':
            node.left = self.add_recurse(node.left, path[1:], value, left_key, right_key, current_path + '0', checkpoint, checkpoint_condition, action)
        if path[0] == '1':
            node.right = self.add_recurse(node.right, path[1:], value, left_key, right_key, current_path + '1', checkpoint, checkpoint_condition, action)
        
        return node

    def remove(self, path, branch, value):
        self.head = self.remove_recurse(self.head, path, branch, value)

        # update paths of all nodes after removal starting with head and empty path
        self.update_paths(self.head, '')
        return self
    
    def remove_recurse(self, node, path, branch, value):
        if node is None:
            return None
        
        # correct node is found, return specified child branch or None
        if node.value == value:
            if branch == 'left':
                return node.left
            if branch == 'right':
                return node.right
            return None
            
        # check other nodes
        if path and path[0] == '0':
            node.left = self.remove_recurse(node.left, path[1:], branch, value)
        if path and path[0] == '1':    
            node.right = self.remove_recurse(node.right, path[1:], branch, value)

        return node
    
    def update_paths(self, node, current_path):
        if node is None:
            return
        
        node.path = current_path

        # recursively update next nodes, keeping track of the path taken
        self.update_paths(node.left, current_path + '0')
        self.update_paths(node.right, current_path + '1')


    def contains(self, path, value):
        return self.contains_recurse(self.head, path, value)
        
    def contains_recurse(self, node, path, value):
        if node is None:
            return False
        if node.value == value:
            return True
        if path and path[0] == '0':
            return self.contains_recurse(node.left, path[1:], value)
        if path and path[0] == '1':
            return self.contains_recurse(node.right, path[1:], value)
        return False
    
    def traverse_dialogue(self, node):
        # while there exists a node to traverse
        while node:
            # checkpoint handling
            if node.checkpoint:
                # if node.checkpoint_condition exists and evaluates to True
                if node.checkpoint_condition and node.checkpoint_condition():
                    # remove checkpoint
                    node.checkpoint = False

                    node_to_remove = node

                    # move to next node
                    if node.left:
                        node = node.left
                    elif node.right:
                        node = node.right

                    # FIX: branch traversal    
                    self.remove(node_to_remove.path, None, node_to_remove.value)

            print(node.value)
            time.sleep(1)

            # if node has an additional action, execute action
            if node.action:
                node.action()

            # keep track of node to remove later
            node_to_remove = node

            # if the node is a checkpoint, pause dialogue
            if node.checkpoint:
                return
            
            # no more branches to traverse
            if node.left is None and node.right is None:
                self.remove(node_to_remove.path, None, node_to_remove.value)
                return
                
            # if only one branch is present, traverse to that branch without player input
            elif node.left is None:
                node = node.right
                self.remove(node_to_remove.path, 'right', node_to_remove.value)
            elif node.right is None:
                node = node.left
                self.remove(node_to_remove.path, 'left', node_to_remove.value)

            # if two branches are present, get path from user
            else:
                path = input(node.left_key + " or " + node.right_key + "? ").strip().casefold()

                while path not in [node.left_key, node.right_key]:
                    print("'" + path + "' is an invalid choice.")
                    path = input(node.left_key + " or " + node.right_key + "? ").strip().casefold()
                
                # traverse based on path
                if path == node.left_key:
                    node = node.left
                    self.remove(node_to_remove.path, 'left', node_to_remove.value)
                elif path == node.right_key:
                    node = node.right
                    self.remove(node_to_remove.path, 'right', node_to_remove.value)


test_dialogue = Dialogue_Tree().add(None, "Do you want waffles or pancakes?", "waffles", "pancakes")
test_dialogue.add('0', "Do you want coffee or tea with your waffles?", "coffee", "tea")
test_dialogue.add('1', "Do you want milk or juice with your pancakes?", "milk", "juice")
test_dialogue.add('00', "You chose waffles and coffee.", None, None, True)
test_dialogue.add('01', "You chose waffles and tea.", None, None, True)
test_dialogue.add('10', "You chose pancakes and milk.", None, None, True)
test_dialogue.add('11', "You chose pancakes and juice.", None, None, True)


#test_dialogue.traverse_dialogue(test_dialogue.head)
#test_dialogue.traverse_dialogue(test_dialogue.head)