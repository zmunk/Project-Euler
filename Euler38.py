# p = [1, 2, 3, 4, 5, 6, 7, 8, 9]
# for i in range(2,10):
#     q = p[0:i]
#     print q

def alliswell(s):
    if len(s) != 9:
        return False
    temp = []
    for i in range(len(s)):
        if s[i] == '0' or s[i] in temp:
            return False
        temp.append(s[i])
    return True

l = [918273645, 123456789]
for n in range(5000, 10000):
    result = ""
    for j in range(1, 3):
        result = result + str(n*j)
    if alliswell(result):
        l.append(int(result))

for n in range(100, 334):
    result = ""
    for j in range(1, 4):
        result = result + str(n * j)
    if alliswell(result):
        l.append(int(result))

max = 0
for i in range(len(l)):
    if l[i] > max:
        max = l[i]

print max