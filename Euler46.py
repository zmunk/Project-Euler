from math import *
def ptil(n):
    primes = [2]
    i = 3
    while i < n + 1:
        for p in primes:
            if p > sqrt(i):
                primes.append(i)
                break
            if i % p == 0:
                break
        i = i + (4 if i % 10 == 3 else 2)
    return primes

n = 100000
ps = ptil(n)
# print ps
i = 3
while i < n:
    if i in ps:
        i = i + 2
        continue
# i = 5777
# if True:
    for p in ps:
        # print p,
        if p > i:
            print i
            break
        # print sqrt((float(i) - p) / 2)
        if sqrt((float(i) - p)/2) % 1 == 0:
            break
    i = i + 2
