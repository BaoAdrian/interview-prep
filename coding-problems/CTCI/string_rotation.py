"""
String Rotation (pg 207)

Assume you have a method isSubstring() which checks if one word is a 
substring of another. Given two substrings, s1 ad s2, write code to 
check if s2 is a rotation of s1 using only one call to isSubstring

Example:
'waterbottle' is a rotation of 'erbottlewat'

Idea:
Need to split the strings into partitions, x and y, such that their 
results are equivalent when swapped. For example,
s1 = waterbottle
s2 = erbottlewat

We partition x and y
x = wat
y = erbottle

s1 = xy = wat + erbottle
s2 = yx = erbottle + wat

Taking this further, we can see that yx will ALWAYS be a substring of xyxy.
For example,
yx = erbottlewat
xyxy = wat[erbottlewat]erbottle (where yx is denoted with brackets)

Therefore, yx must be a substring of xyxy
"""

def is_rotation(s1, s2):
    if (len(s1) == len(s2) and len(s1) > 0):
        xyxy = s1 + s1
        if is_substring(s1, xyxy):
            return True
    return False        

def is_substring(s1, s2):
    return s1 in s2

def main():
    s1 = "waterbottle"
    s2 = "erbottlewat"
    print("\'{}\' is a rotation of \'{}\': {}\n".format(s1, s2, is_rotation(s1, s2)))

    s1 = "testingthis"
    s2 = "nope"
    print("\'{}\' is a rotation of \'{}\': {}\n".format(s1, s2, is_rotation(s1, s2)))

if __name__ == "__main__":
    main()