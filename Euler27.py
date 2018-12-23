def isprime(primes, s):
    for p in primes:
        if s % p == 0:
            return False
    return True

def primeslist(x):
    primes = [2]
    i = 3
    while i < x + 1:
        if isprime(primes, i):
            primes.append(i)
        i = i + 1
    return primes

def quad(a, b, l, m, biggestprime):
    #print "n^2 + %d n + %d" % (a, b)
    n = 0
    cont = True
    p = 0
    while cont:
        x = n*n + a*n + b
        if x < 0 or x not in l:
            cont = False
        #print "%d is prime" % x
        p = p + 1
        if x > biggestprime:
            biggestprime = x
        n = n + 1
    if m < p:
        m = p
        print "%d and %d produce most consecutive primes, the product of which is %d" % (a, b, a*b)
        print
    return m,biggestprime


l = primeslist(1000)
m = biggestprime = 0
for a in range(-999, 1000):
    for b in l:
        m,biggestprime = quad(a,b,l,m,biggestprime)
print "m = ",
print m
print "biggestprime = ",
print biggestprime