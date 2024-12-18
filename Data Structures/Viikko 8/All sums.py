def sums(items):

    # inspiration for subset sums taken from: https://www.geeksforgeeks.org/python-program-for-subset-sum-problem-dp-25/

    sums = {0} # create dict for sums

    for number in items:
        newSums = {x + number for x in sums} # create new sums by adding number to each of the current sums
        sums.update(newSums)

    return len(sums) - 1  # exclude initial 0


if __name__ == "__main__":
    print(sums([1, 2, 3]))                  
    print(sums([2, 2, 3]))                  
    print(sums([1, 3, 5, 1, 3, 5]))         
    print(sums([1, 15, 5, 23, 100, 55, 2])) 
