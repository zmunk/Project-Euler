def lych(n):
    r = n
    for i in range(50):
        r = r + rev(r)
        if ispal(r):
            return False
    return True

def ispal(n):
    s = str(n)
    length = len(s)
    for i in range(length/2):
        if int(s[i]) != int(s[- i - 1]):
            return False
    return True

def rev(n):
    s = str(n)
    result = ""
    for i in range(len(s)):
        result = s[i] + result
    return int(result)

count = 0
for i in range(1, 10000):
    if lych(i):
        count = count + 1

print count
