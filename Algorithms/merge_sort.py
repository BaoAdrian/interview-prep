class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

    def __str__(self):
        return_str = ""
        curr = self
        while curr:
            return_str += "[ {} ] > ".format(curr.value)
            curr = curr.next
        return return_str

def merge_sort_linked_list(ll):
    # Case of NULL or single Node
    if ll == None or ll.next == None:
        return ll

    # Split list into left/right halves
    left, right = split_list(ll)

    left = merge_sort_linked_list(left)
    right = merge_sort_linked_list(right)
    ll = merge(left, right)
    return ll

def split_list(ll):
    slow = ll
    fast = ll.next

    while fast:
        fast = fast.next
        if fast != None:
            slow = slow.next
            fast = fast.next
    
    left = ll
    right = slow.next
    slow.next = None
    return left, right

def merge(left, right):
    head, curr = None, None

    # Merge lists
    while left and right:
        if left.value <= right.value:
            if head == None:
                
                head = left
                curr = left
            else:
                curr.next = left
                curr = curr.next
            left = left.next
        else:
            if curr == None:
                head = right
                curr = right
            else:
                curr.next = right
                curr = curr.next
            right = right.next
    
    # Cleanup
    if left == None:
        curr.next = right
    if right == None:
        curr.next = left
    
    return head
        

if __name__ == "__main__":
    head = Node(3)
    second = Node(6)
    third = Node(2)
    fourth = Node(1)
    head.next = second
    second.next = third
    third.next = fourth
    print("Input: {}".format(head))
    head = merge_sort_linked_list(head)
    print("Sorted: {}".format(head))
