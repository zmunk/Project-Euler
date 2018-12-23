import time
from math import *

def isprime(s, primes):
    lim = int(sqrt(s))
    for p in primes:
        if p > lim:
            return True
        if s % p == 0:
            return False

def isprime2(s, primes):
    lim = int(sqrt(s))
    # print lim
    for p in primes:
        if p > lim:
            return True
        if s % p == 0:
            return False

def ptil(lim):
    primes = [2]
    i = 3
    while i < lim:
        if isprime(i, primes):
            primes.append(i)
        i = i + 2
    return primes


def ptot(start):
    primes = [2]
    if start == 1:
        tot = 2
    else:
        tot = 0
    i = 3
    s = 1
    while s < 546:
        if isprime(i, primes):
            if s > start - 1:
                tot = tot + i
            primes.append(i)
            s = s + 1
            # if tot == 997651:
                # print "yes!"
        i = i + 2
    # print s
    # print primes
    # print primes[546-1]
    return tot

st = time.time()
#
i = 1
l = ptil(1100)
# print l
while True:
    # print ptot(i),
    if isprime2(ptot(i), l):
        print ptot(i)
        break
    i = i + 1


print "%.5f seconds" % (time.time() - st)