class SinglyLinkedList:
    """
    SinglyLinkedList: DS Implementation making use of the 
    Node class defined below to define a Singly LinkedList and
    its corresponding methods.
    """
    def __init__(self):
        self.head = None

    def __str__(self):
        """
        str: overridden method to provided formatted string
        representation of the current LinkedList.
        """
        string = ""
        curr = self.head
        while curr:
            string += "[{}] >> ".format(curr.get_element())
            curr = curr.get_next()
        string += "[NULL]"
        return string
    
    def __len__(self):
        length = 0
        curr = self.head
        while curr:
            length += 1
            curr = curr.get_next()
        return length

    def __contains__(self, target_element):
        curr = self.head
        while curr:
            if curr.get_element() == target_element:
                return True
            curr = curr.get_next()
        return False

    def is_empty(self):
        return self.head == None

    def add(self, node):
        """
        add: Adds given node to the front of the 
        LinkedList.
        """
        if self.head == None:
            self.head = node
        else:
            node.set_next(self.head)
            self.head = node

    def append(self, node):
        """
        append: Adds the given node to the end of the
        LinkedList.
        """
        if self.head == None:
            self.head = node
            return

        curr = self.head
        while curr.get_next():
            curr = curr.get_next()
        curr.set_next(node)

    def insert(self, node, index):
        """
        insert: Traverses LinkedList and inserts node at the
        specified index. If index is invalid, will add element
        to the end of the LinkedList.
        """
        if index > len(self):
            print("Invalid index, {}. Appending to end of the list".format(index))
            self.append(node)
        else:
            running_idx = 1
            curr = self.head
            while curr:
                if running_idx == index:
                    node.set_next(curr.get_next())
                    curr.set_next(node)
                    break
                running_idx += 1
                curr = curr.get_next()

    def remove_by_element(self, target_element):
        """
        remove_by_element: Removes & returns node with matching 
        target if found. Otherwise, LinkedList remains in tact.
        """
        print("Target: {}".format(target_element))
        curr = self.head

        if curr.get_element() == target_element:
            self.head = curr.get_next()
            curr.set_next(None)
            return curr

        next = curr.get_next()
        while next:
            if next.get_element() == target_element:
                curr.set_next(next.get_next())
                next.set_next(None)
                return curr
            curr = next
            next = next.get_next()
        
        # If here, no element was found
        return None
    
    def remove_by_index(self, index):
        """
        remove_by_index: Removes & returns node at the 
        corresponding index if valid. Otherwise, LinkedList 
        remains in tact.
        """
        if index > len(self):
            return None
        
        curr = self.head

        if index == 0:
            self.head = curr.get_next()

        next = curr.get_next()
        running_idx = 1
        while next:
            if running_idx == index:
                curr.set_next(next.get_next())
                next.set_next(None)
                return next
            running_idx += 1
            curr = next
            next = next.get_next()

        return None

    def search(self, target_element):
        """
        search: Similar to __contains__(), traverses LinkedList 
        searching for target_element and returns its index if 
        found. Returns -1 otherwise.
        """
        print("Target: {}".format(target_element))
        index = 0
        curr = self.head
        while curr:
            if curr.get_element() == target_element:
                return index
            index += 1
            curr = curr.get_next()
        return -1

class Node:
    """
    Node: Class representing a single Node inside a LinkedList that
    contains an element attribute (any type: int, str, object, etc...).
    """
    def __init__(self, element):
        self.element = element
        self.next = None

    def __str__(self):
        return "[{}]".format(self.element)

    def get_next(self):
        return self.next

    def set_next(self, node):
        self.next = node

    def get_element(self):
        return self.element
    
    def set_element(self, element):
        self.element = element