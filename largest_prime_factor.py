# coding=utf-8


def is_factor(value):
    """get factors of natural numbers"""
    factors = []

    if value < 2:
        return False

    for num in range(2, value):
        if value % num == 0:
            factors.append(num)

    return factors


def largest_prime_factor(func, value):
    """get largest prime factors from a list"""

    factors = func(value)
    primes = []
    for factor in factors:
        is_prime = True
        for prime in range(2, factor):
            if factor % prime == 0:
                is_prime = False
                break

        if is_prime:
            primes.append(factor)
    if primes != []:
        return dict(prime_factors=primes, max_prime_factor=max(primes))
    else:
        return dict(prime_factors=[], max_prime_factor=[])


if __name__ == '__main__':
    import timeit
    print(largest_prime_factor(is_factor, 1111))
    print(timeit.timeit("largest_prime_factor(is_factor, 1111)", globals=globals(), number=10000))
