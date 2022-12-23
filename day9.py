visited = set([(0, 0)])

head = [0, 0]
tail = [0, 0]


for line in open("day9.txt"):
    x, y = line.split()
    y = int(y)

    for _ in range(y):
        dx = 1 if x == "R" else -1 if x == "L" else 0
        dy = 1 if x == "U" else -1 if x == "D" else 0

        head[0] += dx
        head[1] += dy

        diffX = head[0] - tail[0]
        diffY = head[1] - tail[1]

        if abs(diffX) > 1 or abs(diffY) > 1:
            if diffX == 0:
                tail[1] += diffY // 2
            elif diffY == 0:
                tail[0] += diffX // 2
            else :
                tail[0] += 1 if diffX > 0 else -1
                tail[1] += 1 if diffY > 0 else -1
        visited.add(tuple(tail))
print(len(visited))

# PART 2


visited2 = set([(0, 0)])
rope = [[0, 0] for _ in range(10)]

for line in open("day9.txt"):
    x, y = line.split()
    y = int(y)

    for _ in range(y):
        dx = 1 if x == "R" else -1 if x == "L" else 0
        dy = 1 if x == "U" else -1 if x == "D" else 0

        rope[0][0] += dx
        rope[0][1] += dy

        for i in range(9):
            head = rope[i]
            tail = rope[i+1]

            diffX = head[0] - tail[0]
            diffY = head[1] - tail[1]

            if abs(diffX) > 1 or abs(diffY) > 1:
                if diffX == 0:
                    tail[1] += diffY // 2
                elif diffY == 0:
                    tail[0] += diffX // 2
                else :
                    tail[0] += 1 if diffX > 0 else -1
                    tail[1] += 1 if diffY > 0 else -1
            visited2.add(tuple(rope[-1]))
print(len(visited2))



