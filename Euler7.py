p = [2]
i = 3
while len(p) < 10001:
    for j in p:
        if j * j > i:
            p.append(i)
            break
        if i % j == 0:
            break
    i += 2
print p[-1]