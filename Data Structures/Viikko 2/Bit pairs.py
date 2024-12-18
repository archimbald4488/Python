def pairs(s):

    indices = [i for i, bit in enumerate(s) if bit == '1']
    
    n = len(indices)
    
    # Use prefix sums to reduce complexity. Taken from: https://www.geeksforgeeks.org/prefix-sum-array-implementation-applications-competitive-programming/
    prefixSum = [0] * n
    prefixSum[0] = indices[0]
    for i in range(1, n):
        prefixSum[i] = prefixSum[i - 1] + indices[i]
    
    # get the the total distance
    distanceSum = 0
    for i in range(1, n):
        distanceSum += indices[i] * i - prefixSum[i - 1]
    
    return distanceSum


if __name__ == "__main__":
    print(pairs("100101"))          # 10
    print(pairs("101"))             # 2
    print(pairs("100100111001"))    # 71
