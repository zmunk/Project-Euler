import Euler70 as primelib
from Euler72 import LoadingContextManager
from functools import cache
from itertools import count

with LoadingContextManager("generating primes ...", "primes generated"):
    primelib.generate_primes_until(1e3)


@cache
def get_num_ways(n, lim=None):
    if n == 0:
        return 1
    if n == 1:
        return 0
    res = 0
    for p in primelib.primes(throw_exception=True):
        if (lim is not None and p > lim) or p > n:
            break
        res += get_num_ways(n - p, lim=p)
    return res


@cache
def get_ways(n, lim=None, depth=0):
    if n == 0:
        return [()]
    if n == 1:
        return []
    assert n > 1
    res = []
    for p in primelib.primes():
        if (lim is not None and p > lim) or p > n:
            break
        for way in get_ways(n - p, lim=p, depth=depth + 1):
            res.append((p, *way))
    return res


for i in count(start=1):
    if get_num_ways(i) > 5000:
        print(i)
        break
print("done")
