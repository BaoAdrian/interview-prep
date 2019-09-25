"""
LeetCode: Valid Parentheses (#20)
https://leetcode.com/problems/valid-parentheses/

Given a string containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.

An input string is valid if:
    > Open brackets must be closed by the same type of brackets.
    > Open brackets must be closed in the correct order.

Note that an empty string is also considered valid.
"""
def is_valid_stack(s):
    if s == "":
        return True
    
    stack = []
    for c in s:
        if c in {'(', '{', '['}:
            stack.append(c)
        else:
            if not stack or stack.pop() + c not in {'()', '{}', '[]'}:
                return False
    
    if stack != []:
        return False
    return True

def main():
    string = "()"
    print("{} > {}".format(string, is_valid_stack(string)))

    string = "(}"
    print("{} > {}".format(string, is_valid_stack(string)))

    string = "([])"
    print("{} > {}".format(string, is_valid_stack(string)))

    string = "[{({[[[()]]]})}]"
    print("{} > {}".format(string, is_valid_stack(string)))

if __name__ == "__main__":
    main()
