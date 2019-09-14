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

    def peek(self):
        """
        peek: Returns the element at the top of the stack
        or None if stack is empty
        """
        if len(self.stack) >= 1:
            return self.stack[-1]
        return None

    def pop(self):
        """
        pop: Removes the element at the top of the stack if
        one exists and return the element. Otherwise, returns
        None if stack is empty. 
        """
        if len(self.stack) >= 1:
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
        return len(self.stack) == 0

    def size(self):
        """
        size: Returns the current size of the stack
        """
        return len(self.stack)

    def print_stack(self, msg):
        """
        print_stack: Prints formatted output for the current
        structure of the stack.
        """
        print("\n" + msg)
        if self.is_empty():
            print("No elements in the stack")
            return
        max_len = max([len(el) for el in self.stack])
        for element in self.stack[::-1]:
            print("| " + element.center(max_len) + " |")
            print("| " + "-"*(max_len) + " |")
        print()

    def search(self, target):
        """
        search: Searches the stack for a given element and 
        returns its index IF FOUND. Returns None otherwise.
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
            print("No element found: {}\n".format(target))

    def search_and_remove(self, target):
        """
        search_and_remove: Searches current stack for a target element
        and removes it if found. Otherwise, stack remains in tact.
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
            print("Found element. Removing.")
            self.print_stack("New Stack:")
        else:
            print("No element found: '{}'\n".format(target))
        
        return found_element


def main():
    stack = Stack()

    print("\n" + "Testing Stack.push()".center(50, "-"))
    stack.push("Bottom of the stack")
    stack.push("2nd pushed element")
    stack.push("3rd pushed element")
    stack.push("Top of the stack")

    stack.print_stack("Stack:")

    print("\n" + "Testing Stack.search(target)".center(50, "-"))

    print("Searching for: '2nd pushed element'")
    stack.search("2nd pushed element")
    print("Searching for: 'Nonexistent element'")
    stack.search("Nonexistent element")

    print("\n" + "Testing Stack.search_and_remove(target)".center(50, "-"))

    print("Removing: '2nd pushed element'")
    stack.search_and_remove("2nd pushed element")
    print("Removing: 'Nonexistent element'")
    stack.search_and_remove("Nonexistent element")

    print("\n" + "Testing Stack.size() and Stack.pop()".center(50, "-"))
    
    stack.print_stack("Current Stack:")
    print("Current size:   {}".format(stack.size()))
    popped_element = stack.pop()
    print("Popped: '{}'".format(popped_element))
    print("Size after pop: {}".format(stack.size()))
    stack.print_stack("New Stack:")

if __name__ == "__main__":
    main()