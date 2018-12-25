with open("d3.txt") as f:
    i = 0
    startw, starth, ws, hs = {}, {}, {}, {}
    for line in f:
        startw[i] = int(line[line.index("@")+2:line.index(",")])
        starth[i] = int(line[line.index(",")+1:line.index(":")])
        ws[i] = int(line[line.index(":")+2:line.index("x")])
        hs[i] = int(line[line.index("x")+1:])
        i+=1
maxh = maxw = 0
for i, v in enumerate(starth):
    if startw[i] + ws[i] > maxw:
        maxw = startw[i] + ws[i]
    if starth[i] + hs[i] > maxh:
        maxh = starth[i] + hs[i]
vals = []
for i in range(maxh):
    vals.append([])
    vals[i] = [0] * maxw
for i, h in enumerate(hs):
        for k in range(hs[i]):
            for l in range(ws[i]):
                vals[starth[i] + k][startw[i] + l] += 1

count = 0
for i in range(maxh):
    for j in range(maxw):
        if vals[i][j] >= 2:
            count += 1
print(count)
