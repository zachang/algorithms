# coding=utf-8
from functools import  wraps


def sum_multiples(func):
    """Sum multiples of 3 and 5 for all natural numbers below 1000 decorator"""
    @wraps(func)
    def summed(*args, **kwargs):
        """Returning sum"""

        summation = func(*args, **kwargs)
        print(sum(summation))
        return summation

    return summed


@sum_multiples
def multiples(*args):
    """Get multiples of 3 and 5 for all natural numbers below 1000"""

    numbers = []

    for number in args[0]:
        if number % 3 == 0 and number % 5 == 0:
            numbers.append(number)

    return numbers


if __name__ == '__main__':
    range_list = range(1, 1000)
    multiples(range_list)
