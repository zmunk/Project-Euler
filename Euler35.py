import time

def primes(n):
    p = [2]
    i = 3
    st = time.time()
    while i < n:
        f = True
        for c in p:
            if i % c == 0:
                f = False
                break
        if f:
            p.append(i)
        i = i + 2
    print p
    print "%.1f seconds" % (time.time() - st) #284.8 seconds for n = 1,000,000

def circ(n):
    p = [2]
    i = 3
    nep = [2]
    # st = time.time()
    while i < n:
        # if haseven(i):
        #     i = i + 2
        #     continue
        f = True
        for c in p:
            if i % c == 0:
                f = False
                break
        if f:
            p.append(i)
            if not haseven(i):
                nep.append(i)
        i = i + 2
    return nep
    # print "%.1f seconds" % (time.time() - st)

def haseven(n):
    s = str(n)
    for c in s:
        if int(c) % 2 == 0:
            return True
    return False

st = time.time()
def meth(n):
    pot = circ(n)
    r = 0
    for c in pot:
        s = str(c)
        # print s + " ",
        l = len(s)
        esc = False
        for i in range(l-1):
            s = s[1:] + s[0]
            # print s + " ",
            if int(s) not in pot:
                # print esc,
                esc = True
                break
        if esc:
            # print ""
            continue
        print c
        r = r + 1
        # print not esc
    return r

print "%d primes" % meth(1000000) #answer is 55, took 146.2 seconds
# print circ(100)
print "%.1f seconds" % (time.time() - st)