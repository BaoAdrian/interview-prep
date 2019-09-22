
def main():
    # l = [1,2,4,5,5,5,5,7,9,10,12]
    l = [1,2,5,5,5,5,5]
    # l = [5]
    print(left_recursive_binary_search(l, 0, len(l), 5))
    print(recursive_binary_search(l, 0, len(l), 5))
    print(iterative_binary_search(l, 5))
    print(left_iterative_binary_search(l, 5))
    print(right_iterative_binary_search(l, 5))

def recursive_binary_search(data, left, right, key):
    # TODO: Still needs work
    if left <= right:
        i = (left + right) // 2
        if key < data[i]:
            return recursive_binary_search(data, left, i - 1, key)
        if key == data[i]:
            return i
        if key > data[i]:
            return recursive_binary_search(data, i+1, right, key)
    return -1

def left_recursive_binary_search(data, left, right, key):
    if left <= right:
        i = (left + right) // 2
        if key < data[i]:
            return left_recursive_binary_search(data, left, i-1, key)
        if key == data[i]:
            index = i
            return left_recursive_binary_search(data, left, i-1, key)
        if key > data[i]:
            return left_recursive_binary_search(data, i+1, right, key)
    return index

def iterative_binary_search(data, key):
    """
    iterative_binary_search: Iterative binary search
    that will find the first occurrence of the provided
    key, if it exists. Returns -1 otherwise.
    """
    left = -1
    right = len(data)

    while (left + 1 != right):
        i = (left + right) // 2
        if key < data[i]:
            right = i
        if key == data[i]:
            return i
        if key > data[i]:
            left = i
    return -1 # Doesn't exist

def left_iterative_binary_search(data, key):
    """
    left_iterative_binary_search: This modified version
    of the binary search algorithm will detect the LEFT
    MOST occurrence of the provided key.
    EX:
    l = [1,2,4,5,5,5,7,9,10,12]
    returns 3
    <Standard BS returns 5>
    """
    left = -1
    right = len(data)
    while (left + 1 != right):
        i = (left + right) // 2
        if key <= data[i]:
            right = i
            if left + 1 == right:
                return i
        if key > data[i]:
            left = i

    return -1 # Doesn't Exist

def right_iterative_binary_search(data, key):
    """
    right_iterative_binary_search: This modified version
    of the binary search algorithm will detect the RIGHT
    MOST occurrence of the provided key.
    EX:
    l = [1,2,5,5,5,5,5]
    returns 6
    <Standard BS returns 3>
    """
    left = -1
    right = len(data)
    while (left != right):
        i = (left + right) // 2
        if key < data[i]:
            right = i
        if key >= data[i]:
            left = i
            if left + 1 == right:
                return i

    return -1 # Doesn't Exist


if __name__ == "__main__":
    main()