from math import *
# for a in range(1,10):
#     for b in range(1,10):
#         for c in range(1,10):
#             x = pow(a, 5)
#             y = pow(b, 5)
#             z = pow(c, 5)
#             if int("%d%d%d" % (a,b));
s = 0
for i in range(10, 1000000):
    temp = 0
    for c in str(i):
        x = int(c)
        temp = temp + pow(x, 5)
    if i == temp:
        s = s + i
        print i
print "total is %d" % s
