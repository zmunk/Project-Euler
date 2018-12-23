

p = 1
for _ in range(7830457):
    p = p * 2 % (10**10)
print p * 28433 % (10**10) + 1