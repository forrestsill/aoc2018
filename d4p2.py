with open("d4.txt") as f:
    ts = {}
    for line in f:
        ts[line[:line.index("]")+1]] = line[line.index("]")+2:-1]
sorted = sorted(ts.items())
guard = ""
curr = 0
starts = {}
ends = {}
for (k, v) in sorted:
    if "begins shift" in v:
        guard = v[v.index("#")+1:v.index("b")-1]
    elif "wakes up" in v:
        startm = int(start[start.index(":")+1:start.index(":")+3])
        if guard not in starts:
            starts[guard] = []
        starts[guard].append(startm)
        endm = int(k[k.index(":")+1:k.index(":")+3])
        if guard not in ends:
            ends[guard] = []
        ends[guard].append(endm)
        curr += endm - startm
    elif "falls asleep" in v:
        start = k
max = 0
maxg = ""
for k, v in starts.items():
    curr = 0
    for (i, v) in enumerate(starts[k]):
        s = starts[k][i]
        e = ends[k][i]
        curr += (e - s)
    if curr > max:
        max = curr
        maxg = k
counts = {}
print(counts)
print(starts)
for (k, s) in starts.items():
    counts[k] = [0] * 60
    for (i, v) in enumerate(starts[k]):
        for j in range(v, ends[k][i]):
            counts[k][j] += 1
print(counts)
maxcount = 0
maxmin = 0
maxg = 0
for (k, v) in counts.items():
    for (i, n) in enumerate(counts[k]):
        if n > maxcount:
            maxcount = n
            maxmin = i
            maxg = k
print(int(maxg) * maxmin)
