from math import sqrt
from itertools import count
import Euler70 as primelib
from Euler72 import generate_prime_factors

if __name__ == "__main__":
    lim = 12000
    primelib.generate_primes_until(sqrt(lim))
    prime_factors = generate_prime_factors(lim)

    cnt = 0
    for denom in range(4, lim + 1):
        pf = prime_factors[denom]
        for val in count(int(denom / 3) + 1):
            if val * 2 >= denom:
                break
            for p in pf:
                if val % p == 0:
                    break
            else:
                cnt += 1
    print(cnt)
