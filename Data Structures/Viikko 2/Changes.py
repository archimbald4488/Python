def changes(A):
    n = len(A)
    changed = 0

    for i in range(n - 1):
        if A[i] == A[i + 1]:
            changed += 1

            new = A[i] + 1
            if i + 2 < n and new == A[i + 2]:
                new += 1

            A[i + 1] = new

    return changed


if __name__ == "__main__":
    print(changes([1, 1, 2, 2, 2]))     # 2
    print(changes([1, 2, 3, 4, 5]))     # 0
    print(changes([1, 1, 1, 1, 1]))     # 2
