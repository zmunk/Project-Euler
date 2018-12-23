from math import *
import time
st = time.time()
def func():
    a = 1
    while True:
        x = a*(a+1)/2
        if ((sqrt(float(x)*24 + 1) + 1)/6)%1 == 0 and ((sqrt(float(x)*8 + 1) + 1)/4)%1 == 0 and x > 40755:
            return x
        a = a + 1

print func()
print "%.1f seconds" % (time.time() - st)