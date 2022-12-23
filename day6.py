f = open("day6.txt", "r")
data = f.read().strip()

# PART 1
i = 0
while True:
    s = data[i : (i+4)]
    if len(set(list(s))) == 4:
        print(i+4)
        break
    i += 1


# PART 2
i = 0
while True:
    s = data[i : (i+14)]
    if len(set(list(s))) == 14:
        print(i+14)
        break
    i += 1


