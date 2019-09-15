from queue import *
import argparse

def parse_args():
    """
    parse_args: Parse command line arguments to test all
    or selected functionality of the LinkedList class.
    """
    parser = argparse.ArgumentParser()
    parser.add_argument('--test-all', action='store_true',
                        help='Test the functionality of ALL Queue methods')
    parser.add_argument('--test-enqueue', action='store_true',
                        help='Test the functionality of Queue.enqueue()')
    parser.add_argument('--test-dequeue', action='store_true',
                        help='Test the functionality of Queue.dequeue()')
    parser.add_argument('--test-peek', action='store_true',
                        help='Test the functionality of Queue.peek()')
    parser.add_argument('--test-remove', action='store_true',
                        help='Test the functionality of Queue.remove()')
    args = parser.parse_args()
    return args

def test_enqueue():
    print_header(" Testing Queue.enqueue() ")

    queue = Queue()

    queue.enqueue("1st in line")
    queue.enqueue("2nd in line")
    queue.enqueue("3rd in line")

    print("Queue: {}".format(queue))

def test_dequeue():
    print_header(" Testing Queue.dequeue() ")

    queue = Queue()
    queue.enqueue("First process")
    queue.enqueue("Final process")

    print("Queue: {}".format(queue))

    process_to_complete = queue.dequeue()
    print("Dequeued: '{}'".format(process_to_complete))
    print("Queue: {}".format(queue))

    process_to_complete = queue.dequeue()
    print("Dequeued: '{}'".format(process_to_complete))
    print("Queue: {}".format(queue))

    process_to_complete = queue.dequeue()
    print("Dequeued: '{}'".format(process_to_complete))
    print("Queue: {}".format(queue))

def test_peek():
    print_header(" Testing Queue.peek() ")

    queue = Queue()
    queue.enqueue(100)
    queue.enqueue(200)
    queue.enqueue(300)

    print("Queue: {}".format(queue))

    peeked_element = queue.peek()
    print("Peeked element: {}".format(peeked_element))

def test_remove():
    print_header(" Testing Queue.remove(valid) ")

    queue = Queue()
    queue.enqueue(1)
    queue.enqueue(200000)
    queue.enqueue(3333)
    queue.enqueue(797977979)

    print("Queue: {}".format(queue))
    target = 3333
    print("Target: '{}'".format(target))
    queue.remove(target)
    print("Queue: {}".format(queue))

    print_header(" Testing Queue.remove(invalid) ")

    target = 'Does not exist'
    print("Target: '{}'".format(target))
    queue.remove(target)
    print("Queue: {}".format(queue))

def print_header(msg):
    """
    print_header: Utility function to print headers.
    """
    SPACING = 60
    print("\n" + "-"*SPACING)
    print(msg.center(SPACING, "-"))
    print("-"*SPACING)

def main():
    args = parse_args()

    if args.test_all or args.test_enqueue:
        test_enqueue()
    if args.test_all or args.test_dequeue:
        test_dequeue()
    if args.test_all or args.test_peek:
        test_peek()
    if args.test_all or args.test_remove:
        test_remove()

if __name__ == "__main__":
    main()