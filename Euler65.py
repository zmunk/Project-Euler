from itertools import count, islice


def get_values():
    for i in count(1):
        yield 1
        yield 2 * i
        yield 1


def sum_of_digits(val):
    return sum(map(int, str(val)))


n = 100
frac = (0, 1)
values = list(islice(get_values(), n - 1))[::-1]
for val in values[:]:
    frac = (frac[1], val * frac[1] + frac[0])
print(sum_of_digits(frac[0] + 2 * frac[1]))


print("---")
