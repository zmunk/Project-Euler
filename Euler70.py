from itertools import combinations, count
from collections import Counter
from math import sqrt

prime_flags = 0b11
prime_last_checked = 3


def primes(safe=True):
    for i in count():
        if safe and i > prime_last_checked:
            return
        if (prime_flags >> i) & 1 == 0:
            yield i


def generate_primes_until(n):
    global prime_last_checked, prime_flags

    if prime_last_checked >= n:
        return

    for p in primes(safe=False):
        if p * p > n:
            break
        start = max(p * p, (prime_last_checked // p) * p + p)
        for i in range(start, int(n) + 1, p):
            prime_flags |= 1 << i

    prime_last_checked = int(n)


def get_count_relative_primes(n, pf):
    bases = next(zip(*pf))
    acc = 0
    for i in range(1, len(pf) + 1):
        k = (-1) ** ((i + 1) % 2)
        for ds in combinations(bases, i):
            prod = 1
            for base, pow in pf:
                prod *= base ** (pow - (1 if base in ds else 0))
            acc += prod * k
    return n - acc


class PrimeException(Exception):
    pass


def get_prime_factors(n):
    res = []
    for p in primes():
        c = 0
        while n % p == 0:
            c += 1
            n //= p
        if c > 0:

            if c > 1:
                raise PrimeException
            if p < 1229:
                raise PrimeException

            res.append((p, c))

            if len(res) > 2:
                raise PrimeException

        if n == 1:
            break
    if n > 1:
        res.append((n, 1))

    if len(res) != 2:
        raise PrimeException

    return res


lim = 1e7
generate_primes_until(sqrt(lim))

mn = float("inf")
for n in range(int(lim), 1, -1):
    try:
        pf = get_prime_factors(n)
    except PrimeException:
        continue
    m = get_count_relative_primes(n, pf)
    if Counter(str(n)) == Counter(str(m)):
        if n / m < mn:
            print(n, m, n / m)
            mn = n / m
