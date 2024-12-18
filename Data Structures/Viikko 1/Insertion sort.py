def isort(A):
    # TODO
    for i in range(1, len(A)):
        j = i - 1
        while j >= 0 and A[j] > A[j+1]:
            new = A[j]
            A[j] = A[j + 1]
            A[j + 1] = new
            j -= 1

if __name__ == "__main__": 
    A = [4, 3, 6, 2, 9, 7, 1, 8, 5]
    isort(A)
    print(A)  # [1, 2, 3, 4, 5, 6, 7, 8, 9]
