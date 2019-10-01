"""
Sort Array By Parity (#905)
https://leetcode.com/problems/sort-array-by-parity/

Given an array A of non-negative integers, return an array consisting of 
all the even elements of A, followed by all the odd elements of A.
You may return any answer array that satisfies this condition.

Example:
Input: [3,1,2,4]
Output: [2,4,3,1]
The outputs [4,2,3,1], [2,4,1,3], and [4,2,1,3] would also be accepted.

Note:
1, 1 <= A.length <= 5000
2. 0 <= A[i] <= 5000
"""

def sort_by_mod(arr):
    """ Beats 12 % """
    output = []
    for num in sorted(arr):
        if num % 2 == 0:
            output.insert(0, num)
        else:
            output.append(num)
    return output

def sort_by_bitwise(arr):
    """ Beats 12% """
    output = []
    for num in sorted(arr):
        if num & 1 == 0:
            output.insert(0, num)
        else:
            output.append(num)
    return output

def sort_by_bitwise_oneliner(arr):
    """ Beats 56% """
    return sorted(arr, key=lambda x: x & 1)

def sort_by_replacement(arr):
    """ Beats 99% """
    i, j = 0, len(arr) - 1
    while i <= j:
        if arr[i] % 2 != 1:
            i += 1
            continue
            
        if arr[j] % 2 != 0:
            j -= 1
            continue
        
        arr[i], arr[j] = arr[j], arr[i]
        i += 1
        j -= 1
        
    return arr
