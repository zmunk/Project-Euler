def rect_count(m, n):
    return m * (m + 1) * n * (n + 1) // 4


def main():
    target = int(2e6)
    m = 1
    n = 1
    while rect_count(m, n) < target:
        n += 1

    min_diff = float("inf")
    closest = None
    while m < n:
        while (r := rect_count(m, n)) > target:
            n -= 1
        diff = abs(target - r)
        if diff < min_diff:
            closest = m * n
            min_diff = diff
        m += 1
    return closest


if __name__ == "__main__":
    print(main())
