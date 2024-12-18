def jumps(n, a, b):
    
    # Inspiration for solution taken from the "Staircase problem": https://www.geeksforgeeks.org/python-program-for-count-ways-to-reach-the-nth-stair/

    waysArray = [0] * (n + 1) # initialize array
    waysArray[0] = 1 # always start the same way at level 0

    for i in range(1, n + 1):
        if i - a >= 0:
            waysArray[i] += waysArray[i - a] # reach level i by jumping with a
        if i - b >= 0:
            waysArray[i] += waysArray[i - b] # reach level i by jumping with b

    return waysArray[n]


if __name__ == "__main__":
    print(jumps(4, 1, 2))
    print(jumps(8, 2, 3))
    print(jumps(11, 6, 7))
    print(jumps(30, 3, 5))
    print(jumps(100, 4, 5))
