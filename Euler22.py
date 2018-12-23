inp = open('names.txt',"r")
gays = inp.read().lower().replace('"',"").split(',')
gays.sort()

def nameval(name):
    a =[ord(char) - 96 for char in name.lower()]
    return sum(a)


result = 0
for i in range(len(gays)):
    result = result + (i+1)*nameval(gays[i])
print result

