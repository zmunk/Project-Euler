from math import *
import time
def pfact(n, primes):
    if n == 1:
        return []
    for p in primes:
        if p > sqrt(n):
            return [n]
        # print p
        if n % p == 0:
            temp = 1
            while n % p == 0:
                temp = temp * p
                n = n / p
            return [temp] + pfact(n, primes)

def ptil(n):
    primes = [2, 3, 5]
    i = 7
    while i < n + 1:
        for p in primes:
            if p > sqrt(i):
                primes.append(i)
                break
            if i % p == 0:
                break
        i = i + (4 if i % 10 == 3 else 2)
    return primes

def func(n, p):
    return pfact(n, p)

# print ptil(10)
# print func(645)
st = time.time()
i = 1
p = ptil(100000)
while True:
    if len(func(i, p)) == len(func(i+1, p)) == len(func(i+2, p)) == len(func(i+3, p)) == 4:
        print i
        break
    i = i + 1

print "%.1f seconds" % (time.time() - st)