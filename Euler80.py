from math import sqrt
import decimal

decimal.getcontext().prec = 102


def sqrt_dig_sum(n):
    digits = str(decimal.Decimal(n).sqrt()).replace(".", "")[:100]
    return sum(map(int, digits))


assert sqrt_dig_sum(2) == 475

acc = 0
for i in range(1, 100):
    if sqrt(i) % 1 == 0:
        continue
    acc += sqrt_dig_sum(i)
print(acc)
