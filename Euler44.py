import time
from math import *
st = time.time()
def func(lim):
    a = 1
    while a < lim:
        for n in range(1, lim - a):
            d = 3*a*n + a*(3*a - 1)/2
            t = d + 3*n*n - n
            if ((sqrt(float(t)*24 + 1) + 1)/6)%1 == 0 and ((sqrt(float(d)*24 + 1) + 1)/6)%1 == 0:
                print "n is %d and a is %d" % (n, a)
                return d
        a = a + 1

print func(2190)

print "%.1f seconds" % (time.time() - st)