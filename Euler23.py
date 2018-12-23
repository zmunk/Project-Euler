import time
def isabund(n):
    result = 0
    for i in range(1, n/2 + 1):
        if n % i == 0:
            result = result + i
    if result > n:
        return n
    else:
        return 0

def abunlist(n):
    result = []
    for i in range(n+1):
        x = isabund(i)
        if x != 0:
            result.append(x)
    return result

def method1():
    start_time = time.time()

    abun = abunlist(28123)
    l = len(abun)
    dif = range(1, 28124)
    s = 0
    for i in range(l):
        for j in range(l):
            try:
                x = abun[i] + abun[j]
                dif.remove(x)
                s = s + x
            except ValueError:
                pass
    print s #this value is the sum of all numbers under 28123 that are the sum of two abundant numbers
    # found it, s = 391285755, took a solid 15-20 min

    # print 395465626 - 391285755

    print "%s seconds" % (time.time() - start_time)

def method2(n):
    start_time = time.time()
    abun = []
    abunsum = []
    totsum = 0
    for i in range(1,n+1):
        div = 0
        for j in range(1, i/2 + 1):
            if i % j == 0:
                div = div + j
        if div > i:
            abun.append(i)
            for a in abun[:-1]:
                f = i + a
                if f > n:
                    break
                if f not in abunsum:
                    abunsum.append(f)
                    totsum = totsum + f
    print totsum
    print "%s seconds" % (time.time() - start_time)

method2(10000) #solved for 10000 : 46273932  in 135.457999945 seconds