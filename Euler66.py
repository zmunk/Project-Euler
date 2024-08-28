from typing import Iterator
from math import sqrt
from itertools import count, cycle, islice


def continued_fraction(val) -> Iterator[int]:
    a0 = int(sqrt(val))
    seen = {}
    history = []
    (a, b, c) = (a0, 0, 1)
    repeat = []
    for i in count():
        state = (a, b, c)
        if state in seen:
            repeat = history[seen[state] :]
            break
        seen[state] = i
        history.append(a)
        yield a
        d = a * c - b
        b, c = d, (val - d * d) // c
        a = (a0 + b) // c
    yield from cycle(repeat)


def get_sqrt_approximation(d, num_terms) -> tuple[int, int]:
    a, b = 0, 1
    for val in list(islice(continued_fraction(d), num_terms))[::-1]:
        a, b = b, a + val * b
    return a, b


# https://en.wikipedia.org/wiki/Pell%27s_equation

mx = (0, None)
for d in range(2, 1001):
    if int(sqrt(d)) ** 2 == d:
        continue
    for i in count(1):
        y, x = get_sqrt_approximation(d, num_terms=i)
        if x * x - d * y * y == 1:
            if x > mx[0]:
                mx = (x, d)
            break
print(mx[1])
