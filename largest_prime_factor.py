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


def largest_prime_factor(func):
    """get largest prime factors from a list"""

    factors = func(10000)
    primes = []
    print("factors:", factors)
    for factor in factors:
        is_prime = True
        for prime in range(2, factor):
            if factor % prime == 0:
                is_prime = False
                break

        if is_prime:
            primes.append(factor)
    return dict(prime_factors=primes, max_prime_factor=max(primes))


if __name__ == '__main__':
    # import timeit
    print(largest_prime_factor(is_factor))
    # print(timeit.timeit("largest_prime_factor(is_factor)", globals=globals(), number=10000))
