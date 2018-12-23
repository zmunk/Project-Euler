import time
st = time.time()

r = 0
for i in range(1, 1000):
    r = r + int(str(pow(i, i))[-10:])
print str(r)[-10:]

print "%.6f seconds" % (time.time() -st)