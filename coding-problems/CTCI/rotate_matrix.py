"""
Rotate Matrix (pg203)

Given an image representing an NxN matrix, where each pixel
in the image is representeed by an integer, wirte a method to 
rotate the image by 90 degress. Can you do this in place?


for i = 0 to n:
    temp = top[i]
    top[i] = left[i]
    left[i] = bottom[i]
    bottom[i] = right[i]
    right[i] = temp

Example:
Matrix:
1 1 1 1 
0 2 3 0 
0 4 4 0 
1 1 1 1 

Rotated Matrix:
1 0 0 1 
1 4 2 1 
1 4 3 1 
1 0 0 1 
"""

def rotate(matrix):
    if not matrix or len(matrix) != len(matrix[0]):
        return None

    n = len(matrix)

    for layer in range(n//2):
        first = layer
        last = n - 1 - layer
        i = first
        while i < last:
            offset = i - first
            top = matrix[first][i]

            # left -> top
            matrix[first][i] = matrix[last-offset][first]

            # bottom -> left
            matrix[last-offset][first] = matrix[last][last-offset]

            # right -> bottom
            matrix[last][last-offset] =  matrix[i][last]

            # top -> right
            matrix[i][last] = top
            i += 1


    return matrix

def main():
    matrix = [
        [1,1,1,1],
        [0,2,3,0],
        [0,4,4,0],
        [1,1,1,1]
    ]
    print_matrix(matrix)
    print()
    matrix = rotate(matrix)
    if matrix:
        print_matrix(matrix)

def print_matrix(matrix):
    for row in range(len(matrix)):
        string = ""
        for col in range(len(matrix)):
            string += str(matrix[row][col]) + " "
        print(string)

if __name__ == "__main__":
    main()

