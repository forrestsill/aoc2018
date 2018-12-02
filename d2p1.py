def diff(line1, line2):
    diffs = 0
    word = ""
    for i, c in enumerate(line1):
        if line1[i] != line2[i]:
            diffs += 1
            if diffs > 1:
                return None
        else:
            word += c
    if diffs == 1:
        return word
    else:
        return None

lines = []
cont = True
with open("d2.txt") as f:
    lines = f.readlines()
for line in lines:
    if cont == False:
        break
    for line2 in lines:
        if diff(line, line2) != None:
            print(diff(line, line2))
            cont = False
            break
