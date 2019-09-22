from tree import *
import argparse

def parse_args():
    """
    parse_args: Parse command line arguments to test all
    or selected functionality of the BSTNode class.
    """
    parser = argparse.ArgumentParser()
    parser.add_argument('--test-all', action='store_true',
                        help='Test the functionality of ALL Tree methods')
    parser.add_argument('--test-insert', action='store_true',
                        help='Test the functionality of BSTNode.insert()')
    parser.add_argument('--test-remove', action='store_true',
                        help='Test the functionality of BSTNode.remove()')
    parser.add_argument('--test-find', action='store_true',
                        help='Test the functionality of BSTNode.search()')
    parser.add_argument('--test-traversals', action='store_true',
                        help='Test the functionality of the various BST traversals')
    parser.add_argument('--test-height', action='store_true',
                        help='Test the functionality of BSTNode.get_height()')
    args = parser.parse_args()
    return args

def test_insert():
    print_header(" Testing BST.insert() ")

    root = BSTNode(10)
    root.insert(BSTNode(5))
    root.insert(BSTNode(15))
    print("Binary Search Tree: \n{}".format(root))
    print("Adding a few more nodes")
    root.insert(BSTNode(7))
    root.insert(BSTNode(1))
    root.insert(BSTNode(20))
    print("Binary Search Tree: \n{}".format(root))
    
def test_remove():
    print_header(" Testing BST.remove(valid) ")

    root = BSTNode(10)
    root.insert(BSTNode(5))
    root.insert(BSTNode(15))
    root.insert(BSTNode(20))
    print("Binary Search Tree: \n{}".format(root))

    target = 15
    print("Removing node with value {}".format(15))
    node = root.remove(target)
    print("Binary Search Tree: \n{}".format(root))
    print("Confirm removal: \'{} in root\' = {}".format(target, target in root))
    
    print_header(" Testing BST.remove(invalid) ")

    print("Binary Search Tree: \n{}".format(root))

    target = 100
    print("Removing node with value: {}".format(target))
    node = root.remove(target)
    if node:
        print("Somehow found a non-existant node!")
    else:
        print("No node was found with value: {}".format(target))

def test_search():
    print_header(" Testing BST.search() ")

    root = BSTNode(10)
    root.insert(BSTNode(5))
    root.insert(BSTNode(15))
    root.insert(BSTNode(17))
    root.insert(BSTNode(2))
    root.insert(BSTNode(4))
    root.insert(BSTNode(25))
    
    print("Binary Search Tree: \n{}".format(root))

    target = 15
    print("Does the BST contain {}? -> {}".format(target, root.search(target)))
    target = 4
    print("Does the BST contain {}? -> {}".format(target, root.search(target)))
    target = 99
    print("Does the BST contain {}? -> {}".format(target, root.search(target)))
    target = -1
    print("Does the BST contain {}? -> {}".format(target, root.search(target)))

def test_traversals():
    print_header(" Testing the various BST traversals ")

    root = BSTNode(10)
    nodes = [BSTNode(5), BSTNode(20), BSTNode(3), BSTNode(6), BSTNode(15), BSTNode(25)]
    [root.insert(node) for node in nodes]

    print("Insertion Order: 10 > 5 > 20 > 3 > 6 > 15 > 25")
    print("Binary Search Tree: \n{}".format(root))
    print("Preorder:  {}".format(root.preorder_traversal([])))
    print("Inorder:   {}".format(root.inorder_traversal([])))
    print("Postorder: {}".format(root.postorder_traversal([])))

def test_height():
    print_header(" Testing the various BST traversals ")

    root = BSTNode(10)
    root.insert(BSTNode(5))
    root.insert(BSTNode(15))
    print("Binary Search Tree: \n{}".format(root))
    print("Height: {}".format(root.get_height()))

    print("\nAdding another level...")
    root.insert(BSTNode(4))
    print("Binary Search Tree: \n{}".format(root))
    print("Height: {}".format(root.get_height()))

    print("\nAdding yet ANOTHER level...")
    root.insert(BSTNode(3))
    print("Binary Search Tree: \n{}".format(root))
    print("Height: {}".format(root.get_height()))

    print("\nAdding node that should NOT affect tree height...")
    root.insert(BSTNode(6))
    print("Binary Search Tree: \n{}".format(root))
    print("Height: {}".format(root.get_height()))
    

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

    if args.test_all or args.test_insert:
        test_insert()
    if args.test_all or args.test_remove:
        test_remove()
    if args.test_all or args.test_find:
        test_search()
    if args.test_all or args.test_traversals:
        test_traversals()
    if args.test_all or args.test_height:
        test_height()

if __name__ == "__main__":
    main()
