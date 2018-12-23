import time
from math import *

def eratos(n):
    flags = [True]*(n+1) # [True, True, True, True]
    flags[0] = flags[1] = False
    primes = []
    for i, flag in enumerate(flags):
        if not flag:
            continue
        if i > 1000:
            primes.append(i)
        if i <= sqrt(n):
            for j in xrange(i*i, n+1, i):
                flags[j] = False
    return primes

def perm(s):
    result = []
    if len(s) == 1:
        return [s]
    for c in range(len(s)):
        for l in perm(s[:c] + s[c+1:]):
            if s[c] + l not in result:
                result.append(s[c] + l)
    return result

def differences(t):
    l = len(t)
    result = []
    found = False
    mins = []
    maxs = []
    for i in range(l - 1):
        for c in t[i+1:]:
            if abs(t[i] - c) in result:
                ind = result.index(abs(t[i] - c))
                if any(i in [mins[ind], maxs[ind]] for i in [t[i], c]):
                    print mins[ind], maxs[ind], c
            mins.append(min(t[i], c))
            maxs.append(max(t[i], c))
            result.append(abs(t[i] - c))
    if found:
        print t
    return result

st = time.time()
primes = eratos(10000)
b = []
l = []
for p in primes:
    s = str(p)
    temp = []
    for d in perm(s):
        if int(d) in primes and int(d) not in b:
            b.append(int(d))
            temp.append(int(d))
    if len(temp) >= 3:
        l.append(temp)
for i in range(len(l)):
     differences(l[i])


print "%.2f seconds" % (time.time() - st)