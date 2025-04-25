from math import sqrt
import Euler70 as primelib


lim = int(5e7)
primelib.generate_primes_until(sqrt(lim))


def power_list(exp):
    res = []
    for p in primelib.primes():
        pp = p**exp
        if pp > lim:
            break
        res.append(pp)
    return res


def main():
    quads = power_list(4)
    cubes = power_list(3)
    squares = power_list(2)

    nums = set()
    for q in quads:
        for c in cubes:
            for s in squares:
                sum_ = q + c + s
                if sum_ > lim:
                    break

                nums.add(sum_)
    return len(nums)


if __name__ == "__main__":
    print(main())
