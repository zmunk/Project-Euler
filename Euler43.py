from math import *
import time

def num(n, s):
    # n = 10
    # s = s - 1
    l = ""
    temp = []
    for i in range(n):
        temp.append(i)
    for i in range(n):
        x = n - i
        p = s/factorial(x-1)
        l = l + str(temp.pop(p))
        s = s - p*factorial(x-1)
    return l

def func(s, sum):
    primes = [2, 3, 5, 7, 11, 13, 17]
    for j in range(1, 8):
        if int(s[j:j + 3]) % primes[j-1] != 0:
            return sum
    # print s
    return sum + int(s)

def func2():
    sum = 0
    for i in range(factorial(10)):
        s = num(10, i)
        if s[0] != '0' and s[3] in ['0', '2', '4', '6', '8'] and s[5] in ['0', '5']:
            # print s
            sum = func(s, sum)
    return sum

st = time.time()
print func2()
print "%.1f seconds" % (time.time() - st)

