from math import *

count = 0
n = 1
while True:
    x = 1
    a = int(n * log(x, 10))
    while a <= n - 1:
        if a == n - 1:
            count += 1
            print count
        x += 1
        a = int(n * log(x, 10))
    n += 1

    # doesn't continue after 49, so 49 is the answer