'''containts Node and Dialogue_Tree classes for traversing NPC dialogue'''
import time

class Node:
    def __init__(self, value, pause, left_key, right_key, checkpoint, action, path):
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
        # pause/breakpoint in dialogue different from a checkpoint
        self.pause = pause
        # Dialogue checkpoint - defaults False
        self.checkpoint = checkpoint
        # additional action to be executed with dialogue - defaults None
        self.action = action

class Dialogue_Tree:
    def __init__(self, questline=None):
        self.head = None
        self.questline = questline
    
    def add(self, path, value, pause = False, checkpoint = False, left_key = None, right_key = None, action = None):
        self.head = self.add_recurse(self.head, path, value, pause, left_key, right_key, '', checkpoint, action)
        return self
    
    def add_recurse(self, node, path, value, pause, left_key, right_key, current_path, checkpoint, action):
        # path is empty, correct position found, add node
        if not path:
            return Node(value, pause, left_key, right_key, checkpoint, action, current_path)
        # path continues beyond existing nodes
        if node is None:
            node = Node(None)
        
        # recursively traverse path
        if path[0] == '0':
            node.left = self.add_recurse(node.left, path[1:], value, pause, left_key, right_key, current_path + '0', checkpoint, action)
        if path[0] == '1':
            node.right = self.add_recurse(node.right, path[1:], value, pause, left_key, right_key, current_path + '1', checkpoint, action)
        
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

    def check_and_remove(self, node):
        """Helper function to check checkpoint conditions and remove nodes when checkpoint met"""
        
        checkpoint_passed = self.questline.check_and_progress()

        if checkpoint_passed:
            node_to_remove = node

            if node.left:
                node = node.left
                self.remove(node_to_remove.path, 'left', node_to_remove.value)
            elif node.right:
                node = node.right
                self.remove(node_to_remove.path, 'right', node_to_remove.value)
            else:
                node = None
                self.remove(node_to_remove.path, None, node_to_remove.value)
        
        return node
    
    def traverse_dialogue(self, node, character_name):
        # while there exists a node to traverse
        while node:

            # check and remove passed checkpoints
            node = self.check_and_remove(node)

            print(character_name + ': ' + node.value)
            time.sleep(1)

            # if node has an additional action, execute action
            if node.action:
                node.action()
                time.sleep(1)

            # keep track of node to remove later
            node_to_remove = node

            # if the node is a checkpoint, pause dialogue
            if node.checkpoint:
                return
            
            # keep track of whether to pause or not later
            pause_traversal = True if node.pause else False

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
                path = input("(1) " + node.left_key + " or (2) " + node.right_key + "? ").strip()

                while path not in ['1', '2']:
                    print("'" + path + "' is an invalid choice.")
                    path = input("(1) " + node.left_key + " or (2) " + node.right_key + "? ").strip()
                
                # traverse based on path
                if path == '1':
                    print("*" + node.left_key + "*")
                    node = node.left
                    self.remove(node_to_remove.path, 'left', node_to_remove.value)
                elif path == '2':
                    print("*" + node.right_key + "*")
                    node = node.right
                    self.remove(node_to_remove.path, 'right', node_to_remove.value)
                
                time.sleep(1)

            # if node is a pause point, pause dialogue
            if pause_traversal:
                return