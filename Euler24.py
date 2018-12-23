from math import *
def num(s):
    n = 10
    s = s - 1
    l = ""
    temp = []
    for i in range(n):
        temp.append(i)
    for i in range(n):
        x = n - i
        p = s/factorial(x-1)
        l = l + str(temp.pop(p))
        s = s - p*factorial(x-1)
    return int(l)
print num(1000000)