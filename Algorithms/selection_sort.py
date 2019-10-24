import random
import time

def swap(nums, i, j):
    temp = nums[i]
    nums[i] = nums[j]
    nums[j] = temp

def selection_sort(nums):
    for i in range(len(nums)):
        low = i
        for j in range(len(nums) - 1, i, -1):
            if nums[j] < nums[low]:
                low = j
        swap(nums, i, low)
    return nums

def selection_sort_tweaked(nums):
    for i in range(len(nums)):
        low = i
        for j in range(len(nums) - 1, i, -1):
            if nums[j] < nums[low]:
                low = j
    if low != i:
        swap(nums, i, low)
    return nums

def main():
    nums = [random.randint(1,1000) for i in range(100000)]
    start = time.time()
    selection_sort(nums)
    end = time.time()
    standard_duration = end - start # seconds

    start = time.time()
    selection_sort_tweaked(nums)
    end = time.time()
    tweaked_duration = end - start # seconds

    print("Standard Selection Sort: {} seconds".format(standard_duration))
    print("Tweaked Selection Sort: {} seconds".format(tweaked_duration))


if __name__ == "__main__":
    main()