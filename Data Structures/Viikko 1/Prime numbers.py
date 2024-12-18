def primes(N: int) -> int:
    if N == 1:
        return

    prime = [True] * (N + 1)
    prime[0] = False
    prime[1] = False

    # Using sieve of eratosthenes as my algorithm, example taken from: https://www.geeksforgeeks.org/sieve-of-eratosthenes/
    p = 2
    while p * p <= N:
        if prime[p]:
            for i in range(p * p, N + 1, p):
                prime[i] = False
        p += 1

    amount = 0

    for p in range(2, N + 1):
        if prime[p]:
            amount += 1

    return amount


if __name__ == "__main__":
    print(primes(7))    # 4
    print(primes(15))   # 6
    print(primes(50))   # 15
