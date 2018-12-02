sum = 0
with open("d1.txt") as f:
    for line in f:
        if line[0] == "+":
            sum += int(line[1:])
        else:
            sum -= int(line[1:])
print(sum)
