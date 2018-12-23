temp = []
for a in range(2,101):
    for b in range(2,101):
        s = 1
        for i in range(b):
            s = a*s
        if s not in temp:
            temp.append(s)
print temp
print len(temp)