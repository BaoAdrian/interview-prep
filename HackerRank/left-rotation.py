# HackerRank
# Left Rotation

def left_rotation(arr, d):
    for i in range(d):
        temp = arr[0]
        for j in range(0, len(arr) - 1):
            arr[j] = arr[j+1]
        arr[-1] = temp
    print(" ".join([str(a) for a in arr]))

def main():
    left_rotation([1,2,3,4,5], 2)

if __name__ == "__main__":
    main()