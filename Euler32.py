from math import *
def num(s):
    n = 9
    l = ""
    temp = []
    for i in range(1,n+1):
        temp.append(i)
    for i in range(n):
        x = n - i
        p = s/factorial(x-1)
        l = l + str(temp.pop(p))
        s = s - p*factorial(x-1)
    return l
def func():
    clist = []
    p = 0
    for i in range(factorial(9)):
        s = num(i)
        c = int(s[5:])
        for j in range(1, 5):
            a = int(s[:j])
            b = int(s[j:5])
            if a * b == c and c not in clist:
                clist.append(c)
                p = p + c
    return p
print func()