def split(T):
    n = len(T)
    
    # Use prefix sums like in the last exercise. Taken from: https://www.geeksforgeeks.org/prefix-sum-array-implementation-applications-competitive-programming/
    # Additional inspiration taken from: https://www.geeksforgeeks.org/index-with-minimum-sum-of-prefix-and-suffix-sums-in-an-array/
    
    prefixMax = [0] * n
    prefixMax[0] = T[0]
    for i in range(1, n):
        prefixMax[i] = max(prefixMax[i - 1], T[i])
    
    suffixMin = [0] * n
    suffixMin[n - 1] = T[n - 1]
    for i in range(n - 2, -1, -1):
        suffixMin[i] = min(suffixMin[i + 1], T[i])
    
    # count the total splits
    splits = 0
    for i in range(n - 1):
        if prefixMax[i] < suffixMin[i + 1]:
            splits += 1
    
    return splits


if __name__ == "__main__":
    print(split([1,2,3,4,5]))       # 4
    print(split([5,4,3,2,1]))       # 0
    print(split([2,1,2,5,7,6,9]))   # 3
    print(split([1,2,3,1]))         # 0
