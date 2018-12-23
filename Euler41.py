from math import *
import time
def num(s, n):
    l = ""
    temp = []
    for i in range(1, n + 1):
        temp.append(i)
    for i in range(n):
        x = n - i
        p = s/factorial(x-1)
        l = l + str(temp.pop(p))
        s = s - p*factorial(x-1)
    return int(l)

def isprime(s, primes):
    for p in primes:
        if s % p == 0:
            return False
    return True

def ptil(n):
    result = [2]
    i = 3
    while i < n + 1:
        if isprime(i,result):
            result.append(i)
        i = i + 1
    return result

def func():
    l = ptil(2766)
    i = 7
    t = 0
    for j in range(factorial(i)):
        s = str(num(j, i))
        if s[-1] not in ['0', '2', '4', '5', '6', '8']:
            t = t + 1
            # print s
            m = int(sqrt(int(s)))
            for p in l:
                if p > m - 1:
                    print s,
                    print j
                    break
                if int(s) % p == 0:
                    # print "%d is divisible by %d " % (int(s), p)
                    break
    print t
st = time.time()
# func()
l = ptil(2766)
t = 0
for i in range(4917, 5040):
    s = str(num(i, 7))
    if s[-1] not in ['0', '2', '4', '5', '6', '8']:
        if isprime(int(s),l):
            print s
print t
print "%.1f seconds" % (time.time() - st)
