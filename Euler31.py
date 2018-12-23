# def method1():
#     a = 200
#     for h in range(a/200 + 1):
#         # print "200*%d + " % h,
#         a = a - 200*h
#         for g in range(a/100 + 1):
#             # print "100*%d + " % g,
#             a = a - 100*g
#             for f in range(a/50 + 1):
#                 # print "50*%d + " % f,
#                 a = a - 50*f
#                 for e in range(a/20 + 1):
#                     # print "20*%d + " % e,
#                     a = a - 20*e
#                     for d in range(a/10 + 1):
#                         # print "10*%d + " % d,
#                         a = a - 10*d
#                         for c in range(a/5 + 1):
#                             # print "5*%d + " % c,
#                             a = a - 5*c
#                             for b in range(a/2 + 1):
#                                 # print "2*%d + " % b,
#                                 a = a - 2*b
#                                 print "200*%d + 100*%d + 50*%d + 20*%d + 10*%d + 5*%d + 2*%d + 1*%d = 200" % (h,g,f,e,d,c,b,a)




# print len(val)
# def method2(val, a, i):
#     if i == 7:
#         if a > 0:
#             print "1*%d" % a
#         print ""
#         return
#     for x in range(a/val[i] + 1):
#         # print x
#         if x > 0:
#             print "%d*%d " % (x, a),
#         asdf(val, a - val[i]*x, i + 1)

# method2(val, 200, 0)

# method1()
val = [200, 100, 50, 20, 10, 5, 2, 1]
def method3(val, rem, n):
    if n == 6:
        return rem/2 + 1
    result = 0
    x = val[n]
    for i in range(rem/x + 1):
        a = rem - i*x
        result = result + method3(val, a, n + 1)
    return result
print method3(val, 200, 0)