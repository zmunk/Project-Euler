from math import *
def eratos(n):
    f = [True]*(n+1)
    f[0] = f[1] = False
    p = []
    for i, c in enumerate(f):
        if not c:
            continue
        p.append(i)
        if i <= sqrt(n):
            for j in xrange(i*i, n+1, i):
                f[j] = False
    return p
primes = eratos(1000000)
for a in range(10):
    for b in range(10):
        for x in range(1, 10, 2):
            for j in range(4):
                for k in range(4 - j):
                    c = 0
                    l = []
                    for i in range(10):
                        s = str(i)*j + str(a) + str(i)*k + str(b) + str(i)*(3 - j - k) + str(x)
                        if s[0] != '0' and int(s) in primes:
                            c = c + 1
                            l.append(s)
                    if c == 8:
                        print l #['121313', '222323', '323333', '424343', '525353', '626363', '828383', '929393']