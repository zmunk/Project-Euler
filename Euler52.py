def samedig(m, n):
    s = str(m)
    p = str(n)
    if len(s) != len(p):
        return False
    if len(s) == 1 and s == p:
        return True
    x = s[0]
    if len(s.replace(x, "")) == len(p.replace(x, "")):
        return samedig(int(s.replace(x, "", 1)), int(p.replace(x, "", 1)))

    return False

i = 1
while True:
    if samedig(i, 2*i):
        if samedig(i, 3*i):
            if samedig(i, 4*i):
                if samedig(i, 5*i):
                    if samedig(i, 6*i):
                        print i
                        break
    i = i + 1