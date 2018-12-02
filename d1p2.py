sum = 0
sums = {}
cont = True
with open("d1.txt") as f:
    while cont == True:
        for line in f:
            if line[0] == "+":
                sum += int(line[1:])
            else:
                sum -= int(line[1:])
            if sum in sums:
                print(sum)
                cont = False
                break
            else:
                sums[sum] = True
        f.seek(0)
