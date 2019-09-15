from stack import Stack

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