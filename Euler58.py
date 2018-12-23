from math import *
import time
st = time.time()

n = 500000000
flags = [True] * (n / 2)
flags[0] = False
thresh = 0.1

primes = []
cpi = 2  # stands for checkpoint index
cp = 9  # stands for checkpoint, which is the next square of an odd number (bottom left diagonal)
count = 0  # counts number of primes on diagonals
for i, flag in enumerate(flags):
    if not flag:
        continue

    x = 2 * i + 1  # x is prime
    last = x
    primes.append(x)

    if x > cp:  # we have passed the checkpoint and completed a loop
        if float(count) / (4 * cpi - 3) < thresh:  # check if ratio of diagonal primes to total elements on diagonals is less than ten percent
            print "below %d%% at %d" % (int(thresh*100), cpi)  # means we succeeded
            break

        cpi += 1  # set next checkpoint index
        cp = 4 * cpi * cpi - 4 * cpi + 1  #set next checkpoint

    if (1.0 + sqrt(4 * x - 3)) % 4 == 0 or sqrt(x - 1) % 2 == 0 or (3.0 + sqrt(4 * x - 3)) % 4 == 0:  # check if x is on top right diagonal, top left diagonal, or bottom left diagonal
        count += 1

    if 2 * i + 1 <= sqrt(n):  # sieve code
        for j in xrange(2 * i * i + 2 * i, n / 2, 2 * i + 1):
            flags[j] = False

# last prime is 499999993
print "%.f seconds" % (time.time() - st)

n = (n/2)*2 + 1
while n < last*last:
    if n % 1000000 == 1:
        print "ratio is %f" % (float(count) / (4 * cpi - 3)),
        print "%.f seconds" % (time.time() - st)
    prime = True
    if n > cp:
        if float(count) / (4 * cpi - 3) < thresh:  # check if ratio of diagonal primes to total elements on diagonals is less than ten percent

            print "below %d%% at %d" % (int(thresh*100), cpi)  # means we succeeded
            break

        cpi += 1  # set next checkpoint index
        cp = 4 * cpi * cpi - 4 * cpi + 1  # set next checkpoint

    i = 0
    while True:
        p = primes[i]
        if p*p > n:
            break
        if n % p == 0:
            prime = False
            break
        i += 1

    if prime:
        if (1.0 + sqrt(4 * n - 3)) % 4 == 0 or sqrt(n - 1) % 2 == 0 or (3.0 + sqrt(4 * n - 3)) % 4 == 0:  # check if x is on top right diagonal, top left diagonal, or bottom left diagonal
            count += 1

    n += 2

print "%.3f%% square of side %d" % (count * 100.0 / (4 * cpi - 3), 2 * cpi - 1)
#9858 seconds below 10% at 13121 square of side 26241





