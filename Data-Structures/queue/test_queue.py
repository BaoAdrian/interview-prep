from queue import Queue

def print_header(msg):
    """
    print_header: Utility function to print headers.
    """
    SPACING = 60
    print("\n" + "-"*SPACING)
    print(msg.center(SPACING, "-"))
    print("-"*SPACING)

def main():

    queue = Queue()

    print_header(" Testing Queue.enqueue() ")
    queue.enqueue("1st element")
    queue.enqueue("2nd element")
    queue.enqueue("3rd element")
    queue.enqueue("4th element")
    queue.print_queue("Queue:")

    print_header(" Testing Queue.peek() ")
    queue.print_queue("Queue:")
    print("First element: {}\n".format(queue.peek()))

    print_header(" Testing Queue.dequeue() & Queue.size() ")
    queue.print_queue("Current Queue (size = {}):".format(queue.size()))
    dequeued_element = queue.dequeue()
    print("Dequeued element: '{}'\n".format(dequeued_element))
    queue.print_queue("New Queue (size = {}):".format(queue.size()))

    print_header(" Testing Queue.remove() ")
    queue.print_queue("Queue:")
    
    invalid_target = "Nonexistent element"
    print("Attempting to remove: '{}'".format(invalid_target))
    queue.remove(invalid_target)
    queue.print_queue("Updated Queue:")

    valid_target = "3rd element"
    print("Attempting to remove: '{}'".format(valid_target))
    queue.remove(valid_target)
    queue.print_queue("Updated Queue:")

if __name__ == "__main__":
    main()