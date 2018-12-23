import time
def func(a, n):
    if n < 9*(a + 1)*pow(10, a) + 1:
        return str(pow(10, a) + n/(a + 1))[n - (n/(a + 1))*(a + 1)]
    return func(a + 1, n - 9*(a + 1)*pow(10, a))

def find(n):
    return int(func(0, n - 1))

def test(n):
    s = ""
    for i in range(1, 1000):
        s = s + str(i)
    return int(s[n - 1])

st = time.time()
# for j in range(100000):
r = 1
for i in range(7):
    r = r*find(pow(10, i))
print r
print "%f seconds" % (time.time() - st)
