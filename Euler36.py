import time
def dtb(n):
    if n == 0:
        return "0"
    if n == 1:
        return "1"
    return dtb(n/2) + str(n%2)

def pal(n):
    r = 0
    for i in range(1, n + 1):
        s = str(i)
        l = len(s)/2
        b = str(dtb(i))
        m = len(b)/2
        if s[:l] == s[:-l-1:-1] and  b[:m] == b[:-m-1:-1]:
            print "%d %s" % (i, b)
            r = r + i
    return r

st = time.time()
print pal(1000000)
# s = "backwards"
# n = 3
# print s[:-n-1:-1]

print "%.1f seconds" % (time.time() - st)