"""
Author: DracoY
File: generator.py

This generates prime numbers.
"""

import prime

def prime_Generator(n: int):
    """Generates n number of primes.

    Returns --int

    Arguments:
        n {int} -- number of primes
    """

    i = 2
    count = 0

    while (count != n):
        if prime.checkPrime(i):
            yield i
            count += 1

        i += 1
