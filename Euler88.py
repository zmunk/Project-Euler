from math import prod
from itertools import count, islice
from collections import defaultdict
from Euler72 import run


def variations(arr: tuple):
    if arr[0] == 2:
        yield (2, *arr)
    for i in range(len(arr)):
        arr_cp = list(arr)
        if i == len(arr) - 1 or arr_cp[i] < arr_cp[i + 1]:
            arr_cp[i] += 1
            yield tuple(arr_cp)


def gen():
    vault = defaultdict(set)

    def save(arr: tuple):
        vault[prod(arr)].add(arr)

    save((2,))
    for n in count(2):
        for arr in vault[n]:
            yield arr
            for var in variations(arr):
                save(var)

    return


# @run
def test_gen():
    print("test running")
    last = 0
    for arr in islice(gen(), 10):
        prod_ = prod(arr)
        assert prod_ >= last
        last = prod_


def main():
    lim = 12_000
    nums = set()
    unchecked = set(range(2, lim + 1))
    for arr in gen():
        k = prod(arr) + len(arr) - sum(arr)
        if k in unchecked:
            nums.add(prod(arr))
            unchecked.remove(k)
        if len(unchecked) == 0:
            break
    return sum(nums)


if __name__ == "__main__":
    test_gen()
    print(main())
