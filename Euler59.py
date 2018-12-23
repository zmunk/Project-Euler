val = 0
def dectobin(n):  # takes int returns str
    if n < 2:
        return str(n)
    if n % 2 == 0:  # if n is even
        return dectobin(n / 2) + "0"
    return dectobin(n / 2) + "1"

def bintodec(n): #takse str returns int
    if len(n) == 1:
        return int(n)
    return bintodec(n[:-1])*2 + int(n[-1])

def bin(n):
    n = dectobin(int(n))
    return "0"*(8 - len(n)) + n

def xor(m, n): #takes char
    m = bin(m)
    n = bin(ord(n))
    res = ""
    for i in range(8):
        if m[i] == n[i]:
            res += "0"
        else:
            res += "1"
    a = bintodec(res)
    return chr(bintodec(res))

def decrypt(code, key): #both lists, key length
    keylist = list(key)
    res = ""
    val = 0
    for i in range(len(code)):
        a = xor(code[i], keylist[i % 3])
        val += ord(a)
        res += a
    return val,res

inp = open("cipher.txt", "r")
ciph = inp.read().strip("\n").split(",")

key = "god"

a,b = decrypt(ciph, key)
# print a
print b
