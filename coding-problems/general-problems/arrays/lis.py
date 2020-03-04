import copy

def LIS(A, n):
    DP = [[] for i in range(n)]

    DP[0] = [A[0]]
    for i in range(1, n):
        print(DP)
        for j in range(i):
            if A[i] > A[j]:
                DP[i] = copy.copy(DP[j])
        DP[i] += [A[i]]
    
    currMax = DP[0]
    for i in range(1, n):
        if len(DP[i]) > len(currMax):
            currMax = DP[i]
        
    return currMax

if __name__ == "__main__":
    A = [10,5,0,7,1,8,9,6,2,3,4]
    print(LIS(A, len(A)))