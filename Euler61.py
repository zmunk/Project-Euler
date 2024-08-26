from itertools import count


def find_polygon_numbers(polygon_function) -> list:
    arr = []
    for i in count():
        n = polygon_function(i)
        if n < 1e3:
            continue
        if n >= 1e4:
            return arr
        arr.append(n)
    raise RuntimeError()


def octagonal_function(i):
    return i * (3 * i - 2)


def heptagonal_function(i):
    return i * (5 * i - 3) // 2


def hexagonal_function(i):
    return i * (2 * i - 1)


def pentagonal_function(i):
    return i * (3 * i - 1) // 2


def square_function(i):
    return i * i


def triangle_function(i):
    return i * (i + 1) // 2


for i, v in enumerate([1, 8, 21, 40, 65], start=1):
    assert octagonal_function(i) == v

for i, v in enumerate([1, 7, 18, 34, 55], start=1):
    assert heptagonal_function(i) == v

for i, v in enumerate([1, 6, 15, 28, 45], start=1):
    assert hexagonal_function(i) == v

for i, v in enumerate([1, 5, 12, 22, 35], start=1):
    assert pentagonal_function(i) == v

for i, v in enumerate([1, 4, 9, 16, 25], start=1):
    assert square_function(i) == v

for i, v in enumerate([1, 3, 6, 10, 15], start=1):
    assert triangle_function(i) == v


def get_rest(poly, ignore_index):
    """flatten rest"""
    arr = []
    for i, sub_arr in enumerate(poly):
        if i == ignore_index:
            continue
        arr += sub_arr
    return arr


def process(num, ignore_indices, history=[]):
    for index, arr in enumerate(poly):
        if index in ignore_indices:
            continue
        for n in arr:
            if n % 100 == num // 100:
                if len(history) >= 4 and n // 100 == history[0] % 100:
                    return history + [num, n]
                if res := process(n, ignore_indices + [index], history + [num]):
                    return res


poly = [
    find_polygon_numbers(octagonal_function),
    find_polygon_numbers(heptagonal_function),
    find_polygon_numbers(hexagonal_function),
    find_polygon_numbers(pentagonal_function),
    find_polygon_numbers(square_function),
    find_polygon_numbers(triangle_function),
]
for num in poly[0]:
    if res := process(num, [0]):
        print(sum(res))
        break
