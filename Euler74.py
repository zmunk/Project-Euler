from functools import cache
from collections import deque
from itertools import count


def digits(n):
    while n > 0:
        yield n % 10
        n //= 10


@cache
def factorial(n):
    if n == 1 or n == 0:
        return 1
    return n * factorial(n - 1)


def sumfac(n):
    return sum(map(factorial, digits(n)))


def get_prechain_length(n, maxlen=60, verbose=0):
    seen = deque([n], maxlen=3)
    if verbose > 0:
        print(n, end=" ")
    for i in count(start=1):
        if maxlen is not None and i > maxlen:
            return None
        n = sumfac(n)
        if n in seen:
            if verbose > 0:
                print(i)
            return i
        seen.append(n)


if __name__ == "__main__":
    assert get_prechain_length(145) == 1
    assert get_prechain_length(169) == 3
    assert get_prechain_length(871) == 2
    assert get_prechain_length(872) == 2
    assert get_prechain_length(69) == 5
    assert get_prechain_length(78) == 4
    assert get_prechain_length(540) == 2

    cnt = 0
    for i in range(1, 1_000_000):
        if get_prechain_length(i) == 60:
            cnt += 1
    print(cnt)
