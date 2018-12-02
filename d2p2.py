twos = 0
threes = 0
with open("d2.txt") as f:
    for line in f:
        counts = {}
        for l in line:
            if l in counts:
                counts[l] += 1
            else:
                counts[l] = 1
        hasTwo = False
        hasThree = False
        for c in counts.values():
            if c == 2:
                hasTwo = True
            if c == 3:
                hasThree = True
        if hasTwo:
            twos += 1
        if hasThree:
            threes += 1
total = twos * threes
print(total)
