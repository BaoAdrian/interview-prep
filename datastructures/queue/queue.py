"""
queue.py

Purpose: This class implements the Queue data structure
and its corresponding methods using a Python List. 
In this implementation of the Queue, the front of the 
Queue is represented by the end of the front of list.
"""

class Queue:
    def __init__(self):
        self.queue = list()

    def __len__(self):
        return len(self.queue)

    def __str__(self):
        string = ""
        for element in self.queue:
            string += "[{}] << ".format(element)
        string += "\n"
        return string
    
    def __contains__(self, element):
        for el in self.queue:
            if el == element:
                return True
        return False
    
    def set_queue(self, queue):
        self.queue = queue

    def get_queue(self):
        return self.queue

    def peek(self):
        """
        peek: Returns the element at the top of the stack
        or None if stack is empty
        """
        if self.is_empty():
            return None
        return self.queue[0]

    def enqueue(self, element):
        """
        enqueue: Adds an element to the end of the queue.
        """
        self.queue.append(element)

    def dequeue(self):
        """
        dequeue: Removes the element at the front of the list and
        returns that element. Otherwise, returns None if the list
        is empty.
        """
        if self.is_empty():
            print("Queue is empty. Nothing to dequeue.")
            return None
        return self.queue.pop(0)

    def is_empty(self):
        """
        is_empty: Checks if the stack is currently empty, 
        returning boolean True/False depending on its evaluation
        """
        return len(self.queue) == 0

    def remove(self, target):
        """
        remove: Searches for the first occurence of target in the 
        queue and removes/returns that value if it exists. Otherwise,
        returns None.
        """
        temp_queue = Queue()
        found_element = None
        while not self.is_empty():
            curr_element = self.dequeue()
            if not found_element and curr_element == target:
                found_element = curr_element
            else:
                temp_queue.enqueue(curr_element)

        self.set_queue(temp_queue.get_queue())
        return found_element