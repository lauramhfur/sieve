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
    while candidates:
        p = candidates[0]
        primes.append(p)
        candidates = [n for n in candidates if n % p]

    return primes


def slow_sieve(n: int) -> list[int]:
    """
    Compute all the primes up to (and possibly including) `n`.

    `n` must be positive.

    >>> slow_sieve(15)
    [2, 3, 5, 7, 11, 13]

    """
    assert n > 0

    candidates = list(range(2, n + 1))
    primes = []

    # This is a quick and easy solution that implements the sieve.
    # It is a bit slow, though (but that is a worry for another lesson)
    while candidates:
        p = candidates[0]
        primes.append(p)
        candidates = [n for n in candidates if n % p]

    return primes


def fast_sieve(n: int) -> list[int]:
    """
    Compute all the primes up to (and possibly including) `n`.

    `n` must be positive.

    >>> fast_sieve(15)
    [2, 3, 5, 7, 11, 13]

    """
    assert n > 0

    # Change candidates to include 0 and 1, so indices matches to values.
    # We won't use the values now, because we already have them as the index,
    # but use a boolean to indicate whether a candidate is eliminated.
    # Obviously, the first two indices area already elimiated
    candidates = [False] * 2 + [True] * (n - 1)

    # Now we run through the candidates (as their indices). We have the same
    # invariant, that the the first True candidate is a prime, and we will
    # eliminate all the following candidates if we can divide them.

    # We don't have to move i above sqrt(n), because those remaining candidates
    # above that cannot be divided by larger numbers. When we elimiate,
    # we can start at i**2, because between i and i^2 there can't be candidates
    # that i can eliminate.

    # It is because we scan through the candidates in larger and larger jumps,
    # and because we can cut off some of the search space, that this version is
    # faster than the more straightforward algorithm above.

    i = 2
    while i * i < n:
        if not candidates[i]:
            break  # no need to process this, it is eliminated
        for j in range(i**2, n+1, i):  # Jump in multiples of i
            candidates[j] = False  # i divides this one
        i += 1

    # The primes are those with True values
    return [i for i, b in enumerate(candidates) if b]
