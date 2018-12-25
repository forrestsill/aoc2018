with open("d3.txt") as f:
    i = 0
    oids, startw, starth, ws, hs = {}, {}, {}, {}, {}
    for line in f:
        oids[i] = line[1:line.index("@")-1]
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
ids = []
for i in range(maxh):
    vals.append([])
    ids.append([])
    vals[i] = [0] * maxw
    ids[i] = [None] * maxw
for i, h in enumerate(hs):
        for k in range(hs[i]):
            for l in range(ws[i]):
                vals[starth[i] + k][startw[i] + l] += 1
                if ids[starth[i] + k][startw[i] + l] is None:
                    ids[starth[i] + k][startw[i] + l] = []
                ids[starth[i] + k][startw[i] + l].append(oids[i])

count = 0
id = ""
out = []
for i in range(maxh):
    for j in range(maxw):
        if ids[i][j] is not None and len(ids[i][j]) > 1:
            for k in ids[i][j]:
                if int(k)-1 not in out:
                    out.append(int(k)-1)
        if vals[i][j] >= 2:
            count += 1
for i in oids:
    if i not in out:
        print(i+1)
