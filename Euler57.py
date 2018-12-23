def rr(a, b):
    return [a + 2*b, a + b]
l = [3, 2]
count = 0
for i in range(1000):
    l = rr(l[0], l[1])
    if len(str(l[0])) > len(str(l[1])):
        count = count + 1
print count