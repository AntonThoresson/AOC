lines = open("day10.txt").read().strip().split("\n")
# c = [1] - for part 1
c = []
X = 1


for line in lines:
    
    data = line.split()
    if len(data) < 2:
        c.append(X)
    else:
        c.append(X)
        c.append(X)
        X += int(data[1])

# c.append(X) - for part 1

# print(sum(x * y for x, y in list(enumerate(c))[20::40])) - for part 1


# PART 2
for row in range(0, len(c), 40):
    for col in range(40):
        print("#" if abs(c[row + col]-col) <= 1 else " ", end = "")
    print()
