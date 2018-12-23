
a = 0
b = 0

alist = [1]
blist = [89]
for n in range(1, 10000001):
    while n not in [1, 89]:
        temp = 0
        for c in str(n):
            temp += int(c) ** 2
        n = temp
    if n == 89:
        b += 1
print b