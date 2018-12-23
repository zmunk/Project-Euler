
inp = open('triangle.txt', 'r')
triangle = []
for line in inp:
    triangle.append([int(x) for x in line.split()])

j = len(triangle) - 1
while j > 0:
    top = triangle[j - 1]
    bottom = triangle[j]
    for i in range(len(triangle[j]) - 1):
        triangle[j - 1][i] = top[i] + max(bottom[i], bottom[i + 1])

    j -= 1

print triangle[0]