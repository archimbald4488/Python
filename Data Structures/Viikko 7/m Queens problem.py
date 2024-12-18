def queen(n, m):

    # n queen problem from GeeksforGeeks used as inspiration: https://www.geeksforgeeks.org/n-queen-problem-backtracking-3/

    if m == 0: # no dots placed
        return 1
    if m > n: # can't place m dots
        return 0

    columns = [False] * n
    diag1 = [False] * (2 * n - 1)  # main diagonals (r - c + (n-1))
    diag2 = [False] * (2 * n - 1)  # anti diagonals (r + c)

    result = 0 

    # backtracking with helper function
    def backtrack(row, dots):
        nonlocal result
        
        if dots == m:
            result += 1
            return
        if row >= n:
            return

        for col in range(n):
            if not columns[col] and not diag1[row - col + (n - 1)] and not diag2[row + col]:
                columns[col] = diag1[row - col + (n - 1)] = diag2[row + col] = True # place the dot
                backtrack(row + 1, dots + 1)
                columns[col] = diag1[row - col + (n - 1)] = diag2[row + col] = False
        
        backtrack(row + 1, dots)

    backtrack(0, 0)

    return result


if __name__ == "__main__":
    print(queen(4, 4))
    print(queen(4, 2))
    print(queen(6, 4))
    print(queen(7, 2))
    print(queen(8, 8))
