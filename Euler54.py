inp = open('poker.txt')

hands1 = []
hands2 = []
for l in inp:
    hands1.append(l[:14].strip("\n"))
    hands2.append(l[15:].strip("\n"))

def val(hand):
    cards = ['2', '3', '4', '5', '6', '7', '8', '9', 'T', 'J', 'Q', 'K', 'A']
    l = hand.split(" ")
    n = [x[0] for x in l]
    s = [x[1] for x in l]
    samesuit = False
    for i in range(1, 5):
        if l[i][1] != l[0][1]:
            break
    else:
        samesuit = True
    royal = ['T', 'J', 'Q', 'K', 'A']
    if samesuit:
        for i in range(5):
            if s[i] not in royal:
                break
        else:
            return 1000 #royal flush
    rank = []
    for i in range(5):
        rank.append(cards.index(n[i]))
    highest = max(rank)
    lowest = min(rank)
    count = [0] * 13
    for c in n:
        ind = cards.index(c)
        count[ind] = count[ind] + 1
    consec = False
    for i in range(5):
        v = cards.index(n[i])
        if max(count) != 1 or v != highest and v != lowest and (cards[min((v + 1),12)] not in n or cards[abs(v - 1)] not in n):
            break
    else:
        print "consec", hand
        consec = True
    if samesuit and consec:
        return 900 + highest #straight flush
    if count[ind] == 4:
        return 800 + count.index(4) #four of a kind
    if 3 in count and 2 in count:
        return 700 + count.index(3) #full house
    if samesuit:
        return 600  + highest #flush
    if consec:
        return 500 + highest #straight
    if 3 in count:
        return 400 + count.index(3) #three of a kind
    if count.count(2) == 2:
        return 300 + sum([i for i, x in enumerate(count) if x == 2])
    if 2 in count:
        return 200 + count.index(2)
    return 100 + highest

count = [0,0]
i = 0
while True:
    try:
        a = val(hands1[i])
        b = val(hands2[i])
        if a == b:
            pass
        elif a < b:
            count[1] = count[1] + 1
        else:
            count[0] = count[0] + 1
    except IndexError:
        break
    i = i + 1
print count