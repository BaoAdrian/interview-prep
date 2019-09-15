"""
stack.py

Purpose: This class implements the Stack data structure
and its corresponding methods. 
In this implementation of the Stack, the top of the stack
is represented by the end of the list.
"""

class Stack:
    def __init__(self):
        self.stack = []

    def __str__(self):
        string = ""
        if self.is_empty():
            print("No elements in the stack")
            return
        max_len = max([len(str(el)) for el in self.stack])
        for element in self.stack[::-1]:
            string += "\n| {} |".format(str(element).center(max_len))
            string += "\n| {} |".format("-"*(max_len))
        string += "\n"
        return string

    def __len__(self):
        return len(self.stack)

    def __contains__(self, element):
        return element in self.stack

    def peek(self):
        """
        peek: Returns the element at the top of the stack
        or None if stack is empty
        """
        if len(self) >= 1:
            return self.stack[-1]
        return None

    def pop(self):
        """
        pop: Removes the element at the top of the stack if
        one exists and return the element. Otherwise, returns
        None if stack is empty. 
        """
        if len(self) >= 1:
            element = self.stack.pop(-1)
            return element
        return None

    def push(self, element):
        """
        push: Adds element to the top of the stack.
        """
        self.stack.append(element)

    def is_empty(self):
        """
        is_empty: Checks if the stack is currently empty, 
        returning boolean True/False depending on its evaluation
        """
        return len(self) == 0

    def search(self, target):
        """
        search: Searches the stack for a given element and 
        and flags the location on the console output. Displays
        note if no element is found.
        """
        is_found = False
        print()
        if self.is_empty():
            print("No elements in the stack")
            return
        max_len = max([len(el) for el in self.stack])
        for element in self.stack[::-1]:
            if element == target:
                is_found = True
                print("| " + element.center(max_len) + " |" + " << target")
            else:
                print("| " + element.center(max_len) + " |")
            print("| " + "-"*(max_len) + " |")
        print()

        if not is_found:
            print("No element found: '{}'\n".format(target))

    def search_and_remove(self, target):
        """
        search_and_remove: Searches current stack for a target element
        and removes it if found. Otherwise, returns None and stack 
        remains in tact.
        """
        temp_stack = Stack()
        found_element = None

        while not self.is_empty():
            curr_element = self.pop()
            if curr_element == target:
                found_element = curr_element
                break 
            temp_stack.push(curr_element)

        # Reinsert stack elements with target removed
        while not temp_stack.is_empty():
            self.push(temp_stack.pop())

        if found_element:
            print("Found element. Removing.\n")
            print("New Stack: {}".format(self))
        else:
            print("No element found: '{}'\n".format(target))
        
        return found_element


