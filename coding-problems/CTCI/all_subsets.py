"""
Powerset - pg 348
Write a method that returns all subsets of a given set

Time:  O(n * 2^n)
Space:  O(n * 2^n)
"""

def find_subsets(s, idx):
    all_subsets = []
    # Base case
    if (len(s) == idx):
        all_subsets = []
        all_subsets.append([]) # empty set
    else:
        all_subsets = find_subsets(s, idx+1)
        item = s[idx]
        more_subsets = []
        for subset in all_subsets:
            new_subset = []
            new_subset += subset
            new_subset.append(item)
            more_subsets.append(new_subset)
        all_subsets += more_subsets
    return all_subsets

def main():
    s = ['a', 'b']
    print(find_subsets(s, 0))


if __name__ == "__main__":
    main()

