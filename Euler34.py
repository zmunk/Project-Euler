from math import *
i = 0
while i < 40586:
    s = str(i)
    r = 0
    for c in s:
        r = r + factorial(int(c))
        if r > i:
            break
    if r == i:
        print r
    i = i + 1

#TRICK QUESTION ALERT:
#The only curious numbers are 145 and 40585.