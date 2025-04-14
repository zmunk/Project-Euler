import pickle
from itertools import combinations
from math import prod, sqrt
from pathlib import Path
from time import perf_counter
from collections import defaultdict
import Euler70 as primelib


class LoadingContextManager:
    """
    e.g.:
    ```
    with LoadingContextManager(
        "generating prime factors ...", "prime factors generated"
    ):
        prime_factors = generate_prime_factors(lim)
    ```
    """

    def __init__(self, msg, exit_msg) -> None:
        self.msg = msg
        self.exit_msg = exit_msg

    def __enter__(self):
        print(self.msg, end="\r")
        self.start_time = perf_counter()

    def __exit__(self, *_):
        print(" " * len(self.msg), end="\r")  # clear line
        elapsed_time = perf_counter() - self.start_time
        print(self.exit_msg, f"({elapsed_time:.2f} s)")


def run(func):
    """
    Place this decorator on a function you want to run without needing to call
    the function explicitly.
    The function should have no arguments.
    """
    return func()


def generate_prime_factors(lim, reload_cache=False):

    cache_file = f"prime_factors_{int(lim)}.pkl"
    if not reload_cache and Path(cache_file).exists():
        return pickle.load(open(cache_file, "rb"))

    prime_factors_dict = {
        i: {"rem": i, "factors": defaultdict(int)} for i in range(1, int(lim) + 1)
    }
    for p in primelib.primes():
        for i in range(p * p, int(lim) + 1, p):
            data = prime_factors_dict[i]
            while data["rem"] % p == 0:
                data["factors"][p] += 1
                data["rem"] //= p
    for i in range(1, int(lim) + 1):
        data = prime_factors_dict[i]
        if data["rem"] > 1:
            data["factors"][data["rem"]] += 1
    prime_factors = {i: dict(data["factors"]) for i, data in prime_factors_dict.items()}

    with open(cache_file, "wb") as f:
        pickle.dump(prime_factors, f)

    return prime_factors


def get_num_reduced(base):
    pf = list(prime_factors[base].keys())
    em = elimination_multiplier(pf)
    for key, val in prime_factors[base].items():
        for _ in range(val - 1):
            em *= key
    return base - em


def elimination_multiplier(factors, degree=None):
    if degree is None:
        degree = len(factors) - 1
    if degree == 0:
        return 1
    return sum(
        prod(combo) for combo in combinations(factors, degree)
    ) - elimination_multiplier(factors, degree=degree - 1)


if __name__ == "__main__":
    lim = 1e6
    primelib.generate_primes_until(sqrt(lim))
    prime_factors = generate_prime_factors(lim, reload_cache=False)
    acc = 0
    for i in range(2, int(lim) + 1):
        acc += get_num_reduced(i)
    print(acc)
