import time
def primes():
    num = 0
    p = [2, 3, 5, 7]
    i = 11
    q = 739397
    while num < 10:
        f = True
        for c in p:
            if i % c == 0:
                f = False
                break
        if f:
            p.append(i)
            if allgood(i, p):
                num = num + 1
                q = q + i
                # print "%d num: %d" %(i, num)
        i = i + 2
    return q

def allgood(n, primes):
    s = str(n)
    for i in range(1,len(s)):
        if int(s[i:]) not in primes or int(s[:i]) not in primes:
            return False
    return True

st = time.time()

print primes()

print "%.1f seconds" % (time.time() - st)
#739397