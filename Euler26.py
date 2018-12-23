#print "0 .",
temp = []
rem = []
def div(temp, r, n):
    a = 10*r/n
    #print a,
    r = 10*r - a*n
    if r in temp:
        x = temp.index(r)
        #print "recurring start: ",
        #print temp[x:]
        #print "recurring digits: " + str(len(temp))
        return len(temp)
    else:
        temp.append(r)
    return div(temp,r,n)

longest = 0
for i in range(1,1001):
    temp = []
    x = div(temp,1,i)
    if x > longest:
        longest = x
        n = i
print longest
print n
# numofdict = {}
# def div2(num):
#     for newnum in range(1,num):
#         tempnum = (1.0/float(newnum))
#         print tempnum
#         numofdict[newnum] = tempnum
#     for values in numofdict.values():
#         templist = []
#         for digit in str(values):
#             templist.append(digit
#div2(20)