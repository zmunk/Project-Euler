
lim = 5
a = 1
d = {}
while True:
    n = a**3
    s = list(str(n))
    s.sort(reverse=True)
    t = int(''.join(s))
    if t == 987655433210:
        print n
        break
    if t not in d:
        d[t] = 1
    elif d[t] == lim - 1:
        print t
        break
    else:
        d[t] += 1
    a += 1
