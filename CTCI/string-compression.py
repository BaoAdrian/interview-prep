# LeetCode
# String Compression

def stringCompression(string):
    final_string = None
    curr_char = None
    curr_count = 0
    for char in string:
        if curr_char is not None and char != curr_char:
            final_string += curr_char + str(curr_count)
            curr_char = char
            curr_count = 1
        else:
            curr_count += 1
        
    if len(final_string) == string:
        return string
    return final_string

def main():
    return_str = stringCompression("aabcccccaa")
    print(return_str)

if __name__ == "__main__":
    main()