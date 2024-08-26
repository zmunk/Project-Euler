from itertools import count
from math import sqrt


def get_period(val) -> int:
    a0 = int(sqrt(val))
    seen = {}
    (a, b, c) = (a0, 0, 1)
    for i in count():
        state = (a, b, c)
        if state in seen:
            return i - seen[state]
        seen[state] = i
        d = a * c - b
        b, c = d, (val - d * d) // c
        a = (a0 + b) // c
    raise RuntimeError


acc = 0
for val in range(2, 10_001):
    if int(sqrt(val)) ** 2 == val:
        continue
    if get_period(val) % 2 == 1:
        acc += 1
print(acc)
exit(0)

#############################
# The rest is for debugging #
#############################

SQRT = "\u221a"


def signed(n):
    if n < 0:
        return f"- {abs(n)}"
    else:
        return f"+ {n}"


def format1(val, b, c, mult=1):
    """
    '(√val + b) / c'

    e.g. '(√23 + 3) / 2'
        where val = 23, b = 3, c = 2
    """
    assert b >= 0
    res = f"{SQRT}{val}"
    if mult > 1:
        res = str(mult) + res
    if b > 0:
        res = f"({res} + {b * mult})"
    # res = "("
    # res += f"{SQRT}{val} + {b * mult})"
    if c > 1:
        res += f" / {c * mult}"
    return res


def format2(a, val, d, c):
    """
    'a + (√val - d) / c'

    e.g. '3 + (√23 - 3) / 2'
        where a = 3, val = 23, d = 3, c = 2
    """
    res = f"{a} + ({SQRT}{val} - {d})"
    if c > 1:
        res += f" / {c}"
    return res


def format3(c, val, d):
    """
    'c / (√23 - d)'

    e.g. '7 / (√23 - 3)'
        where c = 7, val = 23, d = 3
    """
    return f"{c} / ({SQRT}{val} - {d})"


def get_fraction(val, verbose=0):
    a0 = int(sqrt(val))

    b, c = 0, 1
    a = a0

    for _ in range(10):
        yield a
        d = a * c - b
        assert (val - d * d) % c == 0
        e = (val - d * d) // c
        if verbose > 0:
            print(format1(val, b, c), "=", format2(a, val, d, c), f"= {a} + 1/X")
            print(
                "   X =",
                format3(c, val, d),
                "=",
                format1(val, d, e, mult=c),
                "=",
                format1(val, d, e),
            )
            print()

        b, c = d, e
        a = (a0 + b) // c
