# coding=utf-8
from functools import reduce


def power_sum(power):
    """
    Calculates the resulting digits from sum of 2 to the power of n; 
    n being a natural number <= 1000000
    """

    value = str(2 ** power)
    value_list = list(value)
    _sum = reduce((lambda x, y: int(x) + int(y)), value_list)
    return _sum

if __name__ == '__main__':
    print(power_sum(15))
