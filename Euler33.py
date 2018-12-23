def func():
    tr = br = 1
    t = 0
    for i in range(1,10):
        for j in range(1,10):
            a = int(str(i) + str(j))
            for k in range(1,10):
                b = int(str(j) + str(k))
                c = int(str(k) + str(i))
                f = False
                if a < b and float(a)/b == float(i)/k:
                    print str(i) + str(j) + "/" + str(j) + str(k), #a/b
                    tr = tr * i
                    br = br * k
                    f = True
                if a < c and float(a)/c == float(j)/k:
                    print str(i) + str(j) + "/" + str(k) + str(i), #a/c
                    tr = tr * i
                    br = br * k
                    f = True
                if f and t < 3:
                    print " * ",
                    t = t + 1
                    f = False
    return {'tr': tr, 'br': br}
# func()
# print "%d/%d" % (func()['tr'], func()['br'])
def simplify(m,n):
    i = 2
    while i < m + 1:
        if m % i == 0 and n % i == 0:
            m = m / i
            n = n / i
            # print "%d/%d" % (m, n)
            i = 2
            continue
        i = i + 1
    return {'tr': m, 'br': n}
s = func()
y = simplify(s['tr'], s['br'])
print " = %d/%d" % (y['tr'], y['br'])