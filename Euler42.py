def vals():
    m = tri(192)
    inp = open('words2.txt',"r")
    r = inp.read().lower().replace('"', "").replace(",", " ")
    r = r + " "
    print r
    sum = 0
    l = []
    count = 0
    temp = ""
    max = 0
    for c in r:
        temp = temp + c
        if c == ' ':
            # print temp
            l.append(sum)    #max = 145
            if sum > max:
                max = sum
            if sum in m:
                # print temp,
                # print sum
                count = count + 1
            sum = 0
            temp = ""
            continue
        sum = sum + ord(c) - 96
    # print max
    return count

def tri(lim):
    result = []
    i = 1
    while True:
        n = i*(i+1)/2
        if n > lim:
            return result
        result.append(n)
        i = i + 1

# print tri(146)
print vals()
