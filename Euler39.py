n = 120
def sides(n):
    result = 0
    for i in range(n/3, n - 1):
        for j in range((n-i+1)/2, n - i):
            k = n - i - j
            if i*i == j*j + k*k:
                result = result + 1
                # print "%d %d %d" % (i, j, k)
    return result

max = 0
for i in range(1001):
    if max < sides(i):
        maxnum = i
        max = sides(i)
print maxnum

