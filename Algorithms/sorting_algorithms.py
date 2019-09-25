

def main():
    nums = [1,6,8,2,3,1,5,6]
    print(bubble_sort(nums))
    print(selection_sort(nums))
    print(insertion_sort(nums))
    print(shell_sort(nums))
    print(merge_sort(nums))
    print(quick_sort(nums))

def bubble_sort(nums):
    """
    [1,5,7,2]
     ^ ^
    [1,5,7,2]
     ^   ^
    [1,5,7,2]
     ^     ^
    [1,5,7,2]
       ^ ^
    [1,5,7,2]
       ^   ^
    [1,2,7,5]
         ^ ^
    [1,2,7,5] DONE
    """
    for i in range(len(nums)):
        for j in range(i, len(nums), 1):
            if nums[i] > nums[j]:
                temp = nums[i]
                nums[i] = nums[j]
                nums[j] = temp
    return nums

def selection_sort(nums):
    """
    Search for the max value (*) and insert 
    at the current end position.
    [1,5,7,2]
         * ^ 
    [1,5,2,7]
       * ^
    [1,2,5,7]
       *       (Already at correct position)
    [1,5,7,2]
     *         (Already at correct position)
    DONE
    """
    for i in range(len(nums) - 1, 0, -1):
        
        # Find max position
        max_pos = 0
        for j in range(1, i+1):
            if nums[j] > nums[max_pos]:
                max_pos = j
        
        temp = nums[i]
        nums[i] = nums[max_pos]
        nums[max_pos] = temp

    return nums

def insertion_sort(nums):
    """
    Start at the first element and insert each subsequent
    element (^) in the growing sorted sublist (*).
    [1,5,7,2,6,4,9]
     * ^
    [1,5,7,2,6,4,9]
     * * ^
    [1,5,7,2,6,4,9]
     * * * ^
    [1,2,5,7,6,4,9]
     * * * * ^
    [1,2,5,6,7,4,9]
     * * * * * ^
    [1,2,4,5,6,7,9]
     * * * * * * ^
    [1,2,4,5,6,7,9]
     * * * * * * * DONE
    """
    for i in range(len(nums)):
        curr = nums[i]
        pos = i
        while pos > 0 and nums[pos] > curr:
            nums[pos] = nums[pos - 1]
            pos -= 1
        nums[pos] = curr
    return nums

def shell_sort(nums):
    """
    Break list into sublist of a specified gap size and sort
    those elements. Each subsequent iteration, shrink gap size
    until list is sorted.
    [1 5 7 2 6 4 9]
     1 --- 2
       5 --- 6
         7 --- 4
                 9
    [1 5 4 2 6 7 9]
     1 - 4
       5 - 2
             6 - 9
               7
    [1 2 4 5 6 7 9]
     1 2
         4 5
             6 7 
                 9
    [1 2 4 5 6 7 9] DONE      
    """
    def gap_insertion_sort(nums, start, gap):
        for _ in range(start + gap, len(nums), gap):
            curr = nums[start]
            pos = 1
            while pos >= gap and nums[pos - gap] > curr:
                nums[pos] = nums[pos-gap]
                pos -= gap
            nums[pos] = curr
        return nums

    sublist_size = len(nums) // 2
    while sublist_size > 0:
        for start_pos in range(sublist_size):
            gap_insertion_sort(nums, start_pos, sublist_size)
        sublist_size = sublist_size // 2
    return nums


def merge_sort(nums):
    """
    Recursively split the lists into sublists containing a single
    or no element making the list sorted by definition if it contains
    a single element list (or no elements). Then begin the merge process
    zipping up the sorted sublists comparing corresponding elements and
    inserting into the correct position
    [7 2 6 9 3 5 1 8]
    
    > [7 2 6 9] 
    > [7 2] & [6 9] 
    > [7] & [2] & [6] & [9] (BEGIN MERGE)
    > [2 7] & [6 9] > [2 6 7 9] *** 
    
    > [3 5 1 8]
    > [3 5] & [1 8] 
    > [3] & [5] & [1] & [8] (BEGIN MERGE))
    > [3 5] & [1 8] > [1 3 5 8] ***
    
    [2 6 7 9]
              > Merge Sorted sublists > [1 2 3 5 6 7 8 9]
    [1 3 5 8]

    NOTE: Uncomment the print statements to view the process
    of splitting and merging
    """
    # print("Splitting: {}".format(nums))
    if len(nums) > 1:
        mid = len(nums) // 2
        left = nums[:mid]
        right = nums[mid:]

        # Recursively split/sort sublists
        merge_sort(left) 
        merge_sort(right) 

        # Merge sorted left and right sublists
        merge(nums, left, right)
        
    # print("Merging: {}".format(nums))
    return nums

def merge(nums, left, right):
    """
    merge: Merges the left and right sublists into nums
    traversing both lists and performing comparisons to insert
    the correct values into the sorted list.
    """
    i, j, k = 0,0,0
    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            nums[k] = left[i]
            i += 1
        else:
            nums[k] = right[j]
            j += 1
        k += 1
    
    while i < len(left):
        nums[k] = left[i]
        i += 1
        k += 1
    
    while j < len(right):
        nums[k] = right[j]
        j += 1
        k += 1
    return nums

def quick_sort(nums):
    return quick_sort_helper(nums, 0, len(nums) - 1)

def quick_sort_helper(nums, first, last):
    """
    This implementation uses the first value as the 
    initial pivot
    """
    if first < last:
        split = partition(nums, first, last)
        quick_sort_helper(nums, first, split - 1)
        quick_sort_helper(nums, split + 1, last)
    return nums
    
def partition(nums, first, last):
    pivot = nums[first]

    left = first + 1
    right = last
    
    done = False
    while not done:
        while left <= right and nums[left] <= pivot:
            left += 1
        while nums[right] >= pivot and right >= left:
            right -= 1
        
        if right < left:
            done = True
        else:
            temp = nums[left]
            nums[left] = nums[right]
            nums[right] = temp

    temp = nums[first]
    nums[first] = nums[right]
    nums[right] = temp

    return right



if __name__ == "__main__":
    main()