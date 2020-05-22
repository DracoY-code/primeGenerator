"""
Author: DracoY
File: prime_check.py

This checks if a number is prime or not.
"""

def checkPrime(number: int, i: int = 2):
    """This function checks if a number is prime.

    Returns --bool
    
    Arguments:
        number {int} -- number to be checked

    Keyword Arguments:
        check {int} -- check situation (default: {number})
    """

    try:
        if number <= 2:
            return True if (number == 2) else False

        if (number % i) == 0:
            return False

        if (i * i) > number:
            return True

        return checkPrime(number, i + 1)

    except TypeError:
        raise TypeError("Int required!")

    except RecursionError:
        raise RecursionError
