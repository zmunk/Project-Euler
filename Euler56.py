
def digsum(n):
    s = str(n)
    r = 0
    for c in s:
        r = r + int(c)
    return r

max = 0
for a in range(1, 101):
    for b in range(1, 101):
        if digsum(a**b) > max:
            max = digsum(a**b)

print max