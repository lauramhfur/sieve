# This directory will be checked with pytest. It will examine
# all files that start with test_*.py and run all functions with
# names that start with test_

from sieve import sieve


def test_sieve() -> None:
    """Test Eratosthenes sieve."""
    assert sieve(1) == []
    assert sieve(2) == [2]
    assert sieve(3) == [2, 3]
    assert sieve(4) == [2, 3]
    assert sieve(5) == [2, 3, 5]
    assert sieve(6) == [2, 3, 5]
    assert sieve(7) == [2, 3, 5, 7]
    assert sieve(8) == [2, 3, 5, 7]
    assert sieve(9) == [2, 3, 5, 7]
    assert sieve(10) == [2, 3, 5, 7]
    assert sieve(11) == [2, 3, 5, 7, 11]
    assert sieve(12) == [2, 3, 5, 7, 11]
    assert sieve(13) == [2, 3, 5, 7, 11, 13]
