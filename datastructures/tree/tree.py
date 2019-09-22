"""
tree.py

Purpose: This class implements the recursive definition of a Binary
Search Tree where each BSTNode is a subtree of the root BSTNode.
"""
class BSTNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None
    
    def __str__(self):
        return "({} < {} > {})".format(self.left, self.value, self.right)

    def __contains__(self, target):
        if self.search(target) == True:
            return True
        return False

    def insert(self, node):
        """
        insert: Inserts a give node into the BST into its 
        corresponding position following the binary insertion
        logic.
        """
        if self == None:
            self = node
        else:
            if node.get_value() < self.get_value():
                if self.get_left() == None:
                    self.set_left(node)
                else:
                    self.get_left().insert(node)
            else:
                if self.get_right() == None:
                    self.set_right(node)
                else:
                    self.get_right().insert(node)

    def find_successor(self, node):
        """
        find_successor: Once target removal node is found, 
        successor must be found to take its place if 
        necessary.
        """
        curr = node
        while curr.get_left() != None:
            curr = curr.get_left()
        return curr

    def remove(self, target):
        """
        remove: Search BST for target value and removes node
        if found, modifying the tree accordingly to ensure all
        connections are maintained.
        """
        if self == None:
            return self

        if target not in self:
            return None
        
        if target < self.get_value() and self.get_left():
            self.set_left(self.get_left().remove(target))
        elif target > self.get_value() and self.get_right():
            self.set_right(self.get_right().remove(target))
        else:
            # Match, modify nodes accordingly
            # 3 Cases:
            # 1. Leaf node
            # 2. One Child
            # 3. Two Children
            if self.get_left() == None:
                temp = self.get_right()
                self = None
                return temp
            elif self.get_right() == None:
                temp = self.get_left()
                self = None
                return temp
            
            temp = self.find_successor(self.get_right())
            self.set_value(temp.get_value())
            self.set_right(self.get_right().remove(temp.get_value()))
        return self

    def search(self, target):
        """
        search: Searches BST for a given target value and returns
        boolean True/False if found or not.
        """
        if self == None:
            return False
        elif self.get_value() == target:
            return True
        else:
            if target < self.get_value():
                return self.get_left().search(target) if self.get_left() else False
            else:
                return self.get_right().search(target) if self.get_right() else False

    def preorder_traversal(self, traversal):
        """ Preorder Traversal of BST: VLR """
        if self == None:
            return None
        else:
            traversal.append(self.get_value())
            self.get_left().preorder_traversal(traversal) if self.get_left() else None
            self.get_right().preorder_traversal(traversal) if self.get_right() else None
        return traversal

    def inorder_traversal(self, traversal):
        """ Inorder Traversal of BST: LVR """
        if self == None:
            return None
        else:
            self.get_left().inorder_traversal(traversal) if self.get_left() else None
            traversal.append(self.get_value())
            self.get_right().inorder_traversal(traversal) if self.get_right() else None
        return traversal

    def postorder_traversal(self, traversal):
        """ Postorder Traversal of BST: LRV """
        if self == None:
            return None
        else:
            self.get_left().postorder_traversal(traversal) if self.get_left() else None
            self.get_right().postorder_traversal(traversal) if self.get_right() else None
            traversal.append(self.get_value())
        return traversal

    def get_height(self):
        if self == None:
            return 0
        else:
            max_left = self.get_left().get_height() if self.get_left() else 0
            max_right = self.get_right().get_height() if self.get_right() else 0
            return max(max_left+1, max_right+1)

    def get_value(self):
        return self.value
    
    def set_value(self, value):
        self.value = value

    def get_left(self):
        return self.left

    def set_left(self, node):
        self.left = node

    def get_right(self):
        return self.right

    def set_right(self, node):
        self.right = node
