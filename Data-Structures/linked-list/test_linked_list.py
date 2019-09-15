from linked_list import *
import argparse

def parse_args():
    """
    parse_args: Parse command line arguments to test all
    or selected functionality of the LinkedList class.
    """
    parser = argparse.ArgumentParser()
    parser.add_argument('--test-all', action='store_true',
                        help='Test the functionality of ALL LinkedList methods')
    parser.add_argument('--test-add', action='store_true',
                        help='Test the functionality of the various methods used to add Nodes to the LinkedList (add, append, insert)')
    parser.add_argument('--test-removal', action='store_true',
                        help='Test the functionality of the various node removal methods of a LinkedList (remove_by_element, remove_by_index)')
    parser.add_argument('--test-search', action='store_true',
                        help='Test the functionality of LinkedList.search(target)')
    args = parser.parse_args()
    return args

def test_add():
    print_header(" Testing LinkedList.add(node) ")
    ll = SinglyLinkedList()
    print("LinkedList: {}".format(ll))
    n1, n2, n3 = Node(100), Node(200), Node(300)
    print("Adding n1")
    ll.add(n1)
    print("LinkedList: {}".format(ll))
    print("Adding n2")
    ll.add(n2)
    print("LinkedList: {}".format(ll))
    print("Adding n3")
    ll.add(n3)
    print("LinkedList: {}".format(ll))

def test_append():
    print_header(" Testing LinkedList.append(node) ")
    ll = SinglyLinkedList()
    print("LinkedList: {}".format(ll))
    n1, n2, n3 = Node(100), Node(200), Node(300)
    print("Appending n1")
    ll.append(n1)
    print("LinkedList: {}".format(ll))
    print("Appending n2")
    ll.append(n2)
    print("LinkedList: {}".format(ll))
    print("Appending n3")
    ll.append(n3)
    print("LinkedList: {}".format(ll))

def test_insert():
    print_header(" Testing LinkedList.insert(node, index) ")
    ll = SinglyLinkedList()
    nodes = [Node(1), Node(2), Node(3), Node(4)]
    [ll.add(node) for node in nodes]

    print("LinkedList: {}".format(ll))

    new_node = Node(500)
    new_index = 2
    ll.insert(new_node, new_index)

    print("LinkedList: {}".format(ll))

    new_node = Node(1000)
    new_index = 15
    ll.insert(new_node, new_index)

    print("LinkedList: {}".format(ll))

def test_remove_by_element():
    print_header(" Testing LinkedList.remove_by_element(valid) ")
    ll = SinglyLinkedList()
    nodes = [Node("one"), Node("two"), Node("three"), Node("four"), Node("five")]
    [ll.append(node) for node in nodes]

    print("LinkedList: {}".format(ll))

    target_element = "four"
    ll.remove_by_element(target_element)
    print("LinkedList: {}".format(ll))

    print_header(" Testing LinkedList.remove_by_element(invalid) ")
    ll = SinglyLinkedList()
    nodes = [Node("one"), Node("two"), Node("three"), Node("four"), Node("five")]
    [ll.append(node) for node in nodes]

    print("LinkedList: {}".format(ll))

    target_element = "nonexistent"
    ll.remove_by_element(target_element)
    print("LinkedList: {}".format(ll))

def test_remove_by_index():
    print_header(" Testing LinkedList.remove_by_index(valid) ")
    ll = SinglyLinkedList()
    nodes = [Node("one"), Node("two"), Node("three"), Node("four"), Node("five")]
    [ll.append(node) for node in nodes]

    print("LinkedList: {}".format(ll))

    target_index = 2
    ll.remove_by_index(target_index)
    print("LinkedList: {}".format(ll))

    print_header(" Testing LinkedList.remove_by_index(invalid) ")
    ll = SinglyLinkedList()
    nodes = [Node("one"), Node("two"), Node("three"), Node("four"), Node("five")]
    [ll.append(node) for node in nodes]

    print("LinkedList: {}".format(ll))

    target_index = 10
    ll.remove_by_index(target_index)
    print("LinkedList: {}".format(ll))

def test_search():
    print_header(" Testing LinkedList.search(valid_target) ")

    ll = SinglyLinkedList()
    nodes = [Node(1), Node(2), Node(3), Node(4)]
    [ll.add(n) for n in nodes]

    print("LinkedList: {}".format(ll))

    target_element = 2

    index = ll.search(target_element)
    if index != -1:
        print("Found element at index: {}".format(index))
    else:
        print("Could not find node with matching element.")

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

    if args.test_all or args.test_add:
        test_add()
        test_append()
        test_insert()
    if args.test_all or args.test_removal:
        test_remove_by_element()
        test_remove_by_index()
    if args.test_all or args.test_search:
        test_search()

if __name__ == "__main__":
    main()