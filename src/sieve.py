"""Computing primes."""


def sieve(n: int) -> list[int]:
    """
    Compute all the primes up to (and possibly including) `n`.

    `n` must be positive.

    >>> sieve(15)
    [2, 3, 5, 7, 11, 13]

    """
    assert n > 0
    candidates = list(range(2, n + 1))
    primes = []

    # FIXME: fill out this bit
    
    # List comprehension method
    primes = [p for p in candidates if all(p % j != 0 for j in candidates if p != j)]

    # Loop method  
    for p in candidates:                 # Crpteria 3: You are always assuming that the smallest number, 2, is a prime number.
        for j in candidates:
            if p != j:
                if j % p == 0:           # Criteria 2: Testing if a number, "j" can be divided by a prime number, so that the remainder is 0.
                    candidates.remove(j) # Criteria 2: if a number can be divided by a prime number, then it's not a prime number, so we remove "j" in that case.
        primes.append(p)                 # Criteria 2: Since we always remove all other numbers, we know that "i" is always a prime number, also due to criteria 3.
    return primes                        # Criteria 1: Checking that all numbers in "primes" are prime numbers.

print(sieve(15))

