def subsets(n: int) -> list:
    result = [[]] 
    
    # generate subsets
    for i in range(1, n + 1):
        result += [subset + [i] for subset in result]
    
    return result[1:]  # exclude the empty set


if __name__ == "__main__":
    print(subsets(1))
    print(subsets(2)) 
    print(subsets(3)) 
    print(subsets(4)) 

    S = subsets(10)
    print(S[95])
    print(S[254])
    print(S[826])
