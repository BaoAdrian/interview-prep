from stack import *
import argparse

def parse_args():
    """
    parse_args: Parse command line arguments to test all
    or selected functionality of the LinkedList class.
    """
    parser = argparse.ArgumentParser()
    parser.add_argument('--test-all', action='store_true',
                        help='Test the functionality of ALL Stack methods')
    parser.add_argument('--test-push', action='store_true',
                        help='Test the functionality of Stack.push()')
    parser.add_argument('--test-pop', action='store_true',
                        help='Test the functionality of Stack.pop()')
    parser.add_argument('--test-peek', action='store_true',
                        help='Test the functionality of Stack.peek()')
    parser.add_argument('--test-search', action='store_true',
                        help='Test the functionality of Stack.search() & Stack.search_and_remove()')
    args = parser.parse_args()
    return args

def test_push():
    print_header(" Testing Stack.push() ")

    stack = Stack()
    stack.push("Bottom of the stack")
    stack.push("2nd pushed element")
    stack.push("3rd pushed element")
    stack.push("Top of the stack")

    print("Stack:\n{}".format(stack))

def test_pop():
    print_header(" Testing Stack.pop() ")
    
    stack = Stack()
    stack.push("Bottom of the stack")
    stack.push("2nd pushed element")
    stack.push("3rd pushed element")
    stack.push("Top of the stack")

    print("Stack: {}".format(stack))

    popped_element = stack.pop()
    if popped_element:
        print("Popped: '{}'".format(popped_element))
    
    print("Stack: {}".format(stack))

def test_peek():
    print_header(" Testing Stack.pop() ")
    
    stack = Stack()
    stack.push("Bottom")
    stack.push("Middle")
    stack.push("Top")

    print("Stack: {}".format(stack))

    peeked_element = stack.peek()
    if peeked_element:
        print("Peeked element: '{}'".format(peeked_element))

def test_search():
    stack = Stack()
    stack.push("Not this one")
    stack.push("We are looking for this!")
    stack.push("Definitely not this one")

    print_header(" Testing Stack.search(valid) ")
    print("Stack: {}".format(stack))

    target =  "We are looking for this!"
    print("Target: '{}'".format(target))
    stack.search(target)

    print_header(" Testing Stack.search(invalid) ")
    print("Stack: {}".format(stack))

    target = "Does not exist"
    print("Target: '{}'".format(target))
    stack.search(target)

def test_search_and_remove():
    stack = Stack()
    stack.push(1000000)
    stack.push(5555555)
    stack.push(9999999)

    print_header(" Testing Stack.search_and_remove(valid) ")
    print("Stack: {}".format(stack))

    target = 9999999
    print("Target: '{}'".format(target))
    found_element = stack.search_and_remove(target)

    if found_element:
        print("Found element. Removing.\n")
        print("New Stack: {}".format(stack))
    else:
        print("No element found: '{}'\n".format(target))

    print_header(" Testing Stack.search_and_remove(invalid) ")
    print("Stack: {}".format(stack))

    target = 123456
    print("Target: '{}'".format(target))
    found_element = stack.search_and_remove(target) 

    if found_element:
        print("Found element. Removing.\n")
        print("New Stack: {}".format(stack))
    else:
        print("No element found: '{}'\n".format(target))   

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

    if args.test_all or args.test_push:
        test_push()
    if args.test_all or args.test_pop:
        test_pop()
    if args.test_all or args.test_peek:
        test_peek()
    if args.test_all or args.test_search:
        test_search()
        test_search_and_remove()

if __name__ == "__main__":
    main()
