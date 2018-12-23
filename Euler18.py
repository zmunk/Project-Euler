inp = open('pyramidfinal.txt')

nums = []
for line in inp:
    nums.append(line.split())

def rec(count):
    temp = []
    rowab = nums[count]
    if count == len(nums) - 1:
        return nums[-1]
    else:
        x = rec(count + 1)
    for i in range(len(x)-1):
        temp.append(max(int(x[i]), int(x[i+1])) + int(rowab[i]))
    return temp

print rec(0)