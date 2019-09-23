# Cracking the Coding Interview
# 1.4 - Palindrome Permutation

def per_pal(string):
    counts = {}
    odd_count = False
    string = string.lower()
    for char in string:
        if char != " ":
            if char not in counts:
                counts[char] = 1
            else:
                counts[char] += 1

    for count in counts.values():
        if count % 2 != 0:
            if odd_count == True:
                return False
            else:
                odd_count = True
    return True

def main():
    print(per_pal("Tact coa"))

if __name__ == "__main__":
    main()
